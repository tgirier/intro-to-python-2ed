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

    context = {
        'name': session.get('name', ''),
        "num_clicks_1": session.get('button_1', 0),
        "num_clicks_2": session.get('button_2', 0),
        "num_clicks_3": session.get('button_3', 0),
    }
    return render_template("index.html", **context)

@app.route("/reset")
def reset():
    session['name'] = ''
    return redirect(url_for('index'))

@app.route("/click/<btn_id>", methods=['POST'])
def click(btn_id):
    session[btn_id] = session.get(btn_id, 0) + 1
    return {'num_clicks': session[btn_id]}

if __name__ == '__main__':
    app.run(debug=True)