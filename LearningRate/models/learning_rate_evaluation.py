from sklearn.datasets import make_blobs
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from matplotlib import pyplot as plt
from io import BytesIO
import base64

"""
Class LearningRateEvaluation provides graphs of Cross Entropy Loss and Accuracy for a multiclass
classification model. In particular the class generates data by using the make_blobs() method from
sklearn.datasets package.  The model will attempt to classify the points (2-D) in the data into 3 
classifications. Layers will be added to a Sequential model. The class initializer allows the values:
number of samples, learning rate, number of nodes in the hidden layer, and the number of epochs.

This class has one public method:  make_history_graph()
This class has three private methods:  _make_data(), _build_model(), and _train_and_test()
"""

class LearningRateEvaluation:
    def __init__(self, form_dict):
        self.samples = int(form_dict.get("size"))
        self.learning_rate = float(form_dict.get("learningRate"))
        self.n_nodes = int(form_dict.get("nodes"))
        self.n_epochs = int(form_dict.get("epochs"))

    """
    Private Method
    Make 2-D with 3 centers for classification.  The points have a STD of 2 and the method will produce
    the same data for every call with the same parameters
    :returns: training and test arrays separated into x and y values
    """
    def _make_data(self):
        X, y = make_blobs(n_samples=self.samples, centers=3, n_features=2, cluster_std=2, random_state=2)
        # One hot encode labels
        y = to_categorical(y)
        train_size = self.samples // 2
        trainX, testX = X[:train_size, :], X[train_size :, :]
        trainy, testy = y[:train_size], y[train_size:]
        return trainX, trainy, testX, testy

    """
    Private method
    Build a Sequential model with one hidden layer.  The output has values and uses 'softmax' activation.
    :return: the compiled Sequential model
    """
    def _build_model(self):
        model = Sequential()
        model.add(Dense(self.n_nodes, input_dim=2, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(3, activation='softmax'))
        optimizer = SGD(lr=self.learning_rate, momentum=0.9)
        model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        return model

    """
    Private method
    Trains and tests the model from the data created by self._make_data().
    :returns: a history of the train and test process
    """
    def _train_and_test(self):
        trainX, trainy, testX, testy = self._make_data()
        model = self._build_model()
        history = model.fit(trainX, trainy, validation_data=(testX, testy), epochs=self.n_epochs,
                            verbose=0, batch_size=1)
        return history

    """
    Public method
    Calls on the class's self._train_and_test() to generate a history object.  
    Plots Cross-Entropy Loss and Accuracy of both the training and test processes.
    :returns: Ascii encoded serialization of the graphs. 
    """
    def make_history_graph(self):
        history = self._train_and_test()
        plt.clf()
        figure, ax = plt.subplots(nrows=2)
        ax[0].set_title('Cross-Entropy Loss')
        ax[0].plot(history.history['loss'], label='train')
        ax[0].plot(history.history['val_loss'], label='test')
        ax[0].legend()
        ax[0].set_xlabel("Epoch")
        ax[0].set_ylabel("Mean Abs Error")
        ax[1].set_title('Accuracy')
        ax[1].plot(history.history['accuracy'], label='train')
        ax[1].plot(history.history['val_accuracy'], label='test')
        ax[1].legend()
        ax[1].set_xlabel("Epoch")
        ax[1].set_ylabel("Accuracy")
        figure.tight_layout()
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        buff_contents = buffer.getvalue()
        buff_encoded = base64.b64encode((buff_contents))
        buff_str = buff_encoded.decode('ascii')
        encoded = base64.b64encode(buffer.getvalue()).decode('ascii')
        plt.close()
        return encoded
        




