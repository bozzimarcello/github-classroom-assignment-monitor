import os

class Edificio:

    def __init__(self,ID_edificio,Descrizione_edificio,ID_sensore,Tipo_misura,Nome_sito,Data_rilevazione,Valore_misura,Unita_misurazione):
        self.ID_edificio =ID_edificio
        self.Descrizione_edificio = Descrizione_edificio
        self.ID_sensore = ID_sensore
        self.Tipo_misura = Tipo_misura
        self.Nome_sito = Nome_sito
        self.Data_rilevazione = Data_rilevazione
        self.Valore_misura = Valore_misura
        self.Unita_misurazione = Unita_misurazione


class ElaboraCSV:

    def ricava_percorso_assoluto(self,csvfile):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        nome = os.path.join(THIS_FOLDER, csvfile)
        return nome

    def analizza_dati(self,filename):
        lista_dati = []
        myfile = open(filename,'r')
        for linea in myfile.read().splitlines():
            campi = linea.split(';')
            un_edificio = Edificio(campi[0].replace('"',''),campi[1].replace('"',''),campi[2].replace('"',''),campi[3].replace('"',''),campi[4].replace('"',''),campi[5].replace('"',''),campi[6].replace('"',''),campi[7].replace('"',''))
            lista_dati.append(un_edificio)
        myfile.close()
        return lista_dati