from tkinter import *
from matplotlib import pyplot as plt
from math import *
import numpy

def damped_oscillations(m,b,k):
    try:
        x = numpy.linspace(-10,100,1000)
        y = []
        for i in x:
            y.append(e**(-b*i/2*m)*cos(((k/m - (b**2/4*m**2))**(1/2))*i))
        plt.plot(x,y)
        plt.show()
    except:
        x = numpy.linspace(-10,100,1000)
        y = []
        for i in x:
            y.append(e**(-b*i/2*m)*cos(((k/m + (b**2/4*m**2))**0.5)*i))
        plt.plot(x,y)
        plt.show()

def sum_of_sin_wav(number_of_waves):
    a = list()
    w = Toplevel()
    def gra():
        x = numpy.linspace(-10,10,1000)
        y = list()
        y_ = 0
        for i in x:
            for j in a:
                y_ += sin(float(j.get())*2*pi*i)
            y.append(y_)
            y_ = 0
        plt.plot(x,y)
        plt.show()
    for i in range(1,2*number_of_waves,2):
        Label(w,text = f'enter the frequency of {int((i+1)/2)}st function').grid(row = i-1,column = 0)
        e = Entry(w)
        e.grid(row = i,column = 0)
        a.append(e)
    Button(w,text='Graph',command = gra).grid(row = 2*number_of_waves,column = 0)

