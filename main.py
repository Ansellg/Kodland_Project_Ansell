# Impor
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, ):
    # Variabel yang memungkinkan penghitungan konsumsi energi peralatan
    home_coef = 2.3
    light_coef = 200
    return size * home_coef + lights * light_coef  

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')
# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Perhitungan
@app.route('/<size>/<lights>')
def end(size, lights):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights)
                                                    )
                        )
# Formulir
@app.route('/form')
def form():
    return render_template('form.html')

#Hasil formulir
@app.route('/submit', methods=['POST'])
def submit_form():
    # Mendeklarasikan variabel untuk pengumpulan data
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    with open('data.txt', 'w') as f:
        f.write(f'nama: {name}\n')
        f.write(f'email: {email}\n')
        f.write(f'address: {address}\n')
        f.write(f'date: {date}\n')
        f.write('==============\n')

    # Anda dapat menyimpan data Anda atau mengirimkannya melalui email
    return render_template('form_result.html', 
                           # Tempatkan variabel di sini
                           name=name,
                           email=email,
                           address=address,
                           date=date
                           )

app.run(debug=True)
