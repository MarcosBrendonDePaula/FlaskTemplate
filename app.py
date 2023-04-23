import datetime
from dotenv import load_dotenv
load_dotenv()


from flask import Flask, request, send_from_directory, render_template


app = Flask(__name__,template_folder='web/templates')

from routes.HomeRoute import route_home
app.register_blueprint(route_home, url_prefix='/')

@app.context_processor
def utility_processor():
    def now():
        return datetime.now()
    def old(field_name):
        return request.form.get(field_name) if field_name in request.form else ''
    return dict(now=now, validation={}, error_bag={}, old=old)

@app.route('/public/<path:filename>')
def public(filename):
    return send_from_directory('web/public', filename)

if __name__ == '__main__':
    app.run(debug=True)