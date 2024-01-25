from flask import Flask, render_template, request, jsonify
import os
import requests
import subprocess
import socket
import sys

app = Flask(__name__)

@app.route('/', methods=["POST"])
def POST_num():

    command = [sys.executable, "stress_cpu.py"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout, stderr = process.communicate()
    print(stdout, stderr)
    return jsonify({'result': 'success'})

@app.route('/', methods=["GET"])
def GET_num():
    name = socket.gethostname()
    return str(name), 200

