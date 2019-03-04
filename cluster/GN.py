#coding:utf-8
import networkx as nx
import math
import csv
import random as rand
import sys
import matplotlib.pyplot as plt

def buildG(G, file_, delimiter_):
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if int(line[2]) != 0:
            G.add_weighted_edges_from([(line[0],line[1],int(line[2]))])

def CmtyStep(G):
    init_number_comp = nx.number_connected_components(G)
    print('init : %d'%init_number_comp)
    number_comp = init_number_comp
    while number_comp <= init_number_comp:
        bw = nx.edge_betweenness_centrality(G)  # edge betweenness for G
        # find the edge with max centrality
        max_ = 0.0
        # find the edge with the highest centrality and remove all of them if there is more than one!
        for k, v in bw.items():
            # print v
            _BW = float(v) / float(G[k[0]][k[1]]['weight'])   # weighted version of betweenness
            if _BW >= max_:
                max_ = _BW
        for k, v in bw.items():
            if float(v) / float(G[k[0]][k[1]]['weight'])  == max_:
                # print "remove an edge!"
                # print k
                G.remove_edge(k[0], k[1])  # remove the central edge
        number_comp = nx.number_connected_components(G)  # recalculate the no of components

def GetModularity(G, deg_, m_):
    New_A = nx.adj_matrix(G)#建立一个表示边的邻接矩阵
    New_deg = {}
    New_deg = UpdateDeg(New_A, G.nodes())
    #计算Q值
    comps = nx.connected_components(G)#建立一个组成的列表
    print('Number of communities in decomposed G: %d' % nx.number_connected_components(G))
    Mod = 0#设定社团划分的模块化系数并设初始值为0
    for c in comps:
        AVW = 0#两条边在邻接矩阵中的值
        K = 0#两条边的度值
        for u in c:
            AVW += New_deg[u]
            K += deg_[u]
        Mod += ( float(AVW) - float(K*K)/float(2*m_) )#计算出Q值公式累加符号后的值
    Mod = Mod/float(2*m_)#计算出模块化Q值
    return Mod

def UpdateDeg(A, nodes):
    deg_dict = {}
    nodes = list(nodes)
    n = len(nodes)#图中点的个数
    B = A.sum(axis = 1)#将矩阵的每一行向量相加，所得一个数组赋给B，表示与每个点相关的边数
    for i in range(n):
        deg_dict[nodes[i]] = B[i, 0]#将该值存到索引是i的元组中
    return deg_dict

def runGirvanNewman(G, Orig_deg, m_,graphname):
    BestQ = 0.0
    Q = 0.0
    # b=[]
    while True:
        CmtyStep(G)
        Q = GetModularity(G, Orig_deg, m_)
        print("Modularity of decomposed G: %f" % Q)
        if Q > BestQ:
            BestQ = Q
            Bestcomps = nx.connected_components(G)
            b = list(Bestcomps)
            print (b)
            BestG = nx.Graph()
            BestG = G
            print ("Components:", Bestcomps)
            # pos = nx.spring_layout(G)
            # nx.draw_networkx_edges(G,pos,alpha=0.4,edge_color='b')
            # nx.draw_networkx_nodes(G,pos,node_color='r')
            # nx.draw_networkx_labels(G,pos,font_size=10,font_color='black')
            nx.draw(BestG,pos= nx.spring_layout(G),node_size = 100,alpha = 0.5,edge_color = 'b',font_size = 9,with_labels = False)
            plt.savefig(graphname)
            plt.clf()
        if G.number_of_edges() == 0:
            break
    if BestQ > 0.0:
        print ("Max modularity (Q): %f" % BestQ)
        print ("Graph communities:", Bestcomps)
        return b
    else:
        print ("Max modularity (Q): %f" % BestQ)
        # print(b)
        # return b



G = nx.Graph()
buildG(G, r'/Users/yaya/Desktop/data.txt', ',')
n = G.number_of_nodes()#顶点数量
print ('顶点数量：%d' % n)
A = nx.adj_matrix(G)#邻接矩阵
m_ = 0.0#计算边的数量
for i in range(0,n):
    for j in range(0,n):
        m_ += A[i,j]
m_ = m_/2.0
#计算点的度
Orig_deg = {}
Orig_deg = UpdateDeg(A, G.nodes())
#调用算法
b = runGirvanNewman(G, Orig_deg, m_,'graph519.png')

print(b)
with open('/Users/yaya/Desktop/result.txt','w') as f:
    for bb in b:
        for bbb in bb:
            f.writelines([bbb,' '])
        f.writelines(['\n'])
