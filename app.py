from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello():
  return "<p>Teste de Olá Mundo...</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
