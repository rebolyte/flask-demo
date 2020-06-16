from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello world!'

@app.route('/<name>')
def hello_name(name):
	return render_template('show_name.html', name=name)

if __name__ == '__main__':
	app.run(port=5000)
