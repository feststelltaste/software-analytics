ax = top10.plot.scatter('sha', 'code');

for k, v in top10.iterrows():
    ax.annotate(k.split("/")[-1], v)