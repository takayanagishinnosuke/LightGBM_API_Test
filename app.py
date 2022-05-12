from crypt import methods
from distutils.log import error
from flask import Flask, jsonify, request, url_for
import json
from io import BytesIO
from flask_cors import CORS
import numpy as np
import rec




app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app)

@app.route('/', methods=("GET", 'POST'))
def test():
  if request.method == 'POST':
    j = request.get_json()
    A = int(j['A'])
    B = int(j['B'])
    C = int(j['C'])
    D = int(j['D'])
    E = int(j['E'])
    F = int(j['F'])
    G = int(j['G'])
    H = int(j['H'])
    I = int(j['I'])
    J = int(j['J'])
    K = int(j['K'])
    
    data = [[A,B,C,D,E,F,G,H,I,J,K]]

    ans = rec.model(data)

    return jsonify({"result": ans}) 

  else:
    return jsonify({"result": "POST失敗 エラー"})


if __name__ == "__main__":
    app.run(port=5000)
