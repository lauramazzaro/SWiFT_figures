import matplotlib

params = {
    'text.latex.preamble': ['\\usepackage{gensymb}'],
    'image.origin': 'lower',
    'image.interpolation': 'nearest',
    'image.cmap': 'gray',
    'axes.grid': False,
    'savefig.dpi': 350,  # to adjust notebook inline plot size
    'axes.labelsize': 22, # fontsize for x and y labels (was 10)
    'axes.titlesize': 22,
    'lines.linewidth': 4,
    'font.size': 22, # was 10
    'legend.fontsize': 22, # was 10
    'xtick.labelsize': 22,
    'ytick.labelsize': 22,
    #'text.usetex': True,
    'figure.figsize': [3.39, 2.10],
    'font.family': 'sans-serif',
}
matplotlib.rcParams.update(params)
