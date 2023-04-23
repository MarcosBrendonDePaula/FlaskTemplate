import datetime
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, send_from_directory

# cria uma instância do Flask, especificando o nome do módulo atual (__name__) e a pasta de templates
app = Flask(__name__, template_folder='web/templates')

# importa o blueprint route_home do módulo HomeRoute e registra-o no aplicativo app
from routes.HomeRoute import route_home  
app.register_blueprint(route_home, url_prefix='/')

# registra as funções utilitárias now() e old() para serem usadas nos templates HTML
@app.context_processor
def utility_processor():
    def now():
        return datetime.now()
    def old(field_name):
        return request.form.get(field_name) if field_name in request.form else ''
    return dict(now=now, validation={}, error_bag={}, old=old)

# define uma rota para servir arquivos estáticos (como imagens, CSS e JavaScript) na pasta web/public
@app.route('/public/<path:filename>')
def public(filename):
    return send_from_directory('web/public', filename)

# inicia o servidor Flask em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)