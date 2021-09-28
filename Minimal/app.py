from flask import Flask, render_template

app = Flask(__name__)


# Map the url, /MinimalWebApp to the function, load_page
@app.route('/MinimalWebApp')
def load_page():
    return render_template('static_page.html')


if __name__ == '__main__':
    app.run(port=5001, debug = True)
