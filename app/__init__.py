from flask import Flask
import json

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

from app import routes

