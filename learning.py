import tkinter as tk

janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("400x300")

label = tk.Label(janela, text="Olá, mundo!")
label.pack()

janela.mainloop()