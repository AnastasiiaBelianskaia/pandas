import pandas as pd
import matplotlib.pyplot as plt


def plotting():
    df = pd.read_csv('data_plotting.csv')
    df.plot()
    return plt.show()


def scatter_plot():
    df = pd.read_csv('data_plotting.csv')
    df.plot(kind='scatter', x='Duration', y='Calories')
    return plt.show()


def histogram():
    df = pd.read_csv('data_plotting.csv')
    df['Duration'].plot(kind='hist')
    return plt.show()


if __name__ == '__main__':
    plotting()
    scatter_plot()
    histogram()
