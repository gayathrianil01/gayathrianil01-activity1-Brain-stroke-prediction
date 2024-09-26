import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(conf_matrix):
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()