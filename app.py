from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/trails')
def trails():
	trailjson = json.load(file('trails.geojson','rb'))
	trails = trailjson[u'features']
	return render_template('trails.html', trails=trails)

@app.route('/trail/<int:id>')
def trail(id):
	trailjson = json.load(file('trails.geojson','rb'))
	trail = trailjson[u'features'][id]
	return render_template('trail.html', trail=trail)



if __name__ == '__main__':
	app.run(debug=True)