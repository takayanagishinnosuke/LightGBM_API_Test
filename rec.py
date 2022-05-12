from crypt import methods
from distutils.log import error
from flask import Flask, jsonify, request, url_for
import json
from io import BytesIO
from flask_cors import CORS
import numpy as np
import pandas as pd
import os
from requests import head
import pickle


def model(data_set):
  x = pd.DataFrame(data_set)
  # x

  """モデル読み込み"""
  with open('lgbm_model.pkl', mode='rb') as f:
    clf = pickle.load(f)


  """推論"""
  ans = clf.predict(x)

  """ansが0.5以上は1にして返す"""
  predict = (ans >= 0.5).astype(int)

  pre = predict[0]
  print(pre)
  return int(pre) #intにしないとjsonで渡せない

  
