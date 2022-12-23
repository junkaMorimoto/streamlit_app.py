import streamlit as st
from pyparsing.helpers import string_end
from IPython.utils.tempdir import TemporaryDirectory
from matplotlib.projections import ProjectionRegistry
from sympy.geometry import *
import matplotlib.pyplot as plt
import numpy as np
import math
import csv
#%matplotlib inline

st.title('こん')

#tmp = np.array([[1,4],[4,6],[5,4],[5,7],[1,7]])
tmp = np.array([[5,1.1],[5.23,6.16],[10.003,5.92],[10.6,11.2],[6.13,11.99],[5.5,9.4],[1.6,9.2],[3.14,17.21],[16.543,14.123],[14.99,0.625]])
line = 0.5
leftx = min(r[0] for r in tmp)
lefty= min(r[1] for r in tmp)
leftx2 = min(r[0] for r in tmp)
lefty2= min(r[1] for r in tmp)
adjustup = 1
count = 1
putresult = []
totalresult = np.empty((0,8))
putupresult = np.empty((0,8))

def getpoint(x,y):
  allpoint =[]
  point1 = []
  point2 = []
  point3 = []
  point4 = []
  result = np.empty((0,8))
  leftx = x
  lefty = y
  count = 0

  point1 = np.array([leftx,lefty]).reshape(2,1)
  point2 = np.array([leftx,math.sqrt(3)*line+lefty]).reshape(2,1)
  point3 = np.array([line/2+leftx,math.sqrt(3)*line/2+lefty]).reshape(2,1)
  point4 = np.array([3*line/2+leftx,math.sqrt(3)*line/2+lefty]).reshape(2,1)
  allpoint = np.append(point1, point2)
  allpoint = np.append(allpoint,point3)
  allpoint = np.append(allpoint,point4)
  result = np.append(result,np.array([allpoint]),axis=0)
  leftx = leftx + 3*line/2
  lefty = lefty  -math.sqrt(3)*line/2
  count = count + 1
  return(result)

#最小X,Y地点から最大Y地点プラスα地点まで描写
while lefty2 < max([r[1] for r in tmp]) + adjustup :
  lefty = lefty2
  while  leftx < max([r[0] for r in tmp]):
      putresult = getpoint(leftx,lefty)
      totalresult = np.append(totalresult,np.array(putresult),axis=0)
      leftx = leftx + 3*line/2
      lefty = lefty  -math.sqrt(3)*line/2
   
  adjustup = (max([r[0] for r in tmp])/line)*(math.sqrt(3)*line/2)
  leftx = min(r[0] for r in tmp)
  lefty2 = lefty2+ math.sqrt(3)*line
leftx2 = min(r[0] for r in tmp)
lefty2= min(r[1] for r in tmp)- math.sqrt(3)*line


p1 = Polygon( *tmp ) # 凹多角形
polygons = [p1]
#グラフ描画
plt.figure(figsize=(10,10),dpi=97)
plt.axes().set_aspect('equal')
plt.plot()

result = []   
for q in totalresult:   #内外判定
  inout_st1 = p1.encloses_point([q[0],q[1]])
  inout_end1 = p1.encloses_point([q[4],q[5]])
  inout_st2 = p1.encloses_point([q[2],q[3]])
  inout_end2 = p1.encloses_point([q[4],q[5]])
  inout_st3 = p1.encloses_point([q[4],q[5]])
  inout_end3 = p1.encloses_point([q[6],q[7]])

  if inout_st1 == True or inout_end1 == True:
    result.append([q[0],q[1],q[4],q[5]])
    plt.plot(q[0],q[1],marker='.',markersize=3)
    plt.plot(q[4],q[5],marker='.',markersize=3)

  if inout_st2 == True or inout_end2 == True:
    result.append([q[2],q[3],q[4],q[5]])
    plt.plot(q[2],q[3],marker='.',markersize=3)
    plt.plot(q[4],q[5],marker='.',markersize=3)

  if inout_st3 == True or inout_end3 == True:
    result.append([q[4],q[5],q[6],q[7]])
    plt.plot(q[4],q[5],marker='.',markersize=3)
    plt.plot(q[6],q[7],marker='.',markersize=3)

#ポリゴンの描画
for p in polygons :
    tmp = list(map(lambda p:(float(p.x),float(p.y)), p.vertices))
    tmp = plt.Polygon(tmp,fc='red',alpha=0.5)
    plt.gca().add_patch(tmp)
