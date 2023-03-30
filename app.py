from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Jackson Truong! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def abot():
    return render_template('about.html')

@app.route('/favorite-course')
def fav():
    return render_template('favorite_courses.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.methos == 'POST':
        print('First name entered: ' + request.form.get('first_name'))
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
