from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world() -> 'html':
    h = 'Hello ME!!!!'
    return render_template('base.html', html_text=h)


if __name__ == '__main__':
    app.run()
