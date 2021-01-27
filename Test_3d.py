import numpy as np
import matplotlib.pyplot as plt
#import functions tools3D
import tools3d as tools

#---Coordenadas
xg=[]
yg=[]
zg=[]

#----Centro
xc = 80
yc = 40
zc = 40

#----Coordinates locales
x=[40, 30, 80, 75]
y=[60, 10, 60, 45]
z=[ 0,  0,  0,  0]

for i in range(len(x)):
    xg.append(x[i] + xc)
    yg.append(y[i] + yc)
    zg.append(z[i] + zc)

def plotPlaneLine(xg,yg,zg):
    plt.axis([50,250,150,0])
    plt.grid()
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    plt.scatter(xg[3],yg[3],s=20,color='r')

    #----interseccion de los triangulos 
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='r',linestyle=':')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='r',linestyle=':')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='r',linestyle=':')

    plt.gca().set_aspect('equal')
    plt.show()

def hitPoint(x,y,z):
    #Distance point(0,1)
    a = x[1]-x[0]
    b = y[1]-y[0]
    c = z[1]-z[0]
    Q01 = np.sqrt(a*a+b*b+c*c)

    #Distancia del punto(1,2)
    a = x[2]-x[1]
    b = y[2]-y[1]
    c = z[2]-z[1]
    Q12 = np.sqrt(a*a+b*b+c*c)
   
    #Distancia del punto(0,2)
    a = x[2]-x[0]
    b = y[2]-y[0]
    c = z[2]-z[0]
    Q02 = np.sqrt(a*a+b*b+c*c)
    
    #Third point of the triangle
    #Distancia del punto(1,3)
    a = x[3]-x[1]
    b = y[3]-y[1]
    c = z[3]-z[1]
    Q13 = np.sqrt(a*a+b*b+c*c)
    #Distance point(2,3)
    a = x[2]-x[3]
    b = y[2]-y[3]
    c = z[2]-z[3]
    Q23 = np.sqrt(a*a+b*b+c*c)
    #Distance point(0,3)
    a = x[0]-x[3]
    b = y[0]-y[3]
    c = z[0]-z[3]
    Q03 = np.sqrt(a*a+b*b+c*c)
    #Area triangle A
    s = (Q01+Q12+Q02)/2
    A = np.sqrt(s * (s-Q01) * (s-Q12) * (s*Q02))
    #Area triangle A1
    s1 = (Q01 + Q03 + Q13) /2
    A1 = np.sqrt(s1*(s1-Q01) * (s1-Q03) * (s1-Q13))
    #Area triangle A2
    s2 = (Q02 + Q23 + Q03) /2
    A2 = np.sqrt(s2 * (s2-Q02) * (s2-Q23) * (s1-Q03))

    return A,A1,A2
    

def plotSquareLinex(xc,yc,zc):
    [A,A1,A2]=hitPoint(x,y,z)
    print('A=',A)
    print('A1=',A1)
    print('A2=',A2)
    print ('A1+A2',(A1+A2))
    if((A1+A2)>A):
        plt.text(170,60,'El HIT PONT esta fuera de los limites')
    elif((A1+A2)<A):
        plt.text(180,60,'El HIT PONT esta dentro del hoyo')
    
    plotPlaneLine(xg,yg,zg)


#Pedir num control
while True:
    enter=input('donde esta el histpoint en "x"? o Ingrese se numero de control para salir (18390045)')
    if enter=='18390045':
        break
    else:
        
        x[3]=int(enter)
        enter=input('donde esta el histpoint en "y"? o Ingrese se numero de control para salir (18390045)')
        if enter=='18390031':
            break
        else:
            y[3]=int(enter)

            for i in range(len(x)):
                xg.append( x[i]+xc )
                yg.append( y[i]+yc )
                zg.append( z[i]+zc )

            plotSquareLinex(xc,yc,zc)