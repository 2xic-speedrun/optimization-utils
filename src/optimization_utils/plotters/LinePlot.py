
class LinePlot:
    def __init__(self, x=None, y=None, title=None, legend=None, x_text=None, y_text=None, y_min=None, y_max=None) -> None:
        assert y is not None, "Y cannot be none"
        self.x = list(range(len(y))) if not x else x
        self.y = y
        self.title = title
        self.legend = legend
        self.x_text = x_text
        self.y_text = y_text
        self.ylim = [y_min, y_max]
