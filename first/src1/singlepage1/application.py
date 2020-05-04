from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texts = ["Essayez la dernière version de Visual Studio 2019 pour créer votre IDE idéal", 
         "générer des applications plus intelligentes, bénéficier d’une intégration au cloud", 
         "optimiser les performances et garder une longueur d’avance sur vos concurrents"]

@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]