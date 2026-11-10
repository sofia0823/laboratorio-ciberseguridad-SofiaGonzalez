from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        estudiante = os.getenv("ESTUDIANTE_NOMBRE", "Sofia Gonzalez Herrera")

        html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servidor DMZ</title>
    <style>
        body {{ font-family: Arial; margin: 40px; background: #f4f4f9; }}
        .caja {{ background: white; padding: 25px; border-radius: 8px; }}
        h1 {{ color: #2c3e50; }}
        .ok {{ color: #27ae60; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="caja">
        <h1>✅ Servidor Web DMZ — EN LÍNEA</h1>
        <p><strong>Estudiante:</strong> {estudiante}</p>
        <p><strong>Estado:</strong> <span class="ok">Activo y funcionando</span></p>
        <hr>
        <p>Laboratorio de Ciberseguridad</p>
    </div>
</body>
</html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), CustomHandler)
    print(f"✅ Servidor en el puerto {puerto}")
    servidor.serve_forever()
