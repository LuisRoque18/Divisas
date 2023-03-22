from tkinter import *
from tkinter import ttk

root=Tk()

#metodo
def Convertir():

    if monedaActual.get()!=Convertirmoneda.get():
        if Convertirmoneda.get()=="MXN":
            if monedaActual.get()=="USD":
                resultado = moneda.get()*19.00
                textoNumeroB.config(text=f'{resultado} MXN')

            if monedaActual.get()=="EUR":
                resultado = moneda.get()*20.29
                textoNumeroB.config(text=f'{resultado} MXN')

        if Convertirmoneda.get()=="USD":

            if monedaActual.get()=="MXN":
                resultado = moneda.get()*0.053
                textoNumeroB.config(text=f'{resultado} USD')
            if monedaActual.get()=="EUR":
                resultado = moneda.get()*1.07
                textoNumeroB.config(text=f'{resultado} USD')

        if Convertirmoneda.get()=="EUR":
            if monedaActual.get()=="MXN":
                resultado = moneda.get()*0.049
                textoNumeroB.config(text=f'{resultado} EUR')

            if monedaActual.get()=="USD":
                resultado = moneda.get()*0.94
                textoNumeroB.config(text=f'{resultado} EUR')
    else:
        textoNumeroB.config(text=f'Verifica lo que introduciste')


moneda = IntVar()
Convertirmoneda = StringVar()
monedaActual = StringVar()

ventanaPrincipal = Frame(root)
ventanaPrincipal.grid()

#titulo de la raiz
titulo = Label(ventanaPrincipal, text="Convertidor de monedas", font=("Roboto",10,))
titulo.grid(row=1, column=1, padx=10, columnspan=2)

#Etiqueta moneda actual
titulo = Label(ventanaPrincipal, text="Cantidad", font=("Roboto",10))
titulo.grid(row=2, column=1, padx=10, pady=10)

textoNumeroA = Entry(ventanaPrincipal, font=("Roboto",10), textvariable=moneda).grid(row=2, column=2, padx=10, pady=10)

#actual
titulo = Label(ventanaPrincipal, text="Moneda de origen", font=("Roboto",10))
titulo.grid(row=3, column=1, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable=monedaActual).grid(row=4, column=1, padx=10, pady=10)

#convertir
titulo = Label(ventanaPrincipal, text="Convertir a:", font=("Roboto",10))
titulo.grid(row=3, column=2, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable = Convertirmoneda).grid(row=4, column=2, padx=10, pady=10)

#etiqueta resultado
titulo = Label(ventanaPrincipal, text="Resultado", font=("Roboto",10))
titulo.grid(row=5, column=1, padx=10, pady=10)

textoNumeroB = Label(ventanaPrincipal, text="", font=("Roboto",10))
textoNumeroB.grid(row=5, column=2, padx=10, pady=10)

#Boton para convertir
botonConvertir = Button(ventanaPrincipal, text="Convertir", font=("Roboto",10), command=Convertir).grid(row=6, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()