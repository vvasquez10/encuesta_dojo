from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'keep it secret'
datos = {}

@app.route('/', methods=['GET'])
def paginaInicial():    
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def procesaFormulario():    
    datos.update(request.form)
    session['name']=datos['name']
    session['locations']=datos['locations']
    session['languages']=datos['languages']
    session['comments']=datos['comments']

    print(session)

    return redirect ("/result")

@app.route('/result', methods=['GET'])
def exito():    
    if 'name' in session:
        session.clear()
        return render_template("success.html", datos = datos)
    else:
        return redirect ("/")    

@app.route('/back', methods=['GET'])
def backHome():
    session.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run(debug = True)