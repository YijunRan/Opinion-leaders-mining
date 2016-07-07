# -*- coding: utf-8 -*-
import networkx as nx
from response_words import *

def network_wuquan(): #分话题无权网络
    G = nx.DiGraph()
    listdata = WuQuan()
    for data in listdata:
         G.add_edges_from(data)
    return G

def network_jiaquan(): #分话题加权网络
    G = nx.DiGraph()
    listdata = JiaQuan()
    for data in listdata:
        G.add_weighted_edges_from(data)
    return G
        
