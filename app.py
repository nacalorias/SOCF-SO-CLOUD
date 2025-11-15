from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(__name__)

def xget_system_info():
    xprocess = psutil.Process(os.getpid())
    xmemory_mb = xprocess.memory_info().rss / (1024 * 1024)
    xcpu_percent = xprocess.cpu_percent(interval=0.1)
    
    xos_info = f"{platform.system()} ({platform.release()})"
    if platform.system() == "Linux":
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith('PRETTY_NAME'):
                        xos_info = line.split('=')[1].strip().strip('"')
                        break
        except:
            pass
    
    return {
        "nome": "Ana Carolina Afonso Meiado, Ana Carolina Curi de Sales",
        "pid": os.getpid(),
        "memoria_mb": round(xmemory_mb, 2),
        "cpu_percent": round(xcpu_percent, 2),
        "sistema_operacional": xos_info
    }

@app.route('/')
def xindex():
    xinfo = xget_system_info()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Projeto SO Cloud</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
                border-bottom: 3px solid #4CAF50;
                padding-bottom: 10px;
            }}
            .info {{
                margin: 20px 0;
                line-height: 2;
                font-size: 16px;
            }}
            .label {{
                font-weight: bold;
                color: #555;
            }}
            .value {{
                color: #2196F3;
            }}
            .links {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
            }}
            a {{
                color: #4CAF50;
                text-decoration: none;
                margin-right: 20px;
                font-weight: bold;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Projeto SO Cloud - Métricas do Sistema</h1>
            <div class="info">
                <p><span class="label">Nome:</span> <span class="value">{xinfo['nome']}</span></p>
                <p><span class="label">PID:</span> <span class="value">{xinfo['pid']}</span></p>
                <p><span class="label">Memória usada:</span> <span class="value">{xinfo['memoria_mb']} MB</span></p>
                <p><span class="label">CVP:</span> <span class="value">{xinfo['cpu_percent']}%</span></p>
                <p><span class="label">Sistema Operacional:</span> <span class="value">{xinfo['sistema_operacional']}</span></p>
            </div>
            <div class="links">
                <a href="/info">Ver /info (JSON)</a>
                <a href="/metricas">Ver /metricas (JSON)</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/info')
def xinfo_route():
    return jsonify({
        "nome": "Ana Carolina Afonso Meiado, Ana Carolina Curi de Sales"
    })

@app.route('/metricas')
def xmetricas():
    xinfo = xget_system_info()
    return jsonify({
        "pid": xinfo['pid'],
        "memoria_mb": xinfo['memoria_mb'],
        "cpu_percent": xinfo['cpu_percent'],
        "sistema_operacional": xinfo['sistema_operacional']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

APP = xapp
