from flask import Flask, render_template, request
from models.graph_generator import GraphGenerator
app = Flask(__name__)

"""
    Handles the endpoint /Distribution by rendering the main.html page
"""
@app.route('/Distribution')
def load_page():
    return render_template('main.html')

"""
    Handles the endpoint /getDistributionGraph.  Gets the form dictionary from the request
    and calls the API GraphGenerator.generate_graph() that generates the serialized image.
    :returns: Ascii encoded serialized graph image
"""
@app.route('/getDistributionGraph', methods=['POST'])
def make_distribution_graph():
    # Get all form values from the request as a dictionary
    form_dict = request.form.to_dict()
    graph_generator = GraphGenerator(form_dict)
    encoded_image = graph_generator.generate_graph()
    return encoded_image


if __name__ == '__main__':
    app.run(port=5004, debug=True)

