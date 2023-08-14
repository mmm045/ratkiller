# Initialize Flask
from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
        if request.method == "GET":
                return render_template('index.html')
        else:
                return redirect("/winnywinny123")

@app.route("/winnywinny123")
def winny():
        return render_template('winner.html')
