"""Model utilities for example ML project."""

import numpy as np

class SimpleModel:
    """A simple linear regression model."""

    def __init__(self):
        """Initialize model parameters."""
        self.weights = None

    def train(self, X, y):
        """Fit model to data."""
        self.weights = np.linalg.pinv(X) @ y

    def predict(self, X):
        """Predict values using the model."""
        return X @ self.weights
