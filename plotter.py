import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy


def plot(x_labels,y):
    img = BytesIO()
    x_size = len(x_labels)
    x = numpy.array(range(x_size))
    plt.xticks(x, x_labels, rotation='vertical')
    plt.tight_layout()
    plt.plot(x,y)
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url