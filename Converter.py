import tkinter as tk


class Converter:
    def __init__(self):
        self.options_armazenamento_de_dados = [
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

        self.options_comprimento = [
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

        self.options_consumo_de_combustivel = [
            'Milha por galão americano',
            'Milha por galão imperial',
            'Quilômetro por litro',
            'Litro por 100 quilômetros'
        ]

        self.options_energia_mecanica = [
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

        self.options_frequencia = [
            'Hertz',
            'Quilo-hertz',
            'Mega-hertz',
            'Giga-hertz'
        ]

        self.options_massa = [
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

        self.options_pressao = [
            'Atmosfera padrão',
            'Bar',
            'Pascal',
            'Psi',
            'Torr'
        ]

        self.options_temperatura = [
            'Grau Celsius',
            'Grau Fahrenheit',
            'Kelvin'
        ]

        self.options_tempo = [
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

        self.options_transmissao_de_dados = [
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

        self.options_velocidade = [
            'Milha por hora',
            'Pés por segundo',
            'Metro por segundo',
            'Quilômetro por hora',
            'Nó'
        ]

        self.options_volume = [
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

        self.options_area = [
            'Quilômetro quadrado',
            'Metro quadrado',
            'Milha quadrada',
            'Jarda quadrada',
            'Pé quadrado',
            'Polegada quadrada',
            'Hectare',
            'Acre'
        ]

        self.options_angulo = [
            'Grado',
            'Grau',
            'Mil angular',
            'Minuto de arco',
            'Radiano',
            'Segundo de arco'
        ]

    def change_options_menu(self, stringVar_drop_down_1, stringVar_drop_down_2, stringVar_drop_down_3, drop_down_2, drop_down_3):
        atual_option = stringVar_drop_down_1.get()

        if atual_option == 'Armazenamento de Dados':

            stringVar_drop_down_2.set('Byte')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Byte')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_armazenamento_de_dados:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Comprimento':

            stringVar_drop_down_2.set('Metro')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Metro')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_comprimento:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Consumo de Combustível':

            stringVar_drop_down_2.set('Quilômetro por litro')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Quilômetro por litro')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_consumo_de_combustivel:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Energia Mecânica':

            stringVar_drop_down_2.set('Joule')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Joule')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_energia_mecanica:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Frequência'[4]:

            stringVar_drop_down_2.set('Hertz')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Hertz')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_frequencia:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Massa':

            stringVar_drop_down_2.set('Quilograma')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Quilograma')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_massa:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Pressão':

            stringVar_drop_down_2.set('Pascal')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Pascal')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_pressao:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Temperatura':

            stringVar_drop_down_2.set('Grau Celsius')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Grau Celsius')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_temperatura:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Tempo':

            stringVar_drop_down_2.set('Segundo')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Segundo')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_tempo:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Transmissão de dados':

            stringVar_drop_down_2.set('Bit por segundo')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Bit por segundo')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_transmissao_de_dados:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Velocidade':

            stringVar_drop_down_2.set('Metro por segundo')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Metro por segundo')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_velocidade:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Volume':

            stringVar_drop_down_2.set('Litro')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Litro')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_volume:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Área':

            stringVar_drop_down_2.set('Metro quadrado')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Metro quadrado')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_area:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))

        elif atual_option == 'Ângulo':

            stringVar_drop_down_2.set('Grau')
            drop_down_2['menu'].delete(0, 'end')

            stringVar_drop_down_3.set('Grau')
            drop_down_3['menu'].delete(0, 'end')

            for option in self.options_angulo:
                drop_down_2['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_2, option))
                drop_down_3['menu'].add_command(
                    label=option, command=tk._setit(stringVar_drop_down_3, option))
