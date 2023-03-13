from flask import Flask, redirect, render_template, request, url_for
from elaborazione_csv import ElaboraCSV
from github import Github

app = Flask(__name__)

elabora = ElaboraCSV()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dati')
def dati():
    csvfile = 'dati-temperature.csv'
    filename = elabora.ricava_percorso_assoluto(csvfile)
    lista_dati = elabora.analizza_dati(filename)
    return render_template('dati.html', lista_dati=lista_dati)

@app.route('/accesso', methods=["GET", "POST"])
def accesso():
    if request.method == "POST":
        token = request.form["token"]
        g = Github(token)
    return redirect(url_for('accesso'))

@app.route('/compiti')
def compiti():
    lista_compiti = []
    return render_template('compiti.html', lista_compiti=lista_compiti)

