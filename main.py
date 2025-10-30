from flask import Flask, render_template
app =Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/empresa")
def empresa():
	return render_template("empresa.html")
@app.route("/contatos")
def contatos():
	return render_template("contatos.html")
app.run(debug=True, port=5001)