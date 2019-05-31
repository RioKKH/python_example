#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from pathlib import Path


def main():
    p = Path('.')
    q = p.parent / 'data' / 'heatmap.dat'
    df  = pd.read_table(q, delim_whitespace=True)
    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2,
                                   sharex=False,
                                   sharey=False,
                                   figsize=(14, 7))
    sns.heatmap(df.pivot_table(columns='AX',
                               index='AY',
                               values='Real',
                               dropna=False)[::-1],
                cmap='bwr', annot=True, fmt='.2f',
                square=True, vmin=-30, vmax=30, ax=ax0)
    sns.heatmap(df.pivot_table(columns='AX',
                               index='AY',
                               values='Imag',
                               dropna=False)[::-1],
                cmap='bwr', annot=True, fmt='.2f', 
                square=True, vmin=-30, vmax=30, ax=ax1)

    # for ax0
    labels = [item.get_text() for item in ax0.get_xticklabels()]
    ax0.set_xticklabels([str(round(float(label), 2)) for label in labels])
    labels = [item.get_text() for item in ax0.get_yticklabels()]
    ax0.set_yticklabels([str(round(float(label), 2)) for label in labels])

    # for ax1
    labels = [item.get_text() for item in ax1.get_xticklabels()]
    ax1.set_xticklabels([str(round(float(label), 2)) for label in labels])
    labels = [item.get_text() for item in ax1.get_yticklabels()]
    ax1.set_yticklabels([str(round(float(label), 2)) for label in labels])

    # Script below doesn'to work for me.
    #ax0.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    #ax0.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    #ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    #ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    ax0.set_aspect('equal')
    ax1.set_aspect('equal')
    plt.show()


if __name__ == '__main__':
    main()
