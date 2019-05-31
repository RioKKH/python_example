#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

days = mdates.DayLocator()
hours = mdates.HourLocator()
daysFmt = mdates.DateFormatter("%d")

df25 = pd.read_csv('190313.csv', index_col=0, parse_dates=True, comment='#')
df05 = pd.read_csv('190507.csv', index_col=0, parse_dates=True, comment='#')
df25 = pd.read_csv('190406.csv', index_col=0, parse_dates=True, comment='#')
df05 = pd.read_csv('190507.csv', index_col=0, parse_dates=True, comment='#')

df25.index -= df25.index[0]
df05.index -= df05.index[0]
df25.index -= df25.index[0]
df05.index -= df05.index[0]

df25 = df25.assign(hours=(df25.index.total_seconds() / 3600))
df05 = df05.assign(hours=(df05.index.total_seconds() / 3600))
df25 = df25.assign(hours=(df25.index.total_seconds() / 3600))
df05 = df05.assign(hours=(df05.index.total_seconds() / 3600))

ax = df25.plot(x='hours', y='dall', color='orange', marker="o", alpha=0.5, label='25nm')
df05.plot(x='hours', y='dall', color='blue', marker="o", alpha=0.5, ax=ax, label='5nm')
df25.plot(x='hours', y='dall', color='red', marker="o", alpha=0.5, ax=ax, label='25nm')
df05.plot(x='hours', y='dall', color='green', marker="o", alpha=0.5, ax=ax, label='5nm')
plt.legend()
plt.xlabel("Hours")
plt.ylabel("diameter[um]")
plt.grid()
plt.savefig('comparison.png', bbox_inches='tight', dpi=150)
#ax.xaxis.set_major_locator(days)
#ax.xaxis.set_minor_locator(hours)
#ax.xaxis.set_major_formatter(daysFmt)

