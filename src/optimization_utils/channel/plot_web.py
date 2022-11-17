import base64
from io import BytesIO
from matplotlib.figure import Figure

def plot(y):
    fig = Figure()
    ax = fig.subplots()
    ax.plot(y)
    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
