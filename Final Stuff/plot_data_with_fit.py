"""
This function plots two curves of data
"""
__author__ = "Wyatt"


import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):
  
  scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
  curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
  plt.show()
  
  return scatter_plot, curve_plot
