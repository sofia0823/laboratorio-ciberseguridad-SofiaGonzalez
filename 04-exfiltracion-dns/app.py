from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class DNSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>04 — Exfiltración DNS | Laboratorio de Ciberseguridad</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #eef2ff;
        }
        .cabecera {
            background: linear-gradient(90deg, #4338ca, #6366f1);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .cabecera h1 { font-size: 1.6rem; margin-bottom: 5px; }
        .contenido {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }
        h2 {
            color: #4338ca;
            border-bottom: 2px solid #c7d2fe;
            padding-bottom: 8px;
            margin: 30px 0 15px;
        }
        p { line-height: 1.7; margin-bottom: 15px; color: #334155; }
        ul { line-height: 1.8; margin-left: 25px; margin-bottom: 20px; color: #334155; }
        .pasos {
            background: #eef2ff;
            border-left: 4px solid #6366f1;
            padding: 20px;
            border-radius: 6px;
            margin: 20px 0;
        }
        .riesgo {
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
        .defensa {
            background: #f0fdf4;
            border-left: 4px solid #22c55e;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
        .volver {
            display: inline-block;
            margin-top: 25px;
            padding: 10px 22px;
            background: #e5e7eb;
            color: #1f2937;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
        }
        .volver:hover { background: #d1d5db; }
    </style>
</head>
<body>
    <div class="cabecera">
        <h1>📡 04 — Exfiltración por DNS</h1>
        <p>Filtrado de datos a través del sistema de nombres de dominio</p>
    </div>

    <div class="contenido">
        <h2>¿Qué es?</h2>
        <p>La <strong>exfiltración DNS</strong> es una técnica donde datos confidenciales salen de una red protegida ocultándolos dentro de consultas al sistema de nombres de dominio. Como el DNS suele permitirse en las reglas de firewall, muchos sistemas no detectan que hay información robada viaja por ahí.</p>

        <h2>¿Cómo funciona?</h2>
        <div class="pasos">
            <strong>El proceso en 4 pasos:</strong><br><br>
            1. El atacante compromete un equipo dentro de la red interna<br>
            2. Divide los datos robados en fragmentos pequeños<br>
            3. Codifica cada fragmento como parte de un nombre de dominio<br>
            4. Envía consultas DNS a un servidor controlado por el atacante, que reconstruye la información
        </div>

        <h2>¿Por qué es peligroso?</h2>
        <div class="riesgo">
            ⚠️ <strong>Difícil detección:</strong> El tráfico DNS se considera normal y rara vez se inspecciona en profundidad.<br><br>
            ⚠️ <strong>Salida silenciosa:</strong> No abre conexiones nuevas ni visibles hacia afuera.<br><br>
            ⚠️ <strong>Tamaño pequeño:</strong> Sirve para robar contraseñas, tokens o archivos pequeños rápidamente.
        </div>

        <h2>¿Cómo prevenirlo?</h2>
        <div class="defensa">
            ✅ Monitorear y registrar todo el tráfico DNS saliente<br>
            ✅ Bloquear consultas a dominios desconocidos o sospechosos<br>
            ✅ Usar servidores DNS internos con reglas estrictas<br>
            ✅ Limitar qué equipos pueden hacer consultas DNS externas<br>
            ✅ Analizar patrones inusuales en las respuestas DNS
        </div>

        <h2>Concepto clave</h2>
        <p>El DNS fue diseñado para traducir nombres a direcciones IP, no para transportar datos. Cuando se observan consultas con cadenas largas y aleatorias, podría ser señal de actividad maliciosa.</p>

        <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), DNSHandler)
    servidor.serve_forever()
