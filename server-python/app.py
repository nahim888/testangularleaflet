from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

import json
app.config['JSON_SORT_KEYS'] = False

import pandas as pd
import numpy as np
import math
import pymssql
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')


@app.route('/')
def dati():
    query = "SELECT * FROM Stadio"
    df = pd.read_sql(query,conn)
    #return jsonify(list(df.to_dict('index').values()))
    #return df[df['AnnoApertura'].isnull()].to_html()
    return df.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)