#from pyparsing.helpers import string_end
#from IPython.utils.tempdir import TemporaryDirectory
#from matplotlib.projections import ProjectionRegistry
#from sympy.geometry import *
#import matplotlib.pyplot as plt
#import numpy as np
#import csv
#%matplotlib inline

# ポリゴン（多角形）の生成

tmp = np.array([[1,4],[4,6],[5,4],[5,7],[1,7]])
#tmp = np.array([[5,1.1],[5.23,6.16],[10.003,5.92],[10.6,11.2],[6.13,11.99],[5.5,9.4],[1.6,9.2],[3.14,17.21],[16.543,14.123],[14.99,0.625]])

p1 = Polygon( *tmp ) # 凹多角形
polygons = [p1]

#ポリゴンの重点座標
total = 0 
for onepoint in tmp:
  total = total + onepoint
average = total/len(tmp)
centerX = average[0]
centerY = average[1]
center = [centerX,centerY]

#正方形の座標縦向き
#重点よりX座標がプラスの時
pointx = centerX
pointy = centerY
allpoint = []
st_end1 = []
st_end2 = np.empty((0,4))
line = 1 #一辺の長さ

while  pointx < max([r[0] for r in tmp]) + line :
  while pointy < max([r[1] for r in tmp]) :
    allpoint.append([pointx,pointy])
    st = np.array([pointx,pointy]).reshape(2,1)
    pointy = pointy + line
    end = np.array([pointx,pointy]).reshape(2,1)
    st_end1= np.append(st, end)
    st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
  
  pointy = centerY
  #while pointy > min([r[1] for r in tmp]) - line :
  while  pointy > min([r[1] for r in tmp])  :
    allpoint.append([pointx,pointy])
    st = np.array([pointx,pointy]).reshape(2,1)
    pointy = pointy - line
    end = np.array([pointx,pointy]).reshape(2,1)
    st_end1= np.append(st, end)
    st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
  pointy = centerY
  pointx = pointx +  line
#print(st_end2)
#重点よりx座標がマイナスの時
pointx = centerX - line
pointy = centerY
while  pointx > min([r[0] for r in tmp]) - line :
  while pointy < max([r[1] for r in tmp]):
    allpoint.append([pointx,pointy])
    st = np.array([pointx,pointy]).reshape(2,1)
    pointy = pointy + line
    end = np.array([pointx,pointy]).reshape(2,1)
    st_end1= np.append(st, end)
    st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
  pointy = centerY - line
  pointy = centerY
  while  min([r[1] for r in tmp]) < pointy:
    allpoint.append([pointx,pointy])
    st = np.array([pointx,pointy]).reshape(2,1)
    pointy = pointy - line
    end = np.array([pointx,pointy]).reshape(2,1)
    st_end1= np.append(st, end)
    st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
  pointy = centerY
  pointx = pointx -  line

#test = p1.encloses_point(center) #内外判定
#正方形の座標横向き
pointx = centerX
pointy = centerY
while  pointy < max([r[1] for r in tmp]) + line :
   while  pointx < max([r[0] for r in tmp]):
     st = np.array([pointx,pointy]).reshape(2,1)
     pointx = pointx + line
     end = np.array([pointx,pointy]).reshape(2,1)
     st_end1= np.append(st, end)
     st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
   pointx = centerX
  #while pointy > min([r[1] for r in tmp]) - line :
   while  pointx > min([r[0] for r in tmp])  :
     st = np.array([pointx,pointy]).reshape(2,1)
     pointx = pointx - line
     end = np.array([pointx,pointy]).reshape(2,1)
     st_end1= np.append(st, end)
     st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
   pointx = centerX
   pointy = pointy +  line
#print(st_end2)
#重点よりy座標がマイナスの時
pointy = centerY - line
pointx = centerX
while  pointy > min([r[1] for r in tmp]) - line :
  while pointx < max([r[0] for r in tmp]):
    st = np.array([pointx,pointy]).reshape(2,1)
    pointx = pointx + line
    end = np.array([pointx,pointy]).reshape(2,1)
    st_end1= np.append(st, end)
    st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
  pointx = centerX - line
  pointx = centerX
  while  min([r[0] for r in tmp]) < pointx:
    st = np.array([pointx,pointy]).reshape(2,1)
    pointx = pointx - line
    end = np.array([pointx,pointy]).reshape(2,1)
    st_end1= np.append(st, end)
    print(st_end1)
    st_end2= np.append(st_end2,np.array([st_end1]),axis=0)
   # print(st_end2)
  pointx = centerX
  pointy = pointy -  line

#グラフ描画
plt.figure(figsize=(5,5),dpi=96)
plt.plot(centerX,centerY,marker='.',markersize=20) #ポリゴン重点座標

#ポリゴンの描画
for p in polygons :
    tmp = list(map(lambda p:(float(p.x),float(p.y)), p.vertices))
    tmp = plt.Polygon(tmp,fc='red',alpha=0.5)
    plt.gca().add_patch(tmp)
#正方形の座標描画 
result = []   
for q in st_end2:   #内外判定
  inout_st = p1.encloses_point([q[0],q[1]])
  inout_end = p1.encloses_point([q[2],q[3]])
  if inout_st == True or inout_end == True:
    result.append([q[0],q[1],q[2],q[3]])
    plt.plot(q[0],q[1],marker='.',markersize=20)
    plt.plot(q[2],q[3],marker='.',markersize=20)
print(len(result))  

#CSVへの書き出し
f = open('out2.csv', 'w', newline='')
data = [result]
writer = csv.writer(f)
writer.writerows(data)
f.close()
