from flask import Flask
from flask import request

app= Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
	name = request.args.get('name',name) # the first name is key from dict
	return "hello from {}".format(name)

app.run(debug=True)