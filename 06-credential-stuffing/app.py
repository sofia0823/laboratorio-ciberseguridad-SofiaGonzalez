from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class CredentialHandler(BaseHTTPRequestHandler):
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
    <title>06 — Credential Stuffing | Laboratorio de Ciberseguridad</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #fdf2f8;
        }
        .cabecera {
            background: linear-gradient(90deg, #be185d, #ec4899);
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
            color: #be185d;
            border-bottom: 2px solid #fbcfe8;
            padding-bottom: 8px;
            margin: 30px 0 15px;
        }
        p { line-height: 1.7; margin-bottom: 15px; color: #334155; }
        ul { line-height: 1.8; margin-left: 25px; margin-bottom: 20px; color: #334155; }
        .diferencia {
            background: #fdf2f8;
            border-left: 4px solid #ec4899;
            padding: 20px;
            border-radius: 6px;
            margin: 20px 0;
        }
        .porque {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
        .proteccion {
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
        <h1>🔐 06 — Credential Stuffing</h1>
        <p>Uso de credenciales filtradas en otros servicios</p>
    </div>

    <div class="contenido">
        <h2>¿Qué es?</h2>
        <p>El <strong>Credential Stuffing</strong> es un ataque donde el atacante toma pares de correo y contraseña filtrados de una brecha de seguridad y los prueba en otros servicios. Se basa en que muchas personas <strong>reutilizan la misma contraseña</strong> en múltiples cuentas.</p>

        <div class="diferencia">
            <strong>⚠️ No es lo mismo que Fuerza Bruta</strong><br><br>
            • <strong>Fuerza Bruta:</strong> prueba TODAS las combinaciones posibles desde cero<br>
            • <strong>Credential Stuffing:</strong> usa SOLO credenciales que ya existen y fueron filtradas en otra brecha
        </div>

        <h2>¿Cómo funciona?</h2>
        <ol style="line-height:1.8; margin-left:25px; margin-bottom:20px; color:#334155;">
            <li>Un sitio web sufre una brecha y miles de correos + contraseñas quedan expuestos en internet</li>
            <li>El atacante descarga esa lista</li>
            <li>Usa programas automáticos para probar esas mismas credenciales en otros servicios (redes sociales, bancos, correos)</li>
            <li>Si funcionan → ¡acceso concedido!</li>
        </ol>

        <div class="porque">
            <strong>¿Por qué funciona tan bien?</strong><br>
            Porque el hábito de reutilizar contraseñas sigue siendo muy común. Si usas tu correo + misma contraseña en 10 sitios, basta con que UNO sea vulnerado para que todos los demás queden expuestos.
        </div>

        <h2>¿Cómo protegerse?</h2>
        <div class="proteccion">
             <strong>Nunca reutilices contraseñas:</strong> una cuenta = una contraseña única<br>
             <strong>Usa un gestor de contraseñas:</strong> crea y guarda claves distintas por ti mismo<br>
             <strong>Activa 2FA:</strong> autenticación en dos pasos bloquea el acceso aunque roben tu contraseña<br>
             <strong>Verifica si tus datos han sido filtrados:</strong> sitios como "Have I Been Pwned" te avisan si tu correo aparece en brechas públicas<br>
             <strong>Cambia contraseñas</strong> de inmediato si alguno de tus servicios anuncia una brecha de seguridad
        </div>

        <h2>Concepto clave</h2>
        <p>Tu contraseña es como la llave de tu casa: no le pongas la misma cerradura a tu coche, tu oficina y tu caja fuerte. Si una cae, caen todas.</p>

        <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), CredentialHandler)
    servidor.serve_forever()
