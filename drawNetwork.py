# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx

def draw_unweightedG(G):#无权图
    pos = nx.spring_layout(G)# 弹簧布局
    nx.draw(G,pos,node_size = 100,font_size=10,font_family='sans-serif',with_labels=True)
    plt.show()

def draw_weightedG(G):#加权图
    pos = nx.spring_layout(G)# 弹簧布局
    edgewidth = []
    for n,nbrs in G.adjacency_iter():
        for nbr, eattr in nbrs.items():
            edgewidth.append(eattr['weight'])
    nx.draw(G,pos,width = edgewidth,font_size=10,font_family='sans-serif',with_labels=True)
    plt.show()
    
