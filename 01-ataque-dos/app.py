from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class AtaqueDoSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        estudiante = os.getenv("ESTUDIANTE", "Sofia Gonzalez Herrera")

        html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>01 — Ataque DoS | Laboratorio de Ciberseguridad</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            min-height: 100vh;
            padding: 2rem;
        }}
        .contenedor {{
            max-width: 850px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .cabecera {{
            background: linear-gradient(90deg, #dc2626, #ea580c);
            color: white;
            padding: 2rem;
        }}
        .cabecera h1 {{ font-size: 1.6rem; margin-bottom: 0.3rem; }}
        .cuerpo {{ padding: 2rem; }}
        .seccion {{ margin-bottom: 1.8rem; }}
        .seccion h2 {{
            font-size: 1.15rem;
            color: #dc2626;
            margin-bottom: 0.8rem;
            border-bottom: 2px solid #fecaca;
            padding-bottom: 0.3rem;
        }}
        .definicion {{
            background: #fef2f2;
            border-left: 4px solid #dc2626;
            padding: 1rem;
            border-radius: 0 8px 8px 0;
            margin-bottom: 1rem;
        }}
        .lista {{ padding-left: 1.5rem; line-height: 1.8; }}
        .tarjetas {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }}
        .tarjeta {{
            background: #f9fafb;
            padding: 1rem;
            border-radius: 10px;
            border-top: 3px solid #ea580c;
        }}
        .tarjeta h3 {{ font-size: 0.95rem; color: #92400e; margin-bottom: 0.5rem; }}
        .volver {{
            display: inline-block;
            margin-top: 1rem;
            padding: 0.7rem 1.2rem;
            background: #e5e7eb;
            color: #1f2937;
            text-decoration: none;
            border-radius: 8px;
        }}
        .volver:hover {{ background: #d1d5db; }}
        .pie {{
            background: #f9fafb;
            padding: 1rem 2rem;
            font-size: 0.85rem;
            color: #6b7280;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="contenedor">
        <div class="cabecera">
            <h1>⚠️ 01 — Ataque DoS</h1>
            <p style="opacity: 0.9;">Denegación de Servicio</p>
        </div>
        <div class="cuerpo">
            <div class="seccion">
                <h2>¿Qué es?</h2>
                <div class="definicion">
                    <p><strong>DoS (Denial of Service)</strong> es un ataque que busca impedir que usuarios legítimos accedan a un servicio, saturándolo con solicitudes hasta que el sistema se vuelve lento o deja de responder.</p>
                </div>
            </div>
            <div class="seccion">
                <h2>¿Cómo funciona?</h2>
                <ul class="lista">
                    <li>El atacante envía muchísimas peticiones al servidor</li>
                    <li>El servidor agota sus recursos: memoria, procesador, ancho de banda</li>
                    <li>Los usuarios reales no obtienen respuesta</li>
                    <li>En <strong>DDoS</strong> el ataque viene de muchas computadoras a la vez</li>
                </ul>
            </div>
            <div class="seccion">
                <h2>Tipos principales</h2>
                <div class="tarjetas">
                    <div class="tarjeta">
                        <h3>Volumen</h3>
                        <p>Inunda el servidor con tráfico masivo.</p>
                    </div>
                    <div class="tarjeta">
                        <h3>Protocolo</h3>
                        <p>Explota debilidades en la red.</p>
                    </div>
                    <div class="tarjeta">
                        <h3>Aplicación</h3>
                        <p>Ataca funciones del sitio web.</p>
                    </div>
                </div>
            </div>
            <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
        </div>
        <div class="pie">
            Estudiante: {estudiante} | Laboratorio de Ciberseguridad — 2026
        </div>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), AtaqueDoSHandler)
    servidor.serve_forever()

