import itertools

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

    def change_options_menu(self, drop_down_1, drop_down_2, drop_down_3):
        if drop_down_1.get() == 'Armazenamento de Dados':
            drop_down_2.config(value=self.options_armazenamento_de_dados)
            drop_down_3.config(value=self.options_armazenamento_de_dados)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Comprimento':
            drop_down_2.config(value=self.options_comprimento)
            drop_down_3.config(value=self.options_comprimento)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Consumo de Combustível':
            drop_down_2.config(value=self.options_consumo_de_combustivel)
            drop_down_3.config(value=self.options_consumo_de_combustivel)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Energia Mecânica':
            drop_down_2.config(value=self.options_energia_mecanica)
            drop_down_3.config(value=self.options_energia_mecanica)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Frequência':
            drop_down_2.config(value=self.options_frequencia)
            drop_down_3.config(value=self.options_frequencia)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Massa':
            drop_down_2.config(value=self.options_massa)
            drop_down_3.config(value=self.options_massa)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Pressão':
            drop_down_2.config(value=self.options_pressao)
            drop_down_3.config(value=self.options_pressao)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Temperatura':
            drop_down_2.config(value=self.options_temperatura)
            drop_down_3.config(value=self.options_temperatura)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Tempo':
            drop_down_2.config(value=self.options_tempo)
            drop_down_3.config(value=self.options_tempo)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Transmissão de dados':
            drop_down_2.config(value=self.options_transmissao_de_dados)
            drop_down_3.config(value=self.options_transmissao_de_dados)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Velocidade':
            drop_down_2.config(value=self.options_velocidade)
            drop_down_3.config(value=self.options_velocidade)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Volume':
            drop_down_2.config(value=self.options_volume)
            drop_down_3.config(value=self.options_volume)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Área':
            drop_down_2.config(value=self.options_area)
            drop_down_3.config(value=self.options_area)
            drop_down_2.current(0)
            drop_down_3.current(0)

        elif drop_down_1.get() == 'Ângulo':
            drop_down_2.config(value=self.options_angulo)
            drop_down_3.config(value=self.options_angulo)
            drop_down_2.current(0)
            drop_down_3.current(0)

    def change_label_formula_text(self, label_formula, drop_down_1, drop_down_2, drop_down_3):
        option_drop_down_2 = drop_down_2.get()
        option_drop_down_3 = drop_down_3.get()
        
        if drop_down_1.get() == 'Armazenamento de Dados':

            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,049e+6'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1e+9'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,074e+9'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+12'
            
            elif option_drop_down_2 =='Bit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,1e+12'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1e+15'
            
            elif option_drop_down_2 =='Bit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+15'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 ==  'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8,389e+6'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+9'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59e+9'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenmaneto de dados por 8e+12'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796+12'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+15'
            
            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,007e+15'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,024'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1049'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,074e+6'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1e+9'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultaedo aproximado, divida o valor de armazenamentoz\n de dados por 1,1e+9'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+12'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+12'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,192'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8389'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59e+6'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+9'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796e+9'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+12'
            
            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,007e+12'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,024'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 977'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 976562'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,049e+6'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,766e+8'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,074e+9'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,766e+11'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,1e+12'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,812'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7813'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,812e+6'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8,389e+6'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,812e+9'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59e+9'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,812e+12'
            
            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796e+12'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 977'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1074'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,1e+6'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1e+9'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+9'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultadoa proximado, multiplique o valor de armazenamento\n de dados por 122'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8,389'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8590'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796e+6'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+9'
            
            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,007e+9'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,049e+6'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1049'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,049'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 954'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 953674'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,049e+6'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,537e+8'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,074e+9'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 131072'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 131'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,629'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7629'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,629e+6'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8,389e+6'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,629e+9'
            
            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59e+9'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 976563'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 954'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,074'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1100'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+6'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+8'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 122070'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 119'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 8796'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'
            
            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9,007e+6'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,074e+9'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,074e+6'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,049e+6'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1074'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,074'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 931'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 931323'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,049e+6'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,342e+8'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 134218'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 131072'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 134'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,451'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7451'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 7,451e+6'
            
            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 9,766e+8'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 953674'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 931'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1,1'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 1126'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+11'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+8'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 1,221e+8'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 119209'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento\n de dados por 116'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'
            
            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento\n de dados por 9007'
        
        elif drop_down_1.get() == 'Comprimento':
            cartesian_product = itertools.product(self.options_comprimento, self.options_comprimento)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Consumo de Combustível':
            cartesian_product = itertools.product(self.options_consumo_de_combustivel, self.options_consumo_de_combustivel)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Energia Mecãnica':
            cartesian_product = itertools.product(self.options_energia_mecanica, self.options_energia_mecanica)

            for product in cartesian_product:
                print(product)

        elif drop_down_1.get() == 'Frequência':
            cartesian_product = itertools.product(self.options_frequencia, self.options_frequencia)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Massa':
            cartesian_product = itertools.product(self.options_massa, self.options_massa)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Pressão':
            cartesian_product = itertools.product(self.options_pressao, self.options_pressao)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Temperatura':
            cartesian_product = itertools.product(self.options_temperatura, self.options_temperatura)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Tempo':
            cartesian_product = itertools.product(self.options_tempo, self.options_tempo)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Transmissão de dados':
            cartesian_product = itertools.product(self.options_transmissao_de_dados, self.options_transmissao_de_dados)
            
            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Velocidade':
            cartesian_product = itertools.product(self.options_velocidade, self.options_velocidade)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Volume':
            cartesian_product = itertools.product(self.options_volume, self.options_volume)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Área':
            cartesian_product = itertools.product(self.options_area, self.options_area)

            for product in cartesian_product:
                print(product)
        
        elif drop_down_1.get() == 'Ângulo':
            cartesian_product = itertools.product(self.options_angulo, self.options_angulo)
