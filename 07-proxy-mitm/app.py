from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class MITMHandler(BaseHTTPRequestHandler):
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
    <title>07 — Proxy MITM | Laboratorio de Ciberseguridad</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #fefce8;
        }
        .cabecera {
            background: linear-gradient(90deg, #854d0e, #d97706);
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
            color: #854d0e;
            border-bottom: 2px solid #fde68a;
            padding-bottom: 8px;
            margin: 30px 0 15px;
        }
        p { line-height: 1.7; margin-bottom: 15px; color: #334155; }
        ul { line-height: 1.8; margin-left: 25px; margin-bottom: 20px; color: #334155; }
        .flujo {
            background: #fef3c7;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin: 25px 0;
        }
        .flujo span {
            display: inline-block;
            background: #fde68a;
            padding: 10px 14px;
            margin: 5px;
            border-radius: 4px;
        }
        .tecnicas {
            display: grid;
            gap: 12px;
            margin: 20px 0;
        }
        .tec {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            border-radius: 6px;
        }
        .peligro {
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
        <h1>🔄 07 — Proxy y Hombre en el Medio (MITM)</h1>
        <p>Intercepción y modificación de comunicaciones</p>
    </div>

    <div class="contenido">
        <h2>¿Qué es?</h2>
        <p>Un ataque de <strong>Hombre en el Medio (MITM)</strong> ocurre cuando un atacante se coloca secretamente entre dos partes que se comunican. Puede escuchar, leer e incluso modificar los mensajes que pasan de uno a otro, sin que las víctimas sepan que hay alguien más escuchando.</p>

        <div class="flujo">
            <span>Tu dispositivo</span> ➜ <span>⚠️ Atacante</span> ➜ <span>Servidor de destino</span><br>
            <small>El atacante intercepta todo lo que viaja en ambas direcciones</small>
        </div>

        <h2>¿Cómo funciona?</h2>
        <p>El atacante se posiciona como intermediario. Tu crees que hablas directamente con el servidor, pero en realidad hablas con él, y él reenvía tus mensajes al servidor real. Lo mismo hace con las respuestas: las recibe del servidor, puede leerlas o cambiarlas, y luego te las envía como si nada hubiera pasado.</p>

        <h2>Técnicas comunes</h2>
        <div class="tecnicas">
            <div class="tec">
                <strong>📶 Wi-Fi maliciosa</strong><br>
                Puntos de acceso abiertos en lugares públicos que parecen legítimos pero son controlados por el atacante. Todo tu tráfico pasa por él.
            </div>
            <div class="tec">
                <strong>🔀 Envenenamiento ARP</strong><br>
                Engaña a la red local para que todo el tráfico de los equipos pase por la máquina del atacante en lugar de ir directamente al router.
            </div>
            <div class="tec">
                <strong>🌐 Suplantación DNS</strong><br>
                Redirige a los usuarios a sitios falsos donde el atacante puede interceptar credenciales y datos.
            </div>
        </div>

        <div class="peligro">
            ⚠️ <strong>¿Qué puede hacer el atacante?</strong><br>
            • Leer contraseñas, mensajes y datos privados<br>
            • Modificar información en tránsito<br>
            • Secuestrar sesiones activas<br>
            • Redirigirte a sitios falsos sin que te des cuenta
        </div>

        <h2>¿Cómo protegerse?</h2>
        <div class="defensa">
             <strong>Usa solo HTTPS:</strong> el candado en la barra de direcciones significa que la comunicación está cifrada<br>
             <strong>Evita Wi-Fi públicas</strong> para transacciones importantes sin usar VPN<br>
             <strong>Verifica siempre el candado</strong> y el nombre del sitio web<br>
             <strong>Usa redes privadas virtuales (VPN)</strong> en redes que no confíes<br>
             No desactives las advertencias de seguridad de tu navegador
        </div>

        <h2>Concepto clave</h2>
        <p>El cifrado convierte lo que el atacante puede ver en algo que no puede entender. Incluso si intercepta el tráfico, si está cifrado correctamente, solo verá texto sin sentido. Por eso el HTTPS es tan importante: no solo protege el destino, sino el viaje de tus datos.</p>

        <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), MITMHandler)
    servidor.serve_forever()

