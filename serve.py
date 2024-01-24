from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

seed = 100

@app.route('/', methods=["POST"])
def POST_num():
    return jsonify({'result': 'success'})

@app.route('/', methods=["GET"])
def GET_num():
    return "success", 200