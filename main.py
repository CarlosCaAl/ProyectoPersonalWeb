from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import forms

app = Flask(__name__,template_folder='plantillas')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def page3():
    formulario = forms.Formulario(request.form)
    if request.method == 'POST' and formulario.validate():
        print(formulario.username.data)
        print(formulario.email.data)
        print(formulario.comment.data)
    return render_template('page3.html',form=formulario)

@app.route('/page4')
def page4():
    error = request.args.get('error','error')
    if error == 'error': return render_template('page4.html')
    if error == 'error01': return render_template('page41.html')
    if error == 'error02': return render_template('page42.html')
    if error == 'error03': return render_template('page43.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/page6')
def page6():
    return render_template('page6.html')

app.run(debug=True,port=5000)