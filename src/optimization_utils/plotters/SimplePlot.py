import matplotlib.pyplot as plt
from .LinePlot import LinePlot


class SimplePlot:
    def __init__(self) -> None:
        self.plots = []

    def plot(self, obj):
        self.plots.append(obj)

    def create_plot(self):
        self.fig, self.axs = plt.subplots(len(self.plots))
        for index, plots in enumerate(self.plots):
            plots = [plots] if type(plots) != list else plots
            for plot in plots:
                ax = self.axs[index] if len(self.plots) > 1 else self.axs
                if isinstance(plot, LinePlot):
                    ax.plot(
                        plot.x,
                        plot.y,
                        label=plot.legend
                    )
                    if plot.legend:
                        ax.legend(loc="upper left")
                else:
                    raise Exception("Unknown plotting type")

    def show(self):
        self.create_plot()
        plt.show()

    def save(self, name):
        self.create_plot()
        plt.savefig(name)