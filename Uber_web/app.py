from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/notebook.html',methods=['GET','POST'])
def notebook():
    return render_template('notebook.html')

@app.route('/dashboard.html',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(host = 'localhost', port =80)   