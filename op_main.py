from getspeaker import *
from createNetwork import *
from centrality import *
from draw import *


def zqx(l1,l2):
    return float(len([e for e in l1 if e in l2]))/len(l1)
    
item = '2011tx3.txt'
sponser = important_speakers(item)
yucedict = {e:sponser.count(e) for e in set(sponser)}
paixudict = sorted(yucedict.iteritems(),key=itemgetter(1),reverse=True)#排序
yucepaixu = [e[0] for e in paixudict][:10]
yucepaixu1 = [e[0] for e in paixudict][:5]
print 'yucepaixu'
print yucepaixu

#有向网络
G0 = network_wuquan()
G1 = network_jiaquan()

c0_10 = degree_centrality(G0)
c1_10 = degree_centrality(G1)
print 'degree_centrality'
print c0_10,zqx(c0_10[:10],yucepaixu[:10]),zqx(c0_10,yucepaixu)
print c0_10,zqx(c0_10[:5],yucepaixu1[:5]),zqx(c0_10,yucepaixu)
print c1_10,zqx(c1_10[:10],yucepaixu[:10]),zqx(c1_10,yucepaixu)
print c1_10,zqx(c1_10[:5],yucepaixu1[:5]),zqx(c1_10,yucepaixu)

c0_10 = betweenness_centrality(G0)
c1_10 = betweenness_centrality(G1)
print 'betweenness_centrality'
print c0_10,zqx(c0_10[:10],yucepaixu[:10]),zqx(c0_10,yucepaixu)
print c0_10,zqx(c0_10[:5],yucepaixu1[:5]),zqx(c0_10,yucepaixu)
print c1_10,zqx(c1_10[:10],yucepaixu[:10]),zqx(c1_10,yucepaixu)
print c1_10,zqx(c1_10[:5],yucepaixu1[:5]),zqx(c1_10,yucepaixu)

c0_10 = closeness_centrality(G0)
c1_10 = closeness_centrality(G1)
print 'closeness_centrality'
print c0_10,zqx(c0_10[:10],yucepaixu[:10]),zqx(c0_10,yucepaixu)
print c0_10,zqx(c0_10[:5],yucepaixu1[:5]),zqx(c0_10,yucepaixu)
print c1_10,zqx(c1_10[:10],yucepaixu[:10]),zqx(c1_10,yucepaixu)
print c1_10,zqx(c1_10[:5],yucepaixu1[:5]),zqx(c1_10,yucepaixu)

P0_10 = PageRank(G0)
P1_10 = PageRank(G1)
print 'PageRank'
print P0_10,zqx(P0_10[:10],yucepaixu[:10]),zqx(P0_10,yucepaixu)
print P0_10,zqx(P0_10[:5],yucepaixu1[:5]),zqx(P0_10,yucepaixu)
print P1_10,zqx(P1_10[:10],yucepaixu[:10]),zqx(P1_10,yucepaixu)
print P1_10,zqx(P1_10[:5],yucepaixu1[:5]),zqx(P1_10,yucepaixu)
