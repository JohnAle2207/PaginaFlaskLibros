from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

usuarios_registrados = {'john': 'john', 'juan': 'juan'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Lógica para manejar el registro de usuarios
        return 'Usuario registrado exitosamente!'
    return render_template('registro.html')

@app.route('/categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        categoria = request.form['categoria']
        # Lógica para manejar la categoría de libros
        return 'Categoría de libros agregada!'
    return render_template('categorias.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in usuarios_registrados and usuarios_registrados[username] == password:
            return 'Inicio de sesión exitoso!'
        else:
            return 'Nombre de usuario o contraseña incorrectos.'
    return render_template('login.html')

@app.route('/descarga/<filename>')
def descarga(filename):
    return send_file(f'static/libros/{filename}', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
