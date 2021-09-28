from flask import Flask, render_template, request
from models.learning_rate_evaluation import LearningRateEvaluation

app = Flask(__name__)

"""
    Handles the endpoint /LearningRate by rendering the main.html page
"""
@app.route('/LearningRate')
def load_page():
    return render_template('main.html')

"""
    Handles the endpoint /LearningRateGraph.  Gets the form dictionary from the request
    and calls the API LearningRateEvaluation.make_history_graph() that generates the Ascii
    encoded serialization of the graph image.
    :returns: the serialized graph image
"""
@app.route('/getLearningRateGraph', methods=['POST'])
def make_distribution_graph():
    # Get all form values from the request as a dictionary
    form_dict = request.form.to_dict()
    graph_generator = LearningRateEvaluation(form_dict)
    encoded_image = graph_generator.make_history_graph()
    return encoded_image


if __name__ == '__main__':
    app.run(port=5004, debug=True)