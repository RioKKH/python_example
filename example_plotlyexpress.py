#!/usr/bin/env python
# coding: utf-8

from mbm_imagelib import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline
plotly.offline.init_notebook_mode()


img = Image()
filtered = Image()
img.load_file('BR_512-1.pgm')
filtered.load_file('filt.pgm')

fig = plt.figure()
plt.imshow(img.img)
plt.colorbar()
#plotly.offline.iplot_mpl(fig)
#plt.imshow(filtered.img)

filtered.apply_gaussian_filter()
filtered.binarize()
filtered.remove_artifacts_touching_border()
filtered.get_property()

plt.imshow(filtered.labeled_img)

if filtered.n != 1:
    areamax = 0
    for i, region in enumerate(filtered.regions):
        x, y = region.centroid
        perimeter.append(region.perimeter)
        #print(f"{x}, {y}, {perimeter}")

perimeter = [filtered.regions[i].perimeter for i in range(0, len(filtered.regions))]

fig = plt.figure()
plt.boxplot(perimeter[:])

brrawhist = pd.read_csv('br_raw_hist.csv')
brfilterhist = pd.read_csv('br_filter_hist.csv')

brrawhist.plot.bar(x='id', y='freq')

#fig = px.bar(brfilterhist,x='id',y='freq',log_y=True)
fig = px.bar(brrawhist,x='id',y='freq',log_y=True)
fig.update_xaxes(showgrid=True, range=[0,100])
fig.update_yaxes(showgrid=True)

#figure = px.bar(brrawhist,x='id',y='freq',log_y=True)
#px.bar(brfilterhist,x='id',y='freq',log_y=True)
#plotly.offline.plot(figure, filename="br_raw_hist.html", include_plotlyjs=False)
