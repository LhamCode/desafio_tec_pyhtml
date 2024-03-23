from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos (inicialmente vazia)
produtos = []

# Rota para a página inicial (listagem de produtos)
@app.route('/')
def index():
    # Ordena os produtos por valor (do menor para o maior)
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('index.html', produtos=produtos_ordenados)

# Rota para o formulário de cadastro de produto
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        disponivel = request.form['disponivel'] == 'sim'

        # Cria um novo produto
        novo_produto = {
            'nome': nome,
            'descricao': descricao,
            'valor': valor,
            'disponivel': disponivel
        }

        # Adiciona o novo produto à lista
        produtos.append(novo_produto)

        # Redireciona para a página inicial (listagem)
        return redirect(url_for('index'))

    # Se o método for GET, exibe o formulário para cadastro
    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)

#Seu ambiente deve ter o Flask instalado#