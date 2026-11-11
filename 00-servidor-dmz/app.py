from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class ServidorDMZ(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        estudiante = os.getenv("ESTUDIANTE", "Sofia Gonzalez Herrera")
        proyecto = os.getenv("PROYECTO", "Laboratorio de Ciberseguridad")

        html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidor DMZ — {proyecto}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            padding: 2rem;
            color: #333;
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
            background: linear-gradient(90deg, #10b981, #059669);
            color: white;
            padding: 2rem;
        }}
        .cabecera h1 {{
            font-size: 1.8rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .cuerpo {{
            padding: 2rem;
        }}
        .seccion {{
            margin-bottom: 1.5rem;
        }}
        .seccion h2 {{
            font-size: 1.1rem;
            color: #0f2027;
            margin-bottom: 0.5rem;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 0.3rem;
        }}
        .dato {{
            padding: 0.5rem 0;
        }}
        .etiqueta {{
            font-weight: bold;
            display: inline-block;
            min-width: 140px;
            color: #4b5563;
        }}
        .valor {{
            color: #1f2937;
        }}
        .activo {{
            color: #059669;
            font-weight: bold;
        }}
        .enlaces {{
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #e5e7eb;
        }}
        .enlaces a {{
            display: inline-block;
            padding: 0.6rem 1rem;
            margin: 0.3rem;
            background: #f3f4f6;
            color: #1f2937;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.2s;
        }}
        .enlaces a:hover {{
            background: #e5e7eb;
            transform: translateY(-2px);
        }}
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
            <h1>✅ Servidor DMZ — EN LÍNEA</h1>
            <p style="margin-top: 0.5rem; opacity: 0.9;">Punto central del laboratorio de ciberseguridad</p>
        </div>
        <div class="cuerpo">
            <div class="seccion">
                <h2>Información del Proyecto</h2>
                <div class="dato"><span class="etiqueta">Estudiante:</span> <span class="valor">{estudiante}</span></div>
                <div class="dato"><span class="etiqueta">Proyecto:</span> <span class="valor">{proyecto}</span></div>
                <div class="dato"><span class="etiqueta">Componente:</span> <span class="valor">Servidor DMZ</span></div>
                <div class="dato">
                    <span class="etiqueta">Estado:</span>
                    <span class="valor activo">● Activo y funcionando</span>
                </div>
            </div>

            <div class="seccion">
                <h2>Descripción</h2>
                <p style="line-height: 1.6;">
                    Esta zona desmilitarizada (DMZ) actúa como punto de acceso central y monitoreo 
                    del laboratorio. Aquí se registran y conectan los diferentes escenarios 
                    prácticos de seguridad implementados.
                </p>
            </div>

            <div class="seccion enlaces">
                <h2>Escenarios del Laboratorio</h2>
                <p style="margin-bottom: 0.8rem; color: #6b7280;">Próximamente disponibles:</p>
                <a href="#">01 — Ataque DoS<<a href="https://lab-ataque-dos-sofia.onrender.com" target="_blank" style="display:inline-block; padding:10px 16px; background:#fef2f2; color:#dc2626; border:1px solid #fecaca; border-radius:8px; text-decoration:none; font-weight:500; margin:5px;">01 — Ataque DoS</a>
>
                <a href="#">02 — Escaneo de Puertos<<a href="https://lab-puertos-sofia.onrender.com" target="_blank" style="display:inline-block; padding:10px 16px; background:#eff6ff; color:#1e40af; border:1px solid #bfdbfe; border-radius:8px; text-decoration:none; font-weight:500; margin:5px;">02 — Escaneo de Puertos</a>
>
                <a href="#">03 — Fuerza Bruta<<a href="https://lab-fuerza-bruta.onrender.com" target="_blank" style="display:inline-block; padding:10px 16px; background:#fffbeb; color:#b45309; border:1px solid #fde68a; border-radius:8px; text-decoration:none; font-weight:500; margin:5px;">03 — Fuerza Bruta</a>
>
                <a href="#">04 — Exfiltración DNS<<a href="" target="_blank" style="display:inline-block; padding:10px 16px; background:#eef2ff; color:#4338ca; border:1px solid #c7d2fe; border-radius:8px; text-decoration:none; font-weight:500; margin:5px;">04 — Exfiltración DNS</a>
>
                <a href="#">05 — Cadena de Suministro</a>
                <a href="#">06 — Credential Stuffing</a>
                <a href="#">07 — Proxy MITM</a>
            </div>
        </div>
        <div class="pie">
            Laboratorio de Ciberseguridad — Desplegado en Render — 2026
        </div>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), ServidorDMZ)
    print(f"✅ Servidor DMZ activo en el puerto {puerto}")
    servidor.serve_forever()
