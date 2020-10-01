from tkinter import *

ventana = Tk()
ventana.title("Mi ventana")
ventana.geometry("800x600")

etiqueta = Label(ventana, text="Esto es una etiqueta")
etiqueta.pack()

SegundaEtiqueta = Label(ventana, text="Segunda Ventana")
SegundaEtiqueta.pack()

ingresoTexto = Entry(ventana)
ingresoTexto.pack()

Button = Button(ventana, text="Mi botón")
Button.pack()


ventana.mainloop()
