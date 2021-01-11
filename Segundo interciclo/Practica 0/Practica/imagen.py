# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:55:21 2021

@author: christian Hernandez
"""
############################################################################################
from matplotlib import pyplot as plt
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import DoubleVar
from tkinter import Canvas
from tkinter import IntVar
from tkinter import Label
from tkinter import Menu
from tkinter import Tk
from tkinter import NW
from PIL import Image
from time import time
import numpy as np
import numpy
import cv2
############################################################################################
############################################################################################
def abrir():
    varios=85#declaracion de variables
    promedio=0#declaracion de variables
    tiempo_inicial = time() #inicia el tiempo para calcular 
    ventana.filename = filedialog.askopenfilename(initialdir = 'C:/Users/chris/OneDrive/Desktop/Procemiento/imagenes',
    title = "Elige Tu Archivo De Imagen:", 
    filetypes = (("Imagenes PNG", "*.png"),("Imagenes GIF ", "*.gif"))) # creamos un ventana y podemos escojerla ruta
    global ruta#inicialimos la variable global
    ruta = ventana.filename
    imagenL = PhotoImage(file = ruta)#la ruta le pasamos a un imagen
    global abrirImagen#inicialimos la variable global
    abrirImagen = canvas.create_image(100, 150, anchor=NW, image=imagenL)#Abrimos las ventanas
    ventana.mainloop()#visualizamos la ventan
    tiempo_final = time()#caculamos el tiempo final
    tiempo_ejecucion = tiempo_final - tiempo_inicial#calculamos el tiempo
    
    print('*******************************************************************************')
    print('*******************************************************************************')
    print('El tiempo de ejecucion promedio una imagen a color :',tiempo_ejecucion ) #En segundos
    promedio=tiempo_ejecucion*varios#sacamos el promedio de todas la imagenes
    print('El tiempo de ejecucion las images totales color:',promedio )
  
     
############################################################################################
############################################################################################
def grises():
    varios1=85# declamos la variables
    promedio1=0# declamos la variables
    tiempo_inicial1 = time() #inicia el tiempo para calcular 
    im = Image.open(ruta)#la imagen de fue abierta la original y se guarda de formayo gif la recuperamos para poder realizar el proceso
    im2 = im
    i = 0
    while i < im2.size[0]:#aplicamos una condiccion 
        j = 0#declaracion de variables
        while j < im2.size[1]:#aplicamos una condiccion
            r, g, b = im2.getpixel((i, j))#realizamos rl proceso de convertir
            g = (r + g + b) / 3#realizamos rl proceso de convertir
            gris = int(g)#realizamos rl proceso de convertir
            pixel = tuple([gris, gris, gris])#realizamos rl proceso de convertir
            im2.putpixel((i, j), pixel)#realizamos rl proceso de convertir
            j+=1
        i+=1
    g = im2.convert('L')
    g.save('C:/Users/chris/OneDrive/Desktop/Procemiento/resultados/grises.gif') #gurdarnamso la imagen que fur procesda
    imagenL = PhotoImage(file = 'C:/Users/chris/OneDrive/Desktop/Procemiento/resultados/grises.gif')#gurdarnamso la imagen que fur procesda
    global grisesito#declaracion de variable
    grisesito = canvas.create_image(500, 150, anchor=NW, image=imagenL)
    ventana.mainloop()#abrimos la ventana
    tiempo_final1 = time() #caculamos el tiempo final
    tiempo_ejecucion1 = tiempo_final1 - tiempo_inicial1#calculamos el tiempo
    print('El tiempo de ejecucion promedio una imagen a griss :',tiempo_ejecucion1 ) #calculamos el tiempo
    promedio1=tiempo_ejecucion1*varios1#sacamos el promedio de todas la imagenes
    print('El tiempo de ejecucion las images totales griss:',promedio1 )#calculamos el promedio
############################################################################################
############################################################################################
def histograma():
    im = Image.open("C:/Users/chris/OneDrive/Desktop/Procemiento/resultados/grises.gif")#Abrimos la imagen 
    im16 = im#declaramos las variblas
    [ren, col] = im16.size#sacamso el tamanio 
    total = ren * col#realizamo la multimplicacion
    
    a = np.asarray(im16, dtype = np.float32)#agregramos un array
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)#sacamos los valores maximo
    valor = 0
    maxd = max(a)
    grises = maxd
    vec=np.zeros(grises + 1)#Devuelve una nueva matriz de forma y tipo dados, llena de ceros.
    for i in range(total - 1):#declaramos el for y inicializamos el rango
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.plot(vec)#graficamos 
    plt.savefig('C:/Users/chris/OneDrive/Desktop/Procemiento/resultados/histograma.png', dpi=80)
    imagenL = PhotoImage(file = 'C:/Users/chris/OneDrive/Desktop/Procemiento/resultados/histograma.png')
    global hist#declaracion de variale
    hist = canvas.create_image(280, 355, anchor=NW, image=imagenL)
    ventana.mainloop()
############################################################################################   
############################################################################################    
def histogramaori():
   img = cv2.imread('C:/Users/chris/OneDrive/Desktop/Procemiento/imagenes/15.png',0)#abrimos la imagen de que fe guardar con aterioridad
   plt.hist(img.ravel(),256,[0,256])#realizamos la grafica
   plt.savefig('C:/Users/chris/OneDrive/Desktop/Procemiento/propios/histogramas.png', dpi=80)#guardamos la inagemn
   imagenL1 = PhotoImage(file = 'C:/Users/chris/OneDrive/Desktop/Procemiento/propios/histogramas.png')
   global hist1#declaracion de varibles
   hist1 = canvas.create_image(280, 355, anchor=NW, image=imagenL1)
   ventana.mainloop()#visualizamo sl imgane
    
############################################################################################
############################################################################################
def limpiar():
    canvas.delete("all")
############################################################################################
"""Creacion De Ventana Y Lienzo (Canvas)"""
ventana = Tk()
w = 1000
h = 1000
extraW=ventana.winfo_screenwidth() - w
extraH=ventana.winfo_screenheight() - h
ventana.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
canvas = Canvas(ventana, width=1000, height=650)
canvas.pack()
ventana.title(" IMAGENES")
entrada = IntVar()
entrada2 = DoubleVar()
Label(text = "Imagen Original ", font= ("Times New Roman",14)).place(x=700, y=120)
Label(text = "Imagen Procesada ", font= ("Times New Roman",14)).place(x=1100, y=120)
############################################################################################
"""Creacion De Los Menus"""
barraMenu = Menu(ventana)
mnuOpciones = Menu(barraMenu)
mnuUnidad1 = Menu(barraMenu)
mnuUnidad2 = Menu(barraMenu)
############################################################################################
"""Menu  I"""
mnuUnidad1.add_command(label = "ABRIR IMAGEN", command = abrir)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "ESCALA DE GRISES", command = grises)
mnuUnidad1.add_separator()
############################################################################################
"""Menu  II"""
mnuUnidad2.add_command(label = "HISTOGRAMA ORIGINAL", command = histogramaori)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "HISTOGRAMA PROCESADO", command = histograma)
mnuUnidad2.add_separator()
############################################################################################
"""Menu Opciones"""
mnuOpciones.add_command(label = "LIMPIAR", command = limpiar)
mnuOpciones.add_separator()
mnuOpciones.add_command(label = "SALIR", command = ventana.destroy)
############################################################################################
barraMenu.add_cascade(label = "Grises", menu = mnuUnidad1)
barraMenu.add_cascade(label = "Histograma", menu = mnuUnidad2)
barraMenu.add_cascade(label = "Salir", menu = mnuOpciones)
ventana.config(menu = barraMenu)
ventana.mainloop()
############################################################################################  