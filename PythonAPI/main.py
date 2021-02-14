import Modules as m
from flask import Flask
from flask import request

app = Flask('GetSimple')


@app.route('/UltimoPreco/<ativo>')
def cotacao(ativo):
    return m.UltimoPreco(str(ativo))


app.run()
