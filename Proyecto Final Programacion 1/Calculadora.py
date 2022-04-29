from distutils.command.config import config
from string import hexdigits
from sys import maxsize
import tkinter as tk
from turtle import left, right, width
import sys
from setuptools import Command

#VENTANA
ven=tk.Tk()
ven.title("Calculadora")
ven.geometry("264x400+1000+300")
ven.minsize(width=False,height=False)
ven.maxsize(width=False,height=False)
ven.iconbitmap("Calcul.ico")
ven.config(bg="grey10")

#OPCION DE CERRADO
def cerrar():
    exit=tk.Tk()
    exit.resizable(width=False,height=False)
    exit.title("¿Quieres salir?")
    exit.geometry("264x100+1000+600")
    exit.iconbitmap("Calcul.ico")
    exit.config(background="grey10")

    boton_si=tk.Button(exit,text="Si",#si
    bg="grey3",
    fg="white",
    width=8,
    height=2,
    command=sys.exit)

    boton_si.pack()

    boton_no=tk.Button(exit,#no
    bg="grey3",
    fg="white",
    text="No",
    width=8,
    height=2,
    command=exit.destroy)

    boton_no.pack()


    exit.mainloop()


#MUESTRA DE NUMEROS
M_Muestra=tk.Entry(ven,width=16,foreground="grey37",font=("Helvetica",20))
M_Muestra.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=10,padx=10)


#Funciones de botones
b=0
def boton_pantalla(numeros):
    global b
    M_Muestra.insert(b,numeros)
    b+=1


def resolucion_problemas():
    problemas=M_Muestra.get()
    resultados=eval(problemas)
    M_Muestra.delete(0,tk.END)
    M_Muestra.insert(0,resultados)
    b=0

e=0
def eliminar():
    global e
    M_Muestra.delete(e,tk.END)
    b=0

def eliminar_todo():
    M_Muestra.delete(first=0,last=10)
    return


#BOTONES
Boton0=tk.Button(ven,text="0",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(0))#Numeros
Boton1=tk.Button(ven,text="1",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(1))
Boton2=tk.Button(ven,text="2",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(2))
Boton3=tk.Button(ven,text="3",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(3))
Boton4=tk.Button(ven,text="4",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(4))
Boton5=tk.Button(ven,text="5",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(5))
Boton6=tk.Button(ven,text="6",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(6))
Boton7=tk.Button(ven,text="7",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(7))
Boton8=tk.Button(ven,text="8",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(8))
Boton9=tk.Button(ven,text="9",bg="grey2",fg="white",width=8,height=2,command=lambda: boton_pantalla(9))

Boton_suma=tk.Button(ven,text="+",bg="grey15",fg="white",width=8,height=2,command=lambda: boton_pantalla("+"))#Operadores
Boton_resta=tk.Button(ven,text="-",bg="grey15",fg="white",width=8,height=2,command=lambda: boton_pantalla("-"))
Boton_multi=tk.Button(ven,text="x",bg="grey15",fg="white",width=8,height=2,command=lambda: boton_pantalla("*"))
Boton_divi=tk.Button(ven,text="÷",bg="grey15",fg="white",width=8,height=2,command=lambda: boton_pantalla("/"))

Boton_punto=tk.Button(ven,text="%",bg="grey15",fg="white",width=8,height=2,command=lambda: boton_pantalla("%"))#Otros
Boton_igual=tk.Button(ven,text="=",bg="firebrick1",fg="White",width=8,height=2,command=lambda: resolucion_problemas())

Boton_borrar=tk.Button(ven,text="⌂",bg="grey15",fg="white",width=8,height=2,command=lambda: eliminar())
Boton_allborrar=tk.Button(ven,text="C",bg="grey15",fg="white",width=8,height=2,command=lambda: eliminar_todo())

#Salida
Boton_exit=tk.Button(ven,
    text="EXIT",
    font=("Helvetica",10),
    bg="firebrick1",
    fg="white",
    width=15,
    height=2,
    command=lambda:cerrar())


#MUESTRA DE BOTONES EN VENTANA

Boton1.grid(row=4,column=0,pady=1,padx=0)#Numeros
Boton2.grid(row=4,column=1,pady=1,padx=0)
Boton3.grid(row=4,column=2,pady=1,padx=0)
Boton4.grid(row=3,column=0,pady=1,padx=0)
Boton5.grid(row=3,column=1,pady=1,padx=0)
Boton6.grid(row=3,column=2,pady=1,padx=0)
Boton7.grid(row=2,column=0,pady=1,padx=0)
Boton8.grid(row=2,column=1,pady=1,padx=0)
Boton9.grid(row=2,column=2,pady=1,padx=0)
Boton0.grid(row=5,column=1,pady=1,padx=0)

Boton_suma.grid(row=2,column=3,pady=1,padx=0)#operadores
Boton_resta.grid(row=3,column=3,pady=1,padx=0)
Boton_multi.grid(row=4,column=3,pady=1,padx=0)
Boton_divi.grid(row=5,column=2,pady=1,padx=0)


Boton_punto.grid(row=5,column=0,pady=1,padx=0)#Otros
Boton_igual.grid(row=5,column=3,pady=1,padx=0)

Boton_borrar.grid(row=1,column=2,columnspan=1,pady=1,padx=0)
Boton_allborrar.grid(row=1,column=3,columnspan=2,pady=1,padx=0)

Boton_exit.grid(row=7,column=1,columnspan=2,pady=1,padx=0)#Salida



ven.mainloop()