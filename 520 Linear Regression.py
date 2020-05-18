# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from ast import literal_eval as make_tuple

def main():
    #determine size of steps to take when finding stationary points
    try:
        lrate = float(input("learning rate: "))
    except:
        print("error, learning rate set to 0.01")
        lrate = 0.01
    
    
    #gather data
    inchecker = 0
    data = []
    candata = [(1,0),(2,2),(3,2),(4,3),(4.5,2)]
    while inchecker == 0:
        imp = input("type 'done' or (x,y) datapoint: ")
        if imp != 'done':
            try:
                if imp[0] == '(' and imp[-1] == ')' and len(imp) > 4:
                    data.append(make_tuple(imp))
                else:
                   print("error, datapoint not recorded")  
            except:
               print("error, datapoint not recorded")                 
        else:
            inchecker = 1
    if len(data) < 2:
        data = candata
        print("invalid dataset, using canned data")
    
    
    cept = 0
    slope = 0
    cond = 0
    while cond < 1:
        returns = costf(data, cept, slope, lrate)
        cept = returns[1]
        slope = returns[2]
        cond = returns[3]
    plot(data,cept,slope)



def plot(data, cept, slope):
        xdata = []
        ydata = []
        yhyp = []
        for i in data:
            xdata.append(i[0])
            ydata.append(i[1])
            yhyp.append(cept + slope * i[0])
        plt.plot(xdata,ydata)
        plt.plot(xdata, yhyp)

    
#cost function to find line of best fit    
def costf(data, cept, slope, lrate):
    cost = 0
    partcept = 0
    partslope = 0
    m = len(data)
    for i in data:
        hyp = cept + slope * i[0]
        cost += (hyp - i[1])**2 / (2*m)
        partcept += (hyp - i[1])/m
        partslope += ((hyp - i[1])*i[0])/m
    cept = cept - partcept * lrate
    slope = slope - partslope * lrate
    cond = 0
    #print(partslope)
    if partslope**2 < .000001 and partcept**2 < .000001:
        cond = 1
         
    returns = [cost, cept, slope, cond]
    return(returns)
        
        


main() 
    
    