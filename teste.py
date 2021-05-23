from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<variable>', method = '[ GET ]')
def index(variable = ''):
  return render_template("teste.html", html = variable)


if __name__ == '__main__':
  app.run()