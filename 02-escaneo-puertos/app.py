from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class EscaneoHandler(BaseHTTPRequestHandler):
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
    <title>02 — Escaneo de Puertos | Laboratorio de Ciberseguridad</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f0f4f8;
        }
        .cabecera {
            background: linear-gradient(90deg, #1e40af, #3b82f6);
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
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        h2 {
            color: #1e40af;
            border-bottom: 2px solid #bfdbfe;
            padding-bottom: 8px;
            margin: 30px 0 15px;
        }
        p { line-height: 1.7; margin-bottom: 15px; color: #334155; }
        ul { line-height: 1.8; margin-left: 25px; margin-bottom: 20px; color: #334155; }
        .puertos {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin: 20px 0;
        }
        .puerto {
            background: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 15px;
            border-radius: 6px;
        }
        .puerto strong { color: #1e40af; font-size: 1.1rem; }
        .volver {
            display: inline-block;
            margin-top: 25px;
            padding: 10px 22px;
            background: #e2e8f0;
            color: #1e293b;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            transition: background 0.2s;
        }
        .volver:hover { background: #cbd5e1; }
        .advertencia {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="cabecera">
        <h1>🔌 02 — Escaneo de Puertos</h1>
        <p>Identificación de servicios abiertos en un sistema</p>
    </div>

    <div class="contenido">
        <h2>¿Qué es un puerto?</h2>
        <p>Un <strong>puerto</strong> es un punto final de comunicación que permite a dispositivos y aplicaciones intercambiar información en una red. Funciona como una "puerta" por donde entran y salen los datos.</p>
        
        <h2>¿Qué es el escaneo de puertos?</h2>
        <p>Es una técnica que consiste en enviar solicitudes a un rango de puertos de un sistema para identificar cuáles están abiertos y qué servicios están escuchando en ellos.</p>
        
        <div class="advertencia">
            ⚠️ <strong>Nota:</strong> El escaneo de puertos sin autorización puede ser ilegal. Este contenido es exclusivamente educativo para entender cómo funcionan las defensas de red.
        </div>
        
        <h2>Puertos más comunes</h2>
        <div class="puertos">
            <div class="puerto"><strong>21</strong><br>FTP — Transferencia de archivos</div>
            <div class="puerto"><strong>22</strong><br>SSH — Acceso remoto seguro</div>
            <div class="puerto"><strong>23</strong><br>Telnet — Acceso remoto sin cifrar</div>
            <div class="puerto"><strong>25</strong><br>SMTP — Envío de correo</div>
            <div class="puerto"><strong>53</strong><br>DNS — Resolución de nombres</div>
            <div class="puerto"><strong>80</strong><br>HTTP — Páginas web</div>
            <div class="puerto"><strong>110</strong><br>POP3 — Recepción de correo</div>
            <div class="puerto"><strong>143</strong><br>IMAP — Correo entrante</div>
            <div class="puerto"><strong>443</strong><br>HTTPS — Web segura</div>
            <div class="puerto"><strong>3389</strong><br>RDP — Escritorio remoto</div>
        </div>
        
        <h2>¿Para qué se utiliza?</h2>
        <ul>
            <li><strong>Administradores:</strong> para verificar la seguridad de sus sistemas y cerrar puertos innecesarios</li>
            <li><strong>Atacantes:</strong> para descubrir servicios vulnerables y planear ataques</li>
        </ul>
        
        <h2>Medidas de protección</h2>
        <ul>
            <li>Utilizar un firewall para cerrar puertos que no se utilicen</li>
            <li>Desactivar servicios que no sean necesarios</li>
            <li>Configurar el firewall para que no responda a escaneos</li>
            <li>Monitorear el tráfico de red en busca de escaneos</li>
        </ul>
        
        <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), EscaneoHandler)
    servidor.serve_forever()
