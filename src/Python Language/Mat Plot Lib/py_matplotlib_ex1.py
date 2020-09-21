#!/bin/python3

"""
Python
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/?ref=lbp

Input:

Output:


"""

# importing the required module 
import matplotlib.pyplot as plt

if __name__ == '__main__':
     
    # x axis values 
    x = [1, 2, 3, 4, 5] 
    # corresponding y axis values 
    y = [2, 1, 4, 3, 5] 
      
    # plotting the points  
    plt.plot(x, y) 
    
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
      
    # giving a title to my graph 
    plt.title('My first graph!') 
      
    # function to show the plot 
    plt.show() 
