#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def load_data(df, resample=True, interval='S'):
    """
    Return 
    """
    if resample:
        df = pd.read_csv(df, index_col=0, parse_dates=True)
        return df.resample('S').interpolate()
    else:
        return pd.read_csv(df, index_col=0, parse_dates=True)


def make_corresponding_data(shorter, longer):
    """
    Make a interpolated data then return it.
    length(<dataframe> shorter) < lenght(<dataframe> longer)

    Parameters
    -------------------------
    shorter : A pandas dataframe
        The length of this dataframe should be shorter than the other one.

    longer : A pandas dataframe
        The length of this dataframe should be longer than the other one.

    Returns
    -------------------------
    longer_selected : A dataframe of pandas. This dataframe has interpolated
    data in terms of the given time period and only corresponding data to
    shorter dataframe index.
    """

    length_shorter = shorter.index.shape
    index_shorter = shorter.index.values.reshape([length_shorter[0], -1])

    length_longer = longer.index.shape
    index_longer = longer.index.values.reshape([length_longer[0], -1])

    diff = longer_index - shorter_index.T
    print(diff.shape)

    argmin_index = np.argmin(np.abs(diff), axis=0)
    longer_selected = longer.iloc[argmin_index]

    return longer_selected

