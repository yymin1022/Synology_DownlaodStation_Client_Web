from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    value = request.form['fileURL']
    return value

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)