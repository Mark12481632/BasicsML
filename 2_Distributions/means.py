# ==================================================
# Check that means of general distributions follow
# a normal distribution.
# The totals should cover a large number of samples.
# ==================================================
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(num_bins, data):
    plt.figure()
    plt.hist(data, bins=num_bins, edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title(f'Histogram: {num_bins} bins')
    plt.show()

rng = np.random.default_rng(242)

# Number samples:
num_samples = 10000
num_in_total = 500

# Select distribution
#data = rng.normal(loc=1.5, scale=2.5, size=num_samples*num_in_total)
#data = rng.poisson(lam=3.2, size=num_samples*num_in_total)
data  = rng.exponential(scale=1.0/4.3, size=num_samples*num_in_total)

totals = [np.sum(data[indx*num_in_total:indx*num_in_total+num_in_total]) for indx in range(num_samples)]

# Plot as histogram
plot_histogram(100, totals)