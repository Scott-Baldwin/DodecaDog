# %% 
# file dialogs

import os
import tkinter as tk
from tkinter import filedialog as fd

def QuickFile(
        dir = os.getcwd(),
        folder = False,
        multi = False,
        ftypes = [], 
        AllFileTypes = True,
        ):
        """
        docstring
        """
        # add option for all files
        if AllFileTypes: ftypes.append(('All files', '*'))
        # create the root window
        root = tk.Tk()
        root.attributes("-topmost", True) # bring to front
        root.withdraw() # hides root window
        try:
                if folder: filename = fd.askdirectory(
                        parent = root,
                        title = 'Select a folder',
                        initialdir = dir)
                elif multi: filename = fd.askopenfilenames(
                        parent = root,
                        title = 'Select file(s)',
                        initialdir = dir,
                        filetypes = ftypes)
                else: filename = fd.askopenfilename(
                        parent = root,
                        title = 'Select a file',
                        initialdir = dir,
                        filetypes = ftypes)
                return filename
        finally: root.destroy()

# %% 
# scatter plots

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def QuickScatter(
        x = np.random.rand(10),
        y = np.random.rand(10),
        c = np.random.rand(10), 
        cm = 'jet', 
        vmin = 0, 
        vmax = 1, 
        ticks = None,
        xlabel = None,
        ylabel = None,
        units = '',
        pad = 0.05 ):
        """
        docstring
        """
        # convert colormap name to cmap object
        cmap = mpl.cm.get_cmap(cm)
        # setup colorbar
        norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
        sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
        # initaialize fig
        fig, ax = plt.subplots()
        # plot data
        ax.scatter(x, y, color=sm.cmap(sm.norm(c)))
        # define axis labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        # define annotations
        txt = [str(round(i,1)) for i in c]
        # plot annotations
        for x,y,t in zip(x,y,txt): ax.annotate(t, xy=(x, y))
        # add colorbar
        cb = plt.colorbar(
                sm,
                ax = ax,
                orientation = 'vertical',
                ticks = ticks,
                pad = pad)
        # add colorbar label
        cb.set_label(
                units, 
                labelpad = -45,
                fontsize = 10)
        return fig, ax

# %%
### END