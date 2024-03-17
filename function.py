import math
import matplotlib.pyplot as plt
import time as t
import numpy as np
import pygame
x = []
y = []

A = 1.3
B = 0
C = -1.2

def function(x):
    fx = A*math.pow(x,3) + B*math.pow(x,2) + C*x
    return fx

def generate_table(start, end, step):
    i = start
    while i <= end:
        x.append(i)
        y.append(function(i))
        i+=step

def initial_points(x,y,x_size,y_size,trans_size,start):
    new_x = x[(start+trans_size)//2]
    new_y = y[(start+trans_size)//2]
    x_transformed = []
    y_transformed = []
    ratio_x = (x_size/2) - new_x
    ratio_y = (y_size/2) - new_y
    for i in range (0,len(x)):
        x_transformed.append(x[i]+ratio_x)
        y_transformed.append(y[i]+ratio_y)
    x_f=[]
    y_f=[]
    # y_f = [0 for i in range(trans_size+1)]
    print()

    # for i in range(0,trans_size//2):
    #      x_f.append(((x_size//2)*(x_transformed[i]-x_transformed[0]))/(x_transformed[trans_size//2]-x_transformed[0]))

    # for i in range(trans_size//2,trans_size+1):
    #     x_f.append(((x_size-(x_size//2))*(x_transformed[i]-x_transformed[trans_size//2])/(x_transformed[trans_size]-x_transformed[trans_size//2]))+640)
    
    # for i in range(0,trans_size+1):
    #     if y_transformed[i] >= 360:
    #         y_f[i]=((((y_size-(y_size//2))*(y_transformed[i]-y_transformed[trans_size//2]))/(max(y_transformed)-360))+360)
    #     else:
    #         y_f[i]=((((y_size//2)*(y_transformed[i]-min(y_transformed)))/(360-min(y_transformed))))
    ploting(x_transformed,y_transformed)
    

    
    

def ploting(x,y):

    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(x, y)

    # Set the limits of the x and y axes
    ax.set_xlim([0, 1280])
    ax.set_ylim([0, 720])

    plt.show()

def main():
    try:
        end = -B + math.sqrt(B**2 - 4*A*C) / (2*A)
        start = -B - math.sqrt(B**2 - 4*A*C) / (2*A)
    except: 
        print("Error")
    trans_size = 10000
    generate_table(start, end, (end-start)/trans_size)
    #ploting(np.dot(x,100),np.dot(y,100))
    # plt.plot(x,y)
    # plt.show()

    initial_points(np.dot(x,1000),np.dot(y,1000),1280,720,int(trans_size*.1),2000)

    
    

    

if __name__ == "__main__":
    main()