from flask import Flask

app = Flask('GetSimple')


@app.route('/')
def home():
    return "Teste GetSimple."


app.run()
