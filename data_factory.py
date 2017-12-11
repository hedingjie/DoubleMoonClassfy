# encoding:utf8
import numpy as np
import math
import random
import matplotlib.pyplot as plt


class DataFactory(object):
    """用于产生数据的对象"""
    def __init__(self):
        super(DataFactory,self).__init__()
        
    def generateUpData(self,n,r,w,d):
        theta=np.random.rand(n)*180
        w_=np.random.rand(n)*w
        length=[(r+w_i) for w_i in w_]
        x_up=[l*math.cos(math.radians(angle) ) for l,angle in zip(length,theta)]
        y_up=[l*math.sin(math.radians(angle) ) for l,angle in zip(length,theta)]
        
        inputs=[]
        inputs.extend([[x_up[i],y_up[i],1] for i in xrange(n) ])
        return inputs
    
    def generateDownData(self,n,r,w,d):
        theta=np.random.rand(n)*(-180)
        w_=np.random.rand(n)*w
        length=[(r+w_i) for w_i in w_]
        x_up=[l*math.cos(math.radians(angle) )+r for l,angle in zip(length,theta)]
        y_up=[l*math.sin(math.radians(angle) )-d for l,angle in zip(length,theta)]
        
        inputs=[]
        inputs.extend([[x_up[i],y_up[i],-1] for i in xrange(n) ])
        return inputs        
    
    def generateData(self,n,r,w,d):
        """用于产生双半月型数据"""
        theta1=np.random.random(n)*180
        theta2=np.random.random(n)*(-180)
        
        xa=[(np.random.random(1)*w+r)*math.cos(angle) for angle in theta1]
        ya=[(np.random.random(1)*w+r)*math.sin(angle) for angle in theta1]
        
        xb=[(np.random.random(1)*w+r)*math.cos(angle)+r for angle in theta2]
        yb=[(np.random.random(1)*w+r)*math.sin(angle) for angle in theta1]
        
        inputs=[]
        
        inputs.extend([xa[i],ya[i],1] for i in xrange(n))
        inputs.extend([xb[i],yb[i],-1] for i in xrange(n))
        return inputs
    
if __name__=='__main__':
    data=DataFactory()
    upsets=data.generateUpData(100, 5, 2, -2)
    downsets=data.generateDownData(100,5,2,-2)
    sets=upsets+downsets
    print sets

    for point in sets:
        if point[2]==1:
            plt.plot(point[0],point[1],'ob')
        else:
            plt.plot(point[0],point[1],'or')
    
    plt.show()