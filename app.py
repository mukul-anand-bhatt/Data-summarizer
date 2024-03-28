from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    subprocess.call(["python", "script.py"])
    return "Script executed successfully"

if __name__ == '__main__':
    app.run(debug=True)
