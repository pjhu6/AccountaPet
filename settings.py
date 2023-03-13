from flask import Flask, request, redirect, render_template, session
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
app.secret_key = 'settings_secret_key'
CORS(app, resources={r"/*": {"origins": ["http://localhost"]}})

@app.route('/settings', methods=['POST'])
def handle_setting_request():
    action = request.form['action']
    if action == 'logout':
        return redirect('http://127.0.0.1:5000/')


if __name__ == '__main__':
    app.run(port=5003)