from flask import Flask, render_template
from models.image_read import ImageRead

app = Flask(__name__)

"""
Endpoint for application's main page
"""
@app.route('/ImageDemo')
def load_page():
    return render_template('main.html')

"""
Endpoint for response to button click.
This endpoint returns the serialized image.  The endpoint, 'getImage' uses an async
javascript function to read an image and return it in serialized form.
"""
@app.route('/getImage', methods=['GET'])
def get_image():
    image_reader = ImageRead()
    encoded_image = image_reader.readImage()
    return encoded_image


if __name__ == '__main__':
    app.run(port=5005, debug=True)
