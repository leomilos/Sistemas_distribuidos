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
             return json.dumps(x)
        return self.solucao
app = Flask(__name__)
cont=0

r = requests.get('https://cc7261-app-modulo-decantador.herokuapp.com/')
print(r.text)
tanque1=lavagem(1)
tanque2=lavagem(2)
tanque3=lavagem(3)
data = json.loads(r.text)
print(data)
tanque1.get_solucao(data['decantador']['solucaolavagem'])
tanque2.get_solucao(tanque1.devolve_solucao())
tanque3.get_solucao(tanque2.devolve_solucao())
data2 = tanque3.devolve_solucao()
print(data2)
post = requests.post("https://test-flask-fei.herokuapp.com/secador")
print(data2)