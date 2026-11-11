from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class FuerzaBrutaHandler(BaseHTTPRequestHandler):
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
    <title>03 — Fuerza Bruta | Laboratorio de Ciberseguridad</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #fef3c7;
        }
        .cabecera {
            background: linear-gradient(90deg, #b45309, #f59e0b);
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
            color: #b45309;
            border-bottom: 2px solid #fde68a;
            padding-bottom: 8px;
            margin: 30px 0 15px;
        }
        p { line-height: 1.7; margin-bottom: 15px; color: #334155; }
        ul { line-height: 1.8; margin-left: 25px; margin-bottom: 20px; color: #334155; }
        .metodos {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .metodo {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            border-radius: 6px;
        }
        .metodo h3 { font-size: 1rem; color: #92400e; margin-bottom: 8px; }
        .peligro {
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
        .buenas {
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
        <h1>🔑 03 — Ataque de Fuerza Bruta</h1>
        <p>Intento sistemático de adivinar credenciales</p>
    </div>

    <div class="contenido">
        <h2>¿Qué es?</h2>
        <p>El ataque de <strong>fuerza bruta</strong> es una técnica donde se prueban sistemáticamente todas las combinaciones posibles de contraseñas o claves hasta encontrar la correcta. Funciona como intentar abrir un candado probando número por número.</p>

        <h2>¿Cómo funciona?</h2>
        <p>El atacante utiliza un programa automatizado que genera miles o millones de combinaciones. Mientras más larga y compleja sea la contraseña, más tiempo le tomará al atacante descifrarla.</p>

        <h2>Formas de realizarlo</h2>
        <div class="metodos">
            <div class="metodo">
                <h3>🔡 Ataque completo</h3>
                <p>Prueba todas las combinaciones posibles de letras, números y símbolos. Es lento pero garantiza encontrar la solución.</p>
            </div>
            <div class="metodo">
                <h3>📋 Ataque de diccionario</h3>
                <p>Usa listas de palabras comunes, contraseñas filtradas y combinaciones probables. Es mucho más rápido y efectivo contra contraseñas débiles.</p>
            </div>
            <div class="metodo">
                <h3>🔁 Variaciones</h3>
                <p>Modifica palabras del diccionario cambiando letras por números o agregando símbolos (ej: "c0ntr4s3ñ4").</p>
            </div>
        </div>

        <div class="peligro">
            ⚠️ <strong>Riesgo:</strong> Este ataque funciona mejor contra contraseñas cortas, comunes o relacionadas con información personal. Una contraseña de 4 caracteres se descifra en minutos; una de 12 caracteres complejos puede tomar millones de años.
        </div>

        <h2>¿Cómo protegerse?</h2>
        <div class="buenas">
            ✅ <strong>Contraseñas largas:</strong> mínimo 12 caracteres<br>
            ✅ <strong>Combinar tipos:</strong> mayúsculas, minúsculas, números y símbolos<br>
            ✅ <strong>Autenticación en dos pasos (2FA):</strong> incluso si adivinan la contraseña, no pueden entrar<br>
            ✅ <strong>Límite de intentos:</strong> bloquear la cuenta tras varios fallos<br>
            ✅ <strong>No reutilizar contraseñas:</strong> una por cada servicio importante
        </div>

        <h2>Concepto clave</h2>
        <p>La seguridad de este ataque depende enteramente de la <strong>fortaleza de tu contraseña</strong>. No hay sistema invencible, pero una buena contraseña hace que el ataque sea tan costoso en tiempo y recursos que el atacante se rinda antes de lograrlo.</p>

        <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), FuerzaBrutaHandler)
    servidor.serve_forever()
