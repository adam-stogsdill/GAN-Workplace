import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Model

class Deep_Convolutional_Generative_Adversarial_Network(Model):

    def __init__(self, input_shape):
        super(Deep_Convolutional_Generative_Adversarial_Network, self).__init__()
        self.optimization = None # Define the optimization method for this model
        self.loss_function = None # Define the loss function of the data
        # initialize and instantiate layers

    def predict(self, input_data):
        # Method to feed data through
        pass
    
    def fit(self, data):
        epochs = 10
        for e in range(epochs):
            print("Epoch",e+1,":")
            for step, input_data in enumerate(data):
                with tf.GradientTape() as tape:
                    # calculate output
                    ouput = self.predict(input_data)
                    # calculate loss


epochs = 10
for e in range(epochs):
    print("Epoch",e+1,":")

    with tf.GradientTape() as tape:
        # calculate output

        # calculate loss
