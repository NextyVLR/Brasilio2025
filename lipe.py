from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def bem_vindo():
    return 'Bem-Vindo! Servidor rodando'

if __name__ == '__main__':
    app.run(debug=True)