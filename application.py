from tkinter import *
from tkinter import ttk
from Converter import *

converter = Converter()

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


def change_options_menu(event):
    converter.change_options_menu(drop_down_1, drop_down_2, drop_down_3)


def change_label_formula_text(event):
    converter.change_label_formula_text(
        label_formula, drop_down_2, drop_down_3)


options_drop_down_1 = [
    'Armazenamento de Dados',
    'Comprimento',
    'Consumo de Combustível',
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
drop_down_1 = ttk.Combobox(
    window,
    values=options_drop_down_1
)

drop_down_1['width'] = w
drop_down_1['font'] = 'Arial 20'
drop_down_1.current(1)
drop_down_1.bind('<<ComboboxSelected>>', change_options_menu)

options_drop_down_2 = converter.options_comprimento
drop_down_2 = ttk.Combobox(
    window,
    values=options_drop_down_2
)

drop_down_2['width'] = 15
drop_down_2['font'] = 'Arial 20'
drop_down_2.current(0)
drop_down_2.bind('<<ComboboxSelected>>', change_label_formula_text)

options_drop_down_3 = converter.options_comprimento
drop_down_3 = ttk.Combobox(
    window,
    values=options_drop_down_3
)

drop_down_3['width'] = 15
drop_down_3['font'] = 'Arial 20'
drop_down_3.current(0)
drop_down_3.bind('<<ComboboxSelected>>', change_label_formula_text)


entry = Entry(
    window,
    width=17,
    font='Arial 19'
)

label_result = Label(
    window,
    font='Arial 18',
    width=17
)

label_equal = Label(
    window,
    text='=',
    font='Arial 20',
    width=5,
    bg='gray'
)

label_formula = Label(
    window,
    font='Arial 20',
    bg='gray',
    text='Fórmula:'
)

drop_down_1.pack()
drop_down_2.place(x=7, y=150)
drop_down_3.place(x=375, y=150)
entry.place(x=7, y=110)
label_result.place(x=375, y=110)
label_equal.place(x=283, y=153)
label_formula.place(x=7, y=240)

window.mainloop()
