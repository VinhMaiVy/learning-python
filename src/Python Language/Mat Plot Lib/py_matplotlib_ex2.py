#!/bin/python3

"""
Python
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/?ref=lbp

Input:

Output:


"""

 
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':  

    # x axis values
    x1 = [1, 2, 3, 4, 5]    
    x = np.asarray(x1).reshape(-1, 1)
    
    # corresponding y axis values
    y1 = [2, 1, 4, 3, 5]
    y = y1
    
    n = len(x)
    
    # plotting the line 1 points  
    # plt.plot(x1, y1, label = "line 1") 
    # plotting the points  
    plt.plot(x1, y1, color='green', linewidth = 2, 
         marker='o', markerfacecolor='blue', markersize=12) 

    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    a = lm.intercept_
    b = lm.coef_[0]
    
    # line 2 points 
    x2 = [i for i in range(1, n+1)]
    y2 = [a + b*i for i in range(1, n+1)]
     
    # plotting the line 2 points  
    #plt.plot(x2, y2, label = "line 2")
    plt.plot(x2, y2, color='red') 
    
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
    # giving a title to my graph 
    plt.title('Two lines on same graph!') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 