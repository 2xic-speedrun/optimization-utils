import base64
from io import BytesIO
from matplotlib.figure import Figure

def plot_xy(y):
    fig = Figure()
    ax = fig.subplots()
    ax.plot(y)
    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

def plot_image(weight, epoch):
    fig = Figure()
    ax = fig.subplots()
    ax.imshow(weight)
    buf = BytesIO()
    ax.set_title(epoch)
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
