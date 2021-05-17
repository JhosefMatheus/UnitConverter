from tkinter import *

window = Tk()

window.geometry("650x300")
window.configure(
    background='gray'
)

options_drop_down_1 = [
    'Armazenamento de Dados',
    'Comprimento',
    'Consumo de Energia',
    'Energia Mecânica',
    'Frequência',
    'Massa',
    'Pressão',
    'Temperatura',
    'Tempo',
    'Transmissão de dados',
    'Velocidade',
    'Volume',
    'Área',
    'Ângulo'
]
default_drop_down_1 = options_drop_down_1[1]
stringVar_drop_down_1 = StringVar(window)
stringVar_drop_down_1.set(default_drop_down_1)
drop_down_1 = OptionMenu(
    window,
    stringVar_drop_down_1,
    *options_drop_down_1
)

drop_down_1.pack()

window.mainloop()
