from flask import Flask, request
import requests
import threading
import time
import json

class lavagem:
    def __init__(self,tanque):
        self.solucao=0
        self.tanque=tanque
    def get_solucao(self,solucao):
        self.trata_solucao(solucao)
    def trata_solucao(self,quantidade):
        self.solucao=quantidade*0.97
    def devolve_solucao(self):
        if self.tanque==3:
             x =  { "solucao": self.solucao}
             return x
        return self.solucao
app = Flask(__name__)
cont=0
data2={"solucao":0}
@app.route("/lavagem",methods=['GET'])
def Envia():
#    http://127.0.0.1:5000/  https:/test-flask-fei.herokuapp.com/secador
    global data2
    return json.dumps(data2)
@app.route("/lavagem",methods=['POST'])
def Recebe():
    data = request.get_json()
    tanque1=lavagem(1)
    tanque2=lavagem(2)
    tanque3=lavagem(3)
    #pega solucao de outro codigo e envia para trata_solucao ou outro tank
    tanque1.get_solucao(data['solucaolavagem'])
    tanque2.get_solucao(tanque1.devolve_solucao())
    tanque3.get_solucao(tanque2.devolve_solucao())
    global data2
    print(data2)
    data2 = tanque3.devolve_solucao()
    req = requests.post('https://test-flask-fei.herokuapp.com/secador', json = data2, headers = {"Content-Type": "application/json"})
    return data2
    
def create_app():
    global app
    return app
