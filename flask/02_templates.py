# N'oubliez pas d'importer render_template
from flask import Flask, render_template
app = Flask("Templates")


@app.route("/")
def hello():
    return "Hello World!"


app.run(debug=True)