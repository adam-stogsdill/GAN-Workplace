import tensorflow as tf
import numpy as np
import pandas as pd

class GenerativeModel(tf.keras.Model):

    def __init__(self):
        super(GenerativeModel, self).__init__()