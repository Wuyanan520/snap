# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:10:04 2017

@author: 08119
"""
import networkx as nx
import pandas as pd
from tnm import *
import os
path = os.getcwd()

filename = 'CollegeMsg.txt'
fh = pd.read_csv(filename,names=['node1', 'node2', 'timestamp'],header=None,delim_whitespace=True)
#fh.head()
#构建网络
G=nx.from_pandas_dataframe(fh,'node1','node2',edge_attr='timestamp', create_using=nx.MultiGraph())

nswap = 2 * len(G.edges())
maxtry = 100 * nswap

G0 = edges_swap_0k(G, nswap=nswap, max_tries=maxtry)
nx.write_edgelist(G0, path+'/G0.txt',data=['timestamp'])
G0 = pd.read_csv('G0.txt',sep=' ',header=None)
G0.sort_values(by=2).to_csv('G0.txt',sep=' ',header=None, index=None)


G0 = edges_swap_1k(G, nswap=nswap, max_tries=maxtry)
nx.write_edgelist(G0, path+'/edges_swap_1k.txt',data=['timestamp'])

G0 = time_swap(G, nswap=nswap, max_tries=maxtry)
nx.write_edgelist(G0, path+'/time_swap.txt',data=['timestamp'])


G0 = time_random(G, nswap=nswap, max_tries=maxtry,mins=fh.timestamp.min(),maxs=fh.timestamp.max())
nx.write_edgelist(G0, path+'/time_random.txt',data=['timestamp'])


G0 = timeweight_swap(G, nswap=nswap, max_tries=maxtry)
nx.write_edgelist(G0, path+'/timeweight_swap.txt',data=['timestamp'])