from flask import (
    Flask,
    redirect, 
    render_template, 
    request, 
    session,
    url_for,
)

app = Flask(__name__)
app.secret_key = b'aetjlkf1146+-454:/6jdsljfe'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
    return render_template("index.html", 
                           name=session.get('name', ''),
                           num_clicks=session.get('num_clicks', 0))

@app.route("/reset")
def reset():
    session['name'] = ''
    return redirect(url_for('index'))

@app.route("/click")
def click():
    session['num_clicks'] = session.get('num_clicks', 0) + 1
    return {'num_clicks': session['num_clicks']}

if __name__ == '__main__':
    app.run(debug=True)