import subprocess
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'button1':
            termux_command = "flask run --port 2024 &"
            subprocess.Popen(termux_command, shell=True)
            pass
        elif action == 'button2':
            termux_command = "flask run --port 2025 &"
            subprocess.Popen(termux_command, shell=True)
            pass
        elif action == 'button3':
            termux_command = "fuser -k 2024/tcp"
            subprocess.Popen(termux_command, shell=True)
            pass
        elif action == 'button4':
            termux_command = "fuser -k 2025/tcp"
            subprocess.Popen(termux_command, shell=True)
            pass

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)