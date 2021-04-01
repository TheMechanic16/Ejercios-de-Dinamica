#!/usr/bin/env python
# coding: utf-8

# # Solución con apoyo visual de Python del ejercicio 11.106 de M.V.
#
# <img src="mecanica vectorial 11-106.png">
#
# Este es un ejercicio de caida libre, que por si no lo saben, es un caso en donde la aceleración en todas las direcciones es constante, por lo tanto sus ecuaciones cinematicas corresponde a las que espuse en la segunda publicación de mi Instagram:
#
# <img src="cinematica acel cosnt.jpg">
#
# Aquí al fin puede verse porque siempre puse las flechas en las ecuaciones, esto indica que son expresiones vectoriales y es valida en todas las direcciones. Para ilustrar esto escribire las ecuaciones de la posición descompuesta en ejes, que a fin de cuentas la posición es lo que me permitira animar la trayectoria:
#
# \begin{equation}
#  \label{eq:posición x}\tag{1}
#  s_{x}=x(t)=x_{0}+v_{0_{x}}*(t-t_{0})+\frac{a_{x}}{2}*(t-t_{0})^2
# \end{equation}
#
# \begin{equation}
#  \label{eq:posición y}\tag{2}
#  s_{y}=y(t)=y_{0}+v_{0_{y}}*(t-t_{0})+\frac{a_{y}}{2}*(t-t_{0})^2
# \end{equation}
#
# Entendiendo que estas son expresiones generales  podemos empezar el codigo importanto las libreria necesarias y definiendo estas como funciones:

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from celluloid import Camera
from math import pi

def pos_x(t):
    x=s0x+v0*np.cos(angOmega)*(t-t0)+(ax/2)*(t-t0)**2
    return x
def pos_y(t):
    y=s0y+v0*np.sin(angOmega)*(t-t0)+(ay/2)*(t-t0)**2
    return y


# Para la solución es totalmente necesario escoger un origen y un sistema de referencía, porque de este dependera la magnitud y dirección de las condiciones iniciales,mi caso lo escogere en el suelo desde donde lanza la jugadora y las direcciones positivas tipicas, osea creciente hacia arriba y a la derecha:
#
# <img src="sistema de referencia y origen escogido.png">
#
# Las condiciones iniciales quedan definidas para este sistema de referencia, aclarando que el cuerpo al que pienso seguir su posición es, logicamente, la pelota:

# In[12]:


t0= 0 # [s] tiempo inicial.
distXTablero=-16 # [ft] distancia x inicial del balon al tablero.
s0x= 0 # [ft] posición inicial x del balon.
s0y= 6.8 # [ft] posición inicial y del balon.
din= 9 # [in] distancia en x del tablero al aro en pulgadas.
d= din*0.0833333 # [ft] distancia en x del tablero al aro.
xf= distXTablero+d # [ft] posición x de la canasta respecto al origen.
yf= 10 # [ft] posición y de la canasta respecto al origen.
ax= 0 # [ft/s2] valor aceleración constante en x.
ay= -32.16 # [ft/s2] valor aceleración constante en y.
angOmega= 150*pi/180 # [°] angulo de la velocidad respecto al eje x en el primer cuadrante.


# La solución del problema se consigue solucionando el sistema de ecuaciones, yo lo hice manualmente y sin tener en cuenta los terminos que se anulaban:
#
# \begin{equation}
#  \label{eq:solución}\tag{3}
#  v_{0}=\sqrt{\frac{a_{y}*x^2}{2*(y-y_{0}-\tan(\theta)*x)*\cos^2(\theta)}}
# \end{equation}
#
# \begin{equation}
#  \label{eq:tiempo final}\tag{4}
#  t=\frac{x}{v_{0}*\cos(\theta)}
# \end{equation}

# In[13]:


v0= np.sqrt((ay*xf**2)/(2*((np.cos(angOmega))**2)*(yf-s0y-np.tan(angOmega)*xf))) # [ft/s] magnitud de la velocidad necesaria para meter el tiro.
tf=xf/(v0*np.cos(angOmega)) # tiempo que tarda el balon en entrar al aro.


# Por ultimo, creamos la animación:

# In[ ]:


fig, axes = plt.subplots()
xdata, ydata = [], []
axes.set_xlim(-18,2)
axes.set_ylim(0, 15)
lab='d='+str(din)+' in'
axes.plot(xdata,label=lab)
axes.legend(loc='upper right')
camera = Camera(fig)
timeSimFin=tf+0.01
numDeImagenes=100
frameps=round(numDeImagenes/(timeSimFin-t0))
time = np.linspace(t0, timeSimFin, numDeImagenes)
for t in time:
    x=pos_x(t)
    y=pos_y(t)
    xdata.append(x)
    ydata.append(y)
    axes.plot(xdata,ydata,color='blue')
    axes.plot(x,y,'o',color='orange')
    canasta=axes.plot([xf-.5,xf+.5],[yf,yf],'r-')
    tablero=axes.plot([distXTablero,distXTablero],[9,11],'r-')
    conexion1=axes.plot([distXTablero,distXTablero+d],[9.3,yf],'r-')
    conexion1=axes.plot([distXTablero,distXTablero+d],[9.6,yf],'r-')
    camera.snap()
animation = camera.animate()
animation.save('tiro_perfecto.gif', fps=100)

# <img src="tiro_perfecto.gif">
