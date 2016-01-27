from bokeh.models.renderers import GlyphRenderer

def get_num_on_canvas(canvas):
    ''' Gets the number of objects on a Bokeh figure. '''
    return sum([isinstance(renderer, GlyphRenderer) for renderer in canvas.renderers])
