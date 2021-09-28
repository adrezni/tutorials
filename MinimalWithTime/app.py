from flask import Flask, render_template
from models.time_generator import TimeGenerator

app = Flask(__name__)


# Map the url, /MinimalWithTime to the function, load_page
@app.route('/MinimalWithTime')
def load_page():

    # Call on the static method get_curr_datetime()
    curr_datetime = TimeGenerator.get_curr_datetime()
    # Render the html file, but pass a parameter called date_time whose value
    # will be curr_datetime
    return render_template('minimal_with_time.html', date_time = curr_datetime)


if __name__ == '__main__':
    app.run(port=5001, debug = True)