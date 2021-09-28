import base64
from io import BytesIO
import seaborn as sns
from scipy.stats import uniform, norm, gamma, poisson
"""
This class generates probability distributions using randomly created data.  In particular,
the distributions are: Uniform, Normal, Gamma and Poisson.  There is only one public method
besides the class initiator in this class and that is generateGraph().  All the other methods
in this class are for private use of the class only.

This class uses stats from scipy.stats for the generation of data points.  The graphing is
done using the seaborn library.

Attributes
__________
form_dictionary: dictionary
    a dictionary of parameters used for data generation and graphing
    
Public Methods
    generateGraph(graph_type)
"""


class GraphGenerator():
    """
    This initializer takes a dictionary of values that are used in the data and graph generation.
    :param form_dict A dictionary object with 7 keys. The keys are: 'graphType', 'size', 'start', 'width',
        'loc', 'scale', 'shape'
    """
    def __init__(self, form_dict):
        self.form_dictionary = form_dict
        # Plotting style
        sns.set(color_codes=True)

    """
    Public Method
    Generates an Ascii encoded serialization of the graph image
    :param graph_type: a str value that is one of "1", "2", "3" or "4" that represent Uniform, Normal,
        Gamma or Poisson distributions
    :returns: Ascii encoded serialization of the graph image  
            The graph image depends upon the value of the param graph_type
    """
    def generate_graph(self):
        graph_type = self.form_dictionary.get("graphType")
        if "1" == graph_type:
            return self._graph_uniform_dist()
        elif "2" == graph_type:
            return self._graph_normal_dist()
        elif "3" == graph_type:
            return self._graph_gamma_dist()
        elif "4" == graph_type:
            return self._graph_poisson_dist()
    """
    Private Method
    :returns: Ascii encoded serialized Uniform Distribution graph image
    """
    def _graph_uniform_dist(self):
        n = int(self.form_dictionary.get("size"))
        start = int(self.form_dictionary.get("start"))
        width = int(self.form_dictionary.get("width"))
        num_bins = 50
        data_uniform = uniform.rvs(size=n, loc=start, scale=width)
        ax = self._get_displot(data_uniform, num_bins, 'Uniform Distribution')

        return self._build_encoded_HTML(ax)

    """
    Private Method
    :returns: Ascii encoded serialized Normal Distribution graph image
    """

    def _graph_normal_dist(self):
        n = int(self.form_dictionary.get("size"))
        loc = int(self.form_dictionary.get("loc"))
        scale = int(self.form_dictionary.get("scale"))
        num_bins = 50
        data_normal = norm.rvs(size=n, loc=loc, scale=scale)
        ax = self._get_displot(data_normal, num_bins, 'Normal Distribution')

        return self._build_encoded_HTML(ax)

    """
    Private Method
    :returns: Ascii encoded serialized Gamma Distribution graph image
    """
    def _graph_gamma_dist(self):
        n = int(self.form_dictionary.get("size"))
        shape = int(self.form_dictionary.get("shape"))
        data_gamma = gamma.rvs(a = shape, size = n)
        num_bins = 50
        ax = self._get_displot(data_gamma, num_bins, 'Gamma Distribution')

        return self._build_encoded_HTML(ax)

    """
    Private Method
    :returns: Ascii encoded serialized Poisson Distribution graph image
    """
    def _graph_poisson_dist(self):
        n = int(self.form_dictionary.get("size"))
        shape = int(self.form_dictionary.get("shape"))
        data_poisson = poisson.rvs(mu=shape, size=n)
        num_bins = 30
        ax = self._get_displot(data_poisson, num_bins, 'Poisson Distribution')

        return self._build_encoded_HTML(ax)

    """
    Private method
    :returns:  seaborn.axisgrid.FacetGrid object used for plotting
    """
    def _get_displot(self, data, bins, distribution_title):
        ax = sns.displot(data, kde=True, color='blue', bins=bins, stat='density', height=5, aspect=1.5,
                         line_kws={'lw': 1}, facecolor='skyblue', edgecolor='white')
        ax.set(xlabel=distribution_title, ylabel='Frequency')
        return ax

    """
    Private method
    :returns: The base64 encoded graph image string 
    """
    def _build_encoded_HTML(self, ax):
        buffer = BytesIO()
        ax.savefig(buffer, format="png")
        buffer.seek(0)
        encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
        return encoded

