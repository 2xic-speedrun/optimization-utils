
class LinePlot:
    def __init__(self, x=None, y=None, title=None, legend=None) -> None:
        assert y is not None, "Y cannot be none"
        self.x = list(range(len(y))) if not x else x
        self.y = y
        self.title = title
        self.legend = legend
