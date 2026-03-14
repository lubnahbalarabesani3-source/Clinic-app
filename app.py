from flask import Flask, render_temp
late, request, redirect
from models import Patient

app = Flask(__name__)


patient_queue = [] 

@app.route('/') 
def index():
    return render_template('index.html', patients=patient_queue)

@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    ailment = request.form.get('ailment')
    if name and ailment:
        new_p = Patient(name, ailment)
        patient_queue.append(new_p)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
