import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Generate 'random' data
np.random.seed(0)
X = 2.5 * np.random.randn(100) + 1.5     # Array of 100 values with mean = 1.5, stdev = 2.5
res = 0.5 * np.random.randn(100)        # Generate 100 residual terms
Y = 2 + 0.3 * X + res                   # Actual values of Y

# Create pandas dataframe to store our X and Y values
df = pd.DataFrame(
    {'X': X,
    'y': Y}
)

# Show the first five rows of our dataframe
df.head()