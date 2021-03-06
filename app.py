#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:12:19 2022

@author: prekshaparmar
"""

from flask import Flask 
from flask import request, render_template
import joblib

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])   # belong to Flask
def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_Regression")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI using Regression is: " + str(pred1)
        return(render_template("index.html", result1= str1))
    else:
        return(render_template("index.html", result1= "2"))

    
if __name__ == "__main__":
    app.run()
    
    
    
