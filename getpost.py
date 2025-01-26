from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['Get','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"<h1>Hello {name}</h1>"
    return render_template('form.html')

@app.route('/submit', methods=['Get','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"<h1>Hello {name}</h1>"
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)