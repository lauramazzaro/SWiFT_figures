import matplotlib

params = {
    'text.latex.preamble': ['\\usepackage{gensymb}'],
    'image.origin': 'lower',
    'image.interpolation': 'nearest',
    'image.cmap': 'gray',
    'axes.grid': False,
    'savefig.dpi': 350,  # to adjust notebook inline plot size
    'axes.labelsize': 24, # fontsize for x and y labels (was 10)
    'axes.titlesize': 24,
    'lines.linewidth': 2,
    'font.size': 24, # was 10
    'legend.fontsize': 24, # was 10
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    #'text.usetex': True,
    'figure.figsize': [3.39, 2.10],
    'font.family': 'serif',
}
matplotlib.rcParams.update(params)
