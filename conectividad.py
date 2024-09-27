''' Programa que comprueba la conectividad de sitios web. 
Al pasarle una url nos devolvera un codigo de estado HTTP
mediante la funcion .getcode(). Para ello utilizaremos los 
modulos tkinter para la interfaz gráfica yurllib'''

import urllib
import tkinter
from urllib.parse import urlparse


def url_valida(url):
    #funcion para verificar que el formato de la url es correcto
    try:
        resultado=urlparse(url)
        return all([resultado.scheme,resultado.netloc])
    except ValueError:
        return False

def urlTexto():
    #funcion para guardar en una variable el texto
    url= caja_texto.get()
    correcto=url_valida(url)
    print (correcto)
    return url

#creamos la ventana principal
ventana= tkinter.Tk()
ventana.geometry("550x150") #para poner el tamaño de la ventana
ventana.title("Comprobador de conectividad")

#creamos la etiqueta a la izquierda de la caja de texto
etiqueta = tkinter.Label(ventana, text="Introduce una url:")
etiqueta.grid(row=3,column=0,padx=10,pady=10, sticky="e")

#creamos la caja de texto
caja_texto=tkinter.Entry(ventana, width=50)
caja_texto.grid(row=3,column=1,padx=10,pady=10)


boton =tkinter.Button(ventana,text="Comprobar", command=urlTexto)
boton.grid(row=4,column=1,padx=10,pady=10)


ventana.mainloop()