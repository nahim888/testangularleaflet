from flask import Flask, jsonify, render_template
import json
from flask_cors import CORS, cross_origin

import pandas as pd
import pymssql
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def dati():
    query = 'SELECT * FROM Stadio'
    df = pd.read_sql(query,conn)
    #json = df.to_json(orient = 'records')
    #print(json)
    return jsonify(list(df.to_dict('index').values()))

app.run()