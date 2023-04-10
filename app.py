from dotenv import load_dotenv
load_dotenv()

from flask import Flask, send_from_directory, render_template


app = Flask(__name__,template_folder='web/templates')

@app.route('/public/<path:filename>')
def public(filename):
    return send_from_directory('web/public', filename)

@app.route("/")
def hello_world():
    return render_template("teste.html")

if __name__ == '__main__':
    app.run(debug=True)