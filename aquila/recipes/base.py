__all__ = [
    "Recipe",
]

from .. import utils
from bokeh.plotting import figure
import time

class Recipe(object):

    def __init__(self, canvas=None, **kwargs):
        if canvas is None:
            self.set_canvas(**kwargs)
        elif isinstance(canvas, Recipe):
            self.canvas = canvas.canvas
        else:
            self.canvas = canvas

        self.nitem = utils.get_num_on_canvas(self.canvas)
        self.time_created = time.time()

    def set_canvas(self, **kwargs):
        self.canvas = figure(title_text_font_size='10pt', **kwargs)

    def get_canvas(self):
        return self.canvas

    def update(self, value):
        raise NotImplementedError("Recipe does not implement the update()"
                                  "method. You will want to use a subclass"
                                  "such as Progress.")
