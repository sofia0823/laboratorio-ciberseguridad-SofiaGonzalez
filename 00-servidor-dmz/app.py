from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        estudiante = os.getenv("ESTUDIANTE_NOMBRE", "Sofia Gonzalez Herrera")

        html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servidor Web DMZ</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }}
        .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; }}
        .status {{ color: #27ae60; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Servidor Objetivo DMZ</h1>
        <p>Estado del servicio: <span class="status">✅ EN LÍNEA / ACTIVO</span></p>
        <hr>
        <p><strong>Laboratorio de Ciberseguridad</strong></p>
        <p>Estudiante: {estudiante}</p>
    </div>
</body>
</html>
        """
        self.wfile.write(html_content.encode("utf-8"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 80))
    server = HTTPServer(("0.0.0.0", port), CustomHandler)
    print(f"Servidor corriendo en el puerto {port}")
    server.serve_forever()
