import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import brewer2mpl
from matplotlib import rcParams
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 10})
%matplotlib inline

'''
Build a DataFrame from the data (ideally, put all data in this object)

Clean the DataFrame. It should have the following properties:
    Each row describes a single object
    Each column describes a property of that object
    Columns are numeric whenever appropriate
    Columns contain atomic properties that cannot be further decomposed
Explore global properties. Use histograms, scatter plots, and aggregation functions to summarize the data.
Explore group properties. Use groupby and small multiples to compare subsets of the data.
'''


#colorbrewer2 Dark2 qualitative color table
dark2_cmap = brewer2mpl.get_map('Dark2', 'Qualitative', 7)
dark2_colors = dark2_cmap.mpl_colors

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'white'
rcParams['patch.facecolor'] = dark2_colors[0]
rcParams['font.family'] = 'StixGeneral'


def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks

    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)


df = pd.read_csv('/Users/stevalang/Galvanize/0002_capstones/capstone1/data/bank/bank-full.csv', delimiter=';')

df_grouped = df.groupby('job').agg({'LoanNr': 'count', 'Default': 'mean'})