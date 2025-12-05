import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs

PORT = 3000
DB_FILE = "db.json"


class GenericMockHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def load_db(self):
        with open(DB_FILE, "r") as f:
            return json.load(f)

    def do_GET(self):
        parsed = urlparse(self.path)
        path_parts = parsed.path.strip("/").split("/")
        resource = path_parts[0] if path_parts else None

        db = self.load_db()

        # Caso base: / (root)
        if not resource:
            self._set_headers()
            self.wfile.write(json.dumps(db).encode())
            return

        # Verifica se la risorsa esiste nel DB
        if resource not in db:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Resource not found"}).encode())
            return

        data = db[resource]

        # Caso: /resource/ID (es: /projects/101)
        if len(path_parts) == 2 and path_parts[1].isdigit():
            item_id = int(path_parts[1])
            item = next((x for x in data if x["id"] == item_id), None)
            if item:
                self._set_headers()
                self.wfile.write(json.dumps(item).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Item not found"}).encode())
            return

        # Caso: /resource (con filtri query params)
        query = parse_qs(parsed.query)
        filtered_data = data

        for key, value in query.items():
            # Filtro semplice (es: ?dev_id=1)
            # Nota: converte in int se il dato originale è int
            val = value[0]
            filtered_data = [x for x in filtered_data if str(x.get(key)) == val]

        self._set_headers()
        self.wfile.write(json.dumps(filtered_data).encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = json.loads(self.rfile.read(content_length))
        post_data["id"] = 999  # ID generato fake
        self._set_headers(201)
        self.wfile.write(json.dumps(post_data).encode())

    def do_PUT(self):
        content_length = int(self.headers["Content-Length"])
        put_data = json.loads(self.rfile.read(content_length))
        # Preserva l'ID dall'URL se presente
        path_parts = self.path.strip("/").split("/")
        if len(path_parts) == 2 and path_parts[1].isdigit():
            put_data["id"] = int(path_parts[1])
        self._set_headers(200)
        self.wfile.write(json.dumps(put_data).encode())

    def do_DELETE(self):
        self._set_headers(200)
        self.wfile.write(json.dumps({}).encode())


print(f"--- SERVER VERIFICA ATTIVO SU PORTA {PORT} ---")
print("Risorse disponibili: developers, projects, tasks")
print("Premi Ctrl+C per interrompere")
with socketserver.TCPServer(("", PORT), GenericMockHandler) as httpd:
    httpd.serve_forever()
