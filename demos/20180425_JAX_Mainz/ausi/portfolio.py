#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt

def plot_diagram(plot_data, x, y, size='Size'):
    
    fig, ax = plt.subplots()

    ax = plot_data.plot.scatter(
        x,
        y,
        s=plot_data[size] * 100,
        alpha=0.7,
        title="Portfolio-Analyse",
        figsize=[10,7],
        fontsize=14,
        ax=ax
    )

    ax.title.set_size(24)
    plt.xlabel(x, fontsize=18)
    plt.ylabel(y, fontsize=18)
    
    # plot vertical axis
    ax.plot(
        [plot_data[x].max()/2, plot_data[x].max()/2],
        [0, plot_data[y].max()], color='k', linestyle='--', linewidth=0.6)
    # plot horizonzal axis
    ax.plot(
        [0, plot_data[x].max()],
        [plot_data[y].max()/2,plot_data[y].max()/2], color='k', linestyle='--', linewidth=0.6)
    
    # plot fields' key words
    ax.text(plot_data[x].max()*1/4, plot_data[y].max()*3/4, "Strengths", ha="center", fontsize=24)
    ax.text(plot_data[x].max()*3/4, plot_data[y].max()*3/4, "Weaknesses", ha="center", fontsize=24)
    ax.text(plot_data[x].max()*1/4, plot_data[y].max()*1/4, "Opportunities", ha="center", fontsize=24)
    ax.text(plot_data[x].max()*3/4, plot_data[y].max()*1/4, "Threats", ha="center", fontsize=24)
    
    for k, v in plot_data[[x, y]].iterrows():
        ax.annotate(k, v, horizontalalignment='center', verticalalignment='middle', fontsize=14)
    
    return ax