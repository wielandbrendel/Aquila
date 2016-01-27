from bokeh.io import push_notebook
from bokeh.plotting import gridplot

class Monitor(object):

    def __init__(self, instances, fig_width=1000, fig_height=400):
        self.instances  = instances
        self.fig_width  = fig_width
        self.fig_height = fig_height

    def _collect_unique_canvas(self):
        return [e.canvas for i, e in enumerate(self.instances) if self.instances.index(e) == i]
        # return set([f.canvas for f in self.instances])

    def get_figure(self):
        canvases = list(self._collect_unique_canvas())
        n_cols = 3
        n_rows = (len(canvases)-1)//3 + 1

        # set correct size of figure
        for c in canvases:
            c.plot_width  = self.fig_width//n_cols
            c.plot_height = self.fig_height//n_rows

        # get figures
        grid = []
        for row in range(n_rows):
            grid.append(canvases[n_cols*row:n_cols*(row+1)])

        return gridplot(grid)

    def update(self, **kwargs):
        for i in self.instances:
            i.update(**kwargs)

        self.push()

    def push(self):
        push_notebook()
