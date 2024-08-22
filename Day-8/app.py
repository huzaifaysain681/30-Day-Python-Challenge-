from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

from flask import request

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here, you could save the data, send an email, etc.
    return f"Thanks for reaching out, {name}! I'll get back to you soon."

if __name__ == '__main__':
    app.run(debug=True)
