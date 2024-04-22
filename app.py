from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Analista de Dados',
    'localidade': 'Rio de Janeiro',
    'salario': 'R$ 3.500,00'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Python',
    'localidade': 'São Paulo',
    'salario': 'R$ 4.500,00'
}, {
    'id': 3,
    'titulo': 'Desenvolvedor Web',
    'localidade': 'Salvador',
    'salario': 'R$ 5.500,00'
}, {
    'id': 4,
    'titulo': 'Gerente de Projetos',
    'localidade': 'Fortaleza',
    'salario': 'R$ 6.500,00'
}, {
    'id': 5,
    'titulo': 'Analista de Marketing',
    'localidade': 'Belo Horizonte',
    'salario': 'R$ 7.500,00'
}, {
    'id': 6,
    'titulo': 'Analista de Suporte',
    'localidade': 'Curitiba',
    'salario': 'R$ 8.500,00'
}, {
    'id': 7,
    'titulo': 'Analista de Vendas',
    'localidade': 'Recife',
    'salario': 'R$ 9.500,00'
}, {
    'id': 8,
    'titulo': 'Analista de Marketing',
    'localidade': 'Belo Horizonte',
    'salario': 'R$ 10.500,00'
}, {
    'id': 9,
    'titulo': 'Analista de Suporte',
    'localidade': 'Curitiba',
    'salario': 'R$ 11.500,00'
}, {
    'id': 10,
    'titulo': 'Analista de Vendas',
    'localidade': 'Recife',
    'salario': 'R$ 12.500,00'
}]


@app.route('/')
def hello():
  return render_template("home.html", vagas=VAGAS)


@app.route("/vagas")
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
