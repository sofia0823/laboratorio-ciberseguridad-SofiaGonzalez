from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class CadenaHandler(BaseHTTPRequestHandler):
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
    <title>05 — Cadena de Suministro | Laboratorio de Ciberseguridad</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f0fdf4;
        }
        .cabecera {
            background: linear-gradient(90deg, #15803d, #22c55e);
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
            color: #15803d;
            border-bottom: 2px solid #bbf7d0;
            padding-bottom: 8px;
            margin: 30px 0 15px;
        }
        p { line-height: 1.7; margin-bottom: 15px; color: #334155; }
        ul { line-height: 1.8; margin-left: 25px; margin-bottom: 20px; color: #334155; }
        .esquema {
            background: #f0fdf4;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin: 25px 0;
        }
        .esquema span {
            display: inline-block;
            background: #dcfce7;
            padding: 8px 12px;
            margin: 5px;
            border-radius: 4px;
        }
        .ejemplos {
            display: grid;
            gap: 12px;
            margin: 20px 0;
        }
        .ejemplo {
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 15px;
            border-radius: 6px;
        }
        .proteccion {
            background: #eff6ff;
            border-left: 4px solid #3b82f6;
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
        <h1>📦 05 — Ataque a la Cadena de Suministro</h1>
        <p>Comprometer el flujo de software y servicios</p>
    </div>

    <div class="contenido">
        <h2>¿Qué es?</h2>
        <p>Un ataque a la <strong>cadena de suministro</strong> ocurre cuando un atacante compromete a un proveedor o componente intermediario. En lugar de atacar directamente a la víctima, corrompe algo que la víctima confía y usa. Cuando la víctima lo actualiza o lo instala, recibe también el ataque.</p>

        <div class="esquema">
            <span>Proveedor</span> ➜ <span>Software comprometido</span> ➜ <span>Distribución</span> ➜ <span>Víctima confiada</span> ➜ <span>⚠️ Comprometida</span>
        </div>

        <h2>¿Por qué es tan peligroso?</h2>
        <ul>
            <li><strong>Confianza abusada:</strong> El software viene de una fuente "legítima", así que las defensas lo dejan pasar</li>
            <li><strong>Alcance masivo:</strong> Un solo cambio malicioso puede afectar a miles o millones de usuarios</li>
            <li><strong>Detección tardía:</strong> El código malicioso puede permanecer oculto durante meses</li>
            <li><strong>Impacto profundo:</strong> Compromete no solo datos, sino el propio sistema de confianza</li>
        </ul>

        <h2>Ejemplos comunes</h2>
        <div class="ejemplos">
            <div class="ejemplo">
                <strong>📦 Librerías de código</strong><br>
                Paquetes maliciosos subidos a repositorios públicos o actualizaciones comprometidas de librerías populares.
            </div>
            <div class="ejemplo">
                <strong>🔧 Software de terceros</strong><br>
                Versiones modificadas de programas que una empresa descarga de su proveedor habitual.
            </div>
            <div class="ejemplo">
                <strong>🔌 Dispositivos físicos</strong><br>
                Equipos manipulados durante el envío o falsificaciones que se instalan en la red.
            </div>
        </div>

        <h2>¿Cómo protegerse?</h2>
        <div class="proteccion">
             Verificar la autenticidad y firma digital de cada actualización<br>
             Usar solo fuentes oficiales y conocidas para descargar software<br>
             Monitorear cambios inesperados en repositorios y dependencias<br>
             Mantener un inventario de todo lo que proviene de terceros<br>
             Revisar notas de versión: si algo cambia sin explicación, investigar
        </div>

        <h2>Concepto clave</h2>
        <p>La seguridad de tu sistema es tan fuerte como el eslabón más débil de tu cadena de confianza. No basta con asegurar tu propio código; también debes saber de dónde viene todo aquello que confías.</p>

        <a href="https://laboratorio-ciberseguridad-sofiagonzalez.onrender.com" class="volver">← Volver al Servidor DMZ</a>
    </div>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 80))
    servidor = HTTPServer(("0.0.0.0", puerto), CadenaHandler)
    servidor.serve_forever()
