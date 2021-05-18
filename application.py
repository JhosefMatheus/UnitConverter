from tkinter import *

window = Tk()

w = 650
h = 300

w_screen = window.winfo_screenwidth()
h_screen = window.winfo_screenheight()

position_x = (w_screen/2) - (w/2)
position_y = (h_screen/2) - (h/2)

window.geometry(f'{w}x{h}+{int(position_x)}+{int(position_y)}')
window.configure(
    background='gray'
)
window.resizable(False, False)

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

options_drop_down_2 = [
    'Quilômetro',
    'Metro',
    'Centímetro',
    'Milímetro',
    'Micrômetro',
    'Nanômetro',
    'Milha',
    'Jarda',
    'Pé',
    'Polegada',
    'Milha náutica'
]
default_drop_down_2 = options_drop_down_2[1]
stringVar_drop_down_2 = StringVar(window)
stringVar_drop_down_2.set(default_drop_down_2)
drop_down_2 = OptionMenu(
    window,
    stringVar_drop_down_2,
    *options_drop_down_2
)

options_drop_down_3 = [
    'Quilômetro',
    'Metro',
    'Centímetro',
    'Milímetro',
    'Micrômetro',
    'Nanômetro',
    'Milha',
    'Jarda',
    'Pé',
    'Polegada',
    'Milha náutica'
]
default_drop_down_3 = options_drop_down_3[1]
stringVar_drop_down_3 = StringVar(window)
stringVar_drop_down_3.set(default_drop_down_3)
drop_down_3 = OptionMenu(
    window,
    stringVar_drop_down_3,
    *options_drop_down_3
)

entry = Entry(
    window,
    width=19,
    font='Arial 19'
)

label_result = Label(
    window,
    font='Arial 18',
    width=19
)

label_equal = Label(
    window,
    text='=',
    font='Arial 20',
    width=5,
    bg='gray'
)

drop_down_1['width'] = w
drop_down_1['font'] = 'Arial 20'
drop_down_1['anchor'] = 'w'

drop_down_2['width'] = 15
drop_down_2['font'] = 'Arial 20'
drop_down_2['anchor'] = 'w'

drop_down_3['width'] = 15
drop_down_3['font'] = 'Arial 20'
drop_down_3['anchor'] = 'w'

drop_down_1.pack()
drop_down_2.place(x=7, y=150)
drop_down_3.place(x=375, y=150)
entry.place(x=7, y=110)
label_result.place(x=375, y=110)
label_equal.place(x=283, y=153)

window.mainloop()
