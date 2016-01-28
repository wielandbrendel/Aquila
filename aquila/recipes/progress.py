from .base import Recipe
from numpy import isnan
import time

class Line(Recipe):

    def __init__(self, y, x='time()', smooth=None, fun=None, **kwargs):
        super(Line, self).__init__(**kwargs)
        self.line = self.canvas.line([], [], line_width=3)
        self.leak = 1/float(smooth) if smooth is not None and smooth > 1 else 1
        self.fun  = fun

        if isinstance(y, str) and isinstance(x, str):
            self.y_key = y
            self.x_key = x
            self.x     = self.line.data_source.data["x"]
            self.y     = self.line.data_source.data["y"]

    def update(self, **kwargs):
        x = kwargs[self.x_key] if self.x_key != 'time()' else time.time() - self.time_created
        y = kwargs[self.y_key] if self.fun is None else self.fun(**kwargs)

        # smoothing of data
        if len(self.y) > 0 and not isnan(self.y[-1]):
            y = self.leak*y + (1 - self.leak)*self.y[-1]

        self.x.append(x)
        self.y.append(y)
