import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs

PORT = 3001
DB_FILE = 'es12_db_biblioteca.json'

class BibliotecaHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def load_db(self):
        with open(DB_FILE, 'r') as f:
            return json.load(f)

    def do_GET(self):
        parsed = urlparse(self.path)
        path_parts = parsed.path.strip('/').split('/')
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
        
        # Caso: /resource/ID (es: /books/1001)
        if len(path_parts) == 2 and path_parts[1].isdigit():
            item_id = int(path_parts[1])
            item = next((x for x in data if x['id'] == item_id), None)
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
            val = value[0]
            filtered_data = [
                x for x in filtered_data 
                if str(x.get(key)) == val
            ]

        self._set_headers()
        self.wfile.write(json.dumps(filtered_data).encode())

print(f"--- SERVER BIBLIOTECA ATTIVO SU PORTA {PORT} ---")
print("Risorse disponibili: authors, genres, books")
print("Premi Ctrl+C per interrompere")
with socketserver.TCPServer(("", PORT), BibliotecaHandler) as httpd:
    httpd.serve_forever()
