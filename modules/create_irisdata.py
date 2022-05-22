from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

dataset = datasets.load_iris()

def create_irisdata(*ags, **kwgs):
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

    fig, ax = plt.subplots()
    ax.scatter(x=dataset.data[dataset.target==0, 0],
              y=dataset.data[dataset.target==0, 1],
              label=dataset.target_names[0],
              c='blue')
    ax.scatter(x=dataset.data[dataset.target==1, 0],
              y=dataset.data[dataset.target==1, 1],
              label=dataset.target_names[1],
              c='red')
    ax.scatter(x=dataset.data[dataset.target==2, 0],
              y=dataset.data[dataset.target==2, 1],
              label=dataset.target_names[2],
              c='green')

    ax.legend(loc='best', fontsize=14)

    ax.set_title('Iris SepalLength / SepalWidth', size=16)
    ax.set_xlabel(dataset.feature_names[0], size=14)
    ax.set_ylabel(dataset.feature_names[1], size=14)

    return df, fig
