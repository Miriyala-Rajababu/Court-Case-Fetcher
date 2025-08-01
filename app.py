from flask import Flask, render_template, request
from scraper import fetch_case_data
from db import log_query, init_db

import random 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    year = request.form["year"]


    result, raw_html = fetch_case_data(case_type, case_number, year)
    log_query(case_type, case_number, year, raw_html)

    if result.get("error"):
        return render_template("index.html", error=result["error"])

    return render_template("index.html", result=result)



if __name__ == "__main__":
    init_db()
    app.run(debug=True)
