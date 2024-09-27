''' Programa que comprueba la conectividad de sitios web. 
Al pasarle una url nos devolvera un codigo de estado HTTP
mediante la funcion .getcode(). Para ello utilizaremos los 
modulos tkinter para la interfaz gráfica yurllib'''

from urllib import request
from urllib.error import URLError,HTTPError
import tkinter as tk


def comprobar_conectividad(): 
#funcion para comprobar la conectividad y devolver el resultado para mostrarlo en una etiqueta

    #guardamos el contenido de la caja de texto en la variable
    url=caja_texto.get()

    try:
        respuesta=request.urlopen(url) 
        codigo_estado=respuesta.getcode()

        if codigo_estado==200:
            resultado_label.config(text=f"El sitio {url} está disponible (Código: {codigo_estado})", fg="green")
        else:
            resultado_label.config(text=f"El sitio {url} no está disponible (Código: {codigo_estado})", fg="red")
    
    except HTTPError as e:
        resultado_label.config(f"Error HTTP: {e.code} para la url {url}", fg="red")
    except URLError as e:
        resultado_label.config(f"URL no válida o no disponible: {e.reason}", fg="red")
    except ValueError:
        resultado_label.config(text="Por favor introduce una URL válida.", bg="red")


                

    
'''
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
    if correcto:
            codigo=conectividad(url)
    else:
         codigo=conectividad(url)
    print(codigo)
    return url

def conectividad(url):
    #funcion para comprobar si la web tiene conectividad
    conec= urllib.request.urlopen(url)
    return conec.getcode()
'''
#creamos la ventana principal
ventana= tk.Tk()
ventana.geometry("550x150") #para poner el tamaño de la ventana
ventana.title("Comprobador de conectividad")

#creamos la etiqueta a la izquierda de la caja de texto
etiqueta = tk.Label(ventana, text="Introduce una url:")
etiqueta.grid(row=3,column=0,padx=10,pady=10, sticky="e")

#creamos la caja de texto
caja_texto=tk.Entry(ventana, width=50)
caja_texto.grid(row=3,column=1,padx=10,pady=10)

#creamos el boton para comprobar la conectividad
boton =tk.Button(ventana,text="Comprobar", command=comprobar_conectividad)
boton.grid(row=4,column=1,padx=10,pady=10)

#creamos una etiqueta para mostrar los resultados
resultado_label=tk.Label(ventana,text="",wraplength=300)
resultado_label.grid(row=5, column=1,columnspan=2,padx=10,pady=10)

#mantiene la ejecucion de la ventana
ventana.mainloop()