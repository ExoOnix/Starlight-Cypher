from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet

app = Flask(__name__)

key = b'j9NJrn_i3RRlmvYwl_feKi2R8PK-JNa8_Hykx9AHwAs='
fernet = Fernet(key)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/tostar', methods=['GET', 'POST'])
def tostar():
    if request.method == 'POST':
        main = request.form['main']
        res = str(fernet.encrypt(main.encode()))
        res = res[2:-1]
        return render_template('tostar.html', enc = res)


             
@app.route('/fromstar', methods=['GET', 'POST'])
def fromstar():
    if request.method == 'POST':
        main = str(request.form['main'])
        print(main)
        try:
            return render_template('fromstar.html', enc = fernet.decrypt(main).decode())
        except:
            return redirect(url_for('index'))

        
           


app.run(host='0.0.0.0', port=81)
