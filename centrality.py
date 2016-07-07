# -*- coding: utf-8 -*-
import networkx as nx
from operator import itemgetter

def betweenness_centrality(G):
    bc = nx.betweenness_centrality(G,weight='weight')#betweeness
    bc1 = sorted(bc.iteritems(),key=itemgetter(1),reverse=True)#排序
    nbc = [e[0] for e in bc1]
    return nbc[:10]

def closeness_centrality(G):
    cc = nx.closeness_centrality(G)#closeness
    cc1 = sorted(cc.iteritems(),key=itemgetter(1),reverse=True)#排序
    ncc = [e[0] for e in cc1]
    return ncc[:10]
    
def degree_centrality(G):
    dc = nx.in_degree_centrality(G)#degree
    dc1 = sorted(dc.iteritems(),key=itemgetter(1),reverse=True)#排序
    ndc = [e[0] for e in dc1]
    return ndc[:10]

def PageRank(G):
    pr = nx.pagerank(G,alpha=0.9,weight='weight',max_iter=10000)#带不带权重结果没什么变化
    pr1 = sorted(pr.iteritems(),key=itemgetter(1),reverse=True)#排序
    npr = [e[0] for e in pr1]
    return npr[:10]
