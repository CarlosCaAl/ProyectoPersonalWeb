from wtforms import Form
from wtforms import StringField

class Formulario(Form):
    username = StringField('Username')
    email = StringField('Correo')
    comment = StringField('Comentario')