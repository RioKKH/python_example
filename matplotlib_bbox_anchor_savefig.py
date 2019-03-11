#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pandas as pd
import matplotlib.pyplot as plt


def main(fname):
    df = pd.read_csv(fname, index_col=0, parse_dates=True)
    ax = df.plot(figsize=(9, 7), marker='o')
    ax.legend(loc='upper left', framealpha=0.8, bbox_to_anchor=(1.05, 1.0))
    plt.subplots_adjust(right=0.8)
    plt.grid(ls='dashed', color='gray', alpha=0.8)
    plt.savefig('test.png', bbox_inches='tight', dpi=100)


if __name__ == "__main__":
    main(sys.argv[1])

