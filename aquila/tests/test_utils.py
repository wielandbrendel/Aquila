import pytest
import bokeh.plotting

def test_get_num_on_canvas1():
    from aquila.utils import get_num_on_canvas    

    fig = bokeh.plotting.figure()
    fig.line([0, 1], [2, 3])
    assert get_num_on_canvas(fig) == 1

def test_get_num_on_canvas2():
    from aquila.utils import get_num_on_canvas

    fig = bokeh.plotting.figure()
    fig.line([0, 1], [2, 3])
    fig.image()
    assert get_num_on_canvas(fig) == 2
