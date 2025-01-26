### Building URL dynamically 
### variable rule 
### jinja2 template engin 


### jinja2 template engin
"""
there are multiple way specifically to read the data souce from t
the back end in the HTML page 
first way is 
{{variable_name}} experssion to print output in html 

second way is 
{% %} for loop and if else condition(basically for the conditional statement, for loop etc)

third way is 
{#______#} for the comment
"""
from flask import Flask, render_template,request,url_for,redirect

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


"""@app.route('/submit', methods=['Get','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"<h1>Hello {name}</h1>"
    return render_template('form.html')
"""
# variable rule 
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score > 50 : 
        res = "pass"
    else:
        res = "fail"
    return render_template('result.html',result = res)
# think to remember 
"""if we take int as a input like 
def success(int : score)
type to print  it like return score but if type return str(score)
it will work fine
"""
@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score > 50 : 
        res = "pass"
    else:
        res = "fail"

    exp = {'score' : score , "res" : res}
    return render_template('result2.html',result = exp)

@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
        Math = float(request.form['Math'])
        logic = float(request.form['logic'])
        programming = float(request.form['programming'])
        Data_science = float(request.form['Data_science'])
        total_score = (Math + logic + programming + Data_science)/4
    else:
        return render_template('submit.html')
    return redirect(url_for('successres',score = total_score))


@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result3.html',result = score)

if __name__ == "__main__":
    app.run(debug=True)