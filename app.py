from flask import Flask, render_template, request
import pymongo
from dotenv import load_dotenv, find_dotenv 
import os
load_dotenv(find_dotenv())

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



