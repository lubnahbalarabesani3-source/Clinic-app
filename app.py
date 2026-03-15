from flask import Flask,render_template,request,redirect,url_for
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
    priority = request.form.get('priority')
    
    if name and ailment:
        patient_queue.append({'name': name, 'ailment': ailment, 'priority': priority})
    
    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete_patient(index):
    if 0 <= index < len(patient_queue):
        patient_queue.pop(index)
    return redirect('/')

@app.route('/clear')
def clear_queue():
    patient_queue.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

