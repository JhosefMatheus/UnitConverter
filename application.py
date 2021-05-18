from tkinter import *
import tkinter as tk

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

options_armazenamento_de_dados = [
            'Bit',
            'Kilobit',
            'Kibibit',
            'Megabit',
            'Megbibit',
            'Gigabit',
            'Gibibit',
            'Terabit',
            'Tebibit',
            'Petabit',
            'Pebibit',
            'Byte',
            'Kilobyte',
            'Kibibyte',
            'Megabyte',
            'MebiByte',
            'Gigabyte',
            'Gibibyte',
            'Terabyte',
            'Tebibyte',
            'Petabyte',
            'Pebibyte'
        ]

options_comprimento = [
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

options_consumo_de_combustivel = [
            'Milha por galão americano',
            'Milha por galão imperial',
            'Quilômetro por litro',
            'Litro por 100 quilômetros'
        ]

options_energia_mecanica = [
            'Joule',
            'Quilojoule',
            'Gram calorie',
            'Quilocaloria',
            'Watt-hora',
            'Quilowatt-hora',
            'Elétron-volt',
            'BTU',
            'therm (US)',
            'Pé-libra força'
        ]

options_frequencia = [
            'Hertz',
            'Quilo-hertz',
            'Mega-hertz',
            'Giga-hertz'
        ]

options_massa = [
            'Tonelada',
            'Quilograma',
            'Grama',
            'Miligrama',
            'Micrograma',
            'Tonelada de deslocamento',
            'Tonelada curta',
            'Stone',
            'Libra',
            'Onça'
        ]

options_pressao = [
            'Atmosfera padrão',
            'Bar',
            'Pascal',
            'Psi',
            'Torr'
        ]

options_temperatura = [
            'Grau Celsius',
            'Grau Fahrenheit',
            'Kelvin'
        ]

options_tempo = [
            'Nanosegundo',
            'Microssegundo',
            'Milissegundo',
            'Segundo',
            'Minuto',
            'Hora',
            'Dia',
            'Semana',
            'Mês',
            'Ano-calendário',
            'Década',
            'Século'
        ]

options_transmissao_de_dados = [
            'Bit por segundo',
            'Quilobit por segundo',
            'Quilobyte por segundo',
            'Kibibit por segundo',
            'Megabit por segundo',
            'Megabyte por segundo',
            'Mebibit por segundo',
            'Gigabit por segundo',
            'Gigabyte por segundo',
            'Gibibit por segundo',
            'Terabit por segundo',
            'Terabyte por segundo',
            'Tebibit por segundo'
        ]

options_velocidade = [
            'Milha por hora',
            'Pés por segundo',
            'Metro por segundo',
            'Quilômetro por hora',
            'Nó'
        ]

options_volume = [
            'Galão americano',
            'Quarto líquido americano',
            'Pinta americana',
            'Copo',
            'Onça líquida americana',
            'Colher de sopa americana',
            'Colher de chá americana',
            'Metro cúbico',
            'Litro',
            'Mililitro',
            'Galão imperial',
            'Quarto imperial',
            'Pinto imperial',
            'Xícara imperial',
            'Onça líquida imperial',
            'Colher de sopa imperial',
            'Colher de chá imperial',
            'Pé cúbico',
            'Polegada cúbica'
        ]

options_area = [
            'Quilômetro quadrado',
            'Metro quadrado',
            'Milha quadrada',
            'Jarda quadrada',
            'Pé quadrado',
            'Polegada quadrada',
            'Hectare',
            'Acre'
        ]

options_angulo = [
            'Grado',
            'Grau',
            'Mil angular',
            'Minuto de arco',
            'Radiano',
            'Segundo de arco'
        ]

def change_options_menu(event):
    atual_option = stringVar_drop_down_1.get()

    if atual_option == options_drop_down_1[0]:

        stringVar_drop_down_2.set('Byte')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_armazenamento_de_dados:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Byte')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_armazenamento_de_dados:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[1]:
        
        stringVar_drop_down_2.set('Metro')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_comprimento:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Metro')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_comprimento:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[2]:
        
        stringVar_drop_down_2.set('Quilômetro por litro')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_consumo_de_combustivel:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Quilômetro por litro')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_consumo_de_combustivel:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[3]:
        
        stringVar_drop_down_2.set('Joule')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_energia_mecanica:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Joule')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_energia_mecanica:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[4]:
        
        stringVar_drop_down_2.set('Hertz')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_frequencia:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Hertz')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_frequencia:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[5]:
        
        stringVar_drop_down_2.set('Quilograma')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_massa:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Quilograma')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_massa:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[6]:
        
        stringVar_drop_down_2.set('Pascal')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_pressao:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Pascal')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_pressao:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[7]:
        
        stringVar_drop_down_2.set('Grau Celsius')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_temperatura:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Grau Celsius')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_temperatura:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))
    
    elif atual_option == options_drop_down_1[8]:

        stringVar_drop_down_2.set('Segundo')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_tempo:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Segundo')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_tempo:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[9]:
        
        stringVar_drop_down_2.set('Bit por segundo')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_transmissao_de_dados:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Bit por segundo')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_transmissao_de_dados:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[10]:
        
        stringVar_drop_down_2.set('Metro por segundo')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_velocidade:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Metro por segundo')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_velocidade:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[11]:
        
        stringVar_drop_down_2.set('Litro')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_volume:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Litro')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_volume:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[12]:
        
        stringVar_drop_down_2.set('Metro quadrado')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_area:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Metro quadrado')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_area:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

    elif atual_option == options_drop_down_1[13]:
        
        stringVar_drop_down_2.set('Grau')
        drop_down_2['menu'].delete(0, 'end')

        for option in options_angulo:
            drop_down_2['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_2, option))
        
        stringVar_drop_down_3.set('Grau')
        drop_down_3['menu'].delete(0, 'end')

        for option in options_angulo:
            drop_down_3['menu'].add_command(label=option, command=tk._setit(stringVar_drop_down_3, option))

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
default_drop_down_1 = options_drop_down_1[1]
stringVar_drop_down_1 = StringVar(window)
stringVar_drop_down_1.set(default_drop_down_1)
drop_down_1 = OptionMenu(
    window,
    stringVar_drop_down_1,
    *options_drop_down_1,
    command=change_options_menu
)

drop_down_1['width'] = w
drop_down_1['font'] = 'Arial 20'
drop_down_1['anchor'] = 'w'

options_drop_down_2 = options_comprimento
default_drop_down_2 = options_drop_down_2[1]
stringVar_drop_down_2 = StringVar(window)
stringVar_drop_down_2.set(default_drop_down_2)
drop_down_2 = OptionMenu(
    window,
    stringVar_drop_down_2,
    *options_drop_down_2
)

drop_down_2['width'] = 15
drop_down_2['font'] = 'Arial 20'
drop_down_2['anchor'] = 'w'

options_drop_down_3 = options_comprimento
default_drop_down_3 = options_drop_down_3[1]
stringVar_drop_down_3 = StringVar(window)
stringVar_drop_down_3.set(default_drop_down_3)
drop_down_3 = OptionMenu(
    window,
    stringVar_drop_down_3,
    *options_drop_down_3
)

drop_down_3['width'] = 15
drop_down_3['font'] = 'Arial 20'
drop_down_3['anchor'] = 'w'


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

drop_down_1.pack()
drop_down_2.place(x=7, y=150)
drop_down_3.place(x=375, y=150)
entry.place(x=7, y=110)
label_result.place(x=375, y=110)
label_equal.place(x=283, y=153)


window.mainloop()
