from flask import Flask 

app= Flask(__name__)

@app.route('/')

def index():
    return 'Hola mundo'

@app.route('/alumnos')

def get_alumnos():
    return 'Retornando todos los alumnos'

if __name__=='__main__':
    app.run()