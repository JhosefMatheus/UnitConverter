import tkinter as tk

class Converter:
    def __init__(self):
        self.__options_armazenamento_de_dados = [
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

        self.__options_comprimento = [
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

        self.__options_consumo_de_combustivel = [
            'Milha por galão americano',
            'Milha por galão imperial',
            'Quilômetro por litro',
            'Litro por 100 quilômetros'
        ]

        self.__options_energia_mecanica = [
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

        self.__options_frequencia = [
            'Hertz',
            'Quilo-hertz',
            'Mega-hertz',
            'Giga-hertz'
        ]

        self.__options_massa = [
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

        self.__options_pressao = [
            'Atmosfera padrão',
            'Bar',
            'Pascal',
            'Psi',
            'Torr'
        ]

        self.__options_temperatura = [
            'Grau Celsius',
            'Grau Fahrenheit',
            'Kelvin'
        ]

        self.__options_tempo = [
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

        self.__options_transmissao_de_dados = [
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

        self.__options_velocidade = [
            'Milha por hora',
            'Pés por segundo',
            'Metro por segundo',
            'Quilômetro por hora',
            'Nó'
        ]

        self.__options_volume = [
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

        self.__options_area = [
            'Quilômetro quadrado',
            'Metro quadrado',
            'Milha quadrada',
            'Jarda quadrada',
            'Pé quadrado',
            'Polegada quadrada',
            'Hectare',
            'Acre'
        ]

        self.__options_angulo = [
            'Grado',
            'Grau',
            'Mil angular',
            'Minuto de arco',
            'Radiano',
            'Segundo de arco'
        ]

    def change_option_menu(self, stringVar, option_menu_1, option_menu_2):
        optionDefault = tk.StringVar()
        optionDefault.set('')
        if stringVar == 'Armazenamento de Dados':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_armazenamento_de_dados:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Comprimento':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_comprimento:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Consumo de Combustível':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_consumo_de_combustivel:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Energia Mecânica':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_energia_mecanica:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Frequência':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_frequencia:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Massa':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_massa:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Pressão':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_pressao:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Temperatura':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_temperatura:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Tempo':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_tempo:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Transmissão de dados':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_transmissao_de_dados:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Velocidade':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_velocidade:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Volume':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_volume:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Área':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_area:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
        elif stringVar == 'Ângulo':
            option_menu_1['menu'].delete(0, 'end')
            option_menu_2['menu'].delete(0, 'end')
            for option in self.__options_angulo:
                option_menu_1['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )
                option_menu_2['menu'].add_command(
                    label=option,
                    command=tk._setit(optionDefault, option)
                )