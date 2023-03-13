from flask import Flask, render_template
from elaborazione_csv import ElaboraCSV

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
