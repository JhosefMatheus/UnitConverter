

class Converter:
    def __init__(self):
        self.options_armazenamento_de_dados = [
            'Bit',
            'Kilobit',
            'Kibibit',
            'Megabit',
            'Mebibit',
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
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1e+15'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+15'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Bit' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8,389e+6'

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
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,007e+15'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,024'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1049'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074e+6'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Kilobit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultaedo aproximado, divida o valor de armazenamentoz de dados por 1,1e+9'

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
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8389'

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
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,007e+12'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,024'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 977'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 976562'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,766e+8'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,766e+11'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,812'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7813'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,812e+6'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8,389e+6'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,812e+9'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59e+9'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,812e+12'

            elif option_drop_down_2 == 'Kibibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796e+12'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 977'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1074'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1e+6'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+9'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultadoa proximado, multiplique o valor de armazenamento de dados por 122'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8,389'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8590'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796e+6'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+9'

            elif option_drop_down_2 == 'Megabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,007e+9'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1049'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 954'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 953674'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,537e+8'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 131'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,629'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7629'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,629e+6'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8,389e+6'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,629e+9'

            elif option_drop_down_2 == 'Mebibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59e+9'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 976563'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 954'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1100'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+6'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+8'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 122070'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 119'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,59'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 8796'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Gigabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,007e+6'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+6'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1074'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 931'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 931323'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,342e+8'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 134218'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 134'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,451'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7451'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,451e+6'

            elif option_drop_down_2 == 'Gibibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,766e+8'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 953674'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 931'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1126'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+11'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+8'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,221e+8'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 119209'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 116'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8,796'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Terabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9007'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+9'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+6'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1100'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 909'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,374e+11'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,374e+8'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,342e+8'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 137439'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 137'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 7,276'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7276'

            elif option_drop_down_2 == 'Tebibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+15'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,766e+11'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,537e+8'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 931323'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 909'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+14'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+11'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,221e+11'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,25e+8'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,192e+8'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 116415'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 114'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Petabit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,007'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+15'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+12'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+9'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+6'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valro de armazenamento de dados por 1126'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,407e+14'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,407e+11'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,374e+11'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,407e+8'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o valor de armazenamento de dados por 1,342e+8'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 140737'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 141'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 7,105'

            elif option_drop_down_2 == 'Pebibit' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,25e+8'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultadoa proximado, divida o valor de armazenamento de dados por 1,342e+8'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,25e+11'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,374e+11'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,25e+14'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 11,407e+14'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um reusultado aproximado, divida o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 1e+15'

            elif option_drop_down_2 == 'Byte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+15'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,812'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 131'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 134218'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,25e+8'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,347e+8'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,25e+11'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,407e+11'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,024'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1049'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074e+6'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 1,1e+9'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Kilobyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+12'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,192'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 122'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 122070'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 1,221e+8'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,342e+8'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,221e+11'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,374e+11'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,024'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Megabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 977'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 976562'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,766e+8'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,766e+11'

            elif option_drop_down_2 == 'Kibibyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7813'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,629'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 134'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 137439'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,25e+8'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,407e+8'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamentod e dados por 1e+6'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 977'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1074'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1e+6'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Megabyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+9'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8,389e+6'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8389'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8,389'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 119'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 119209'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,192e+8'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,342e+8'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1049'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 954'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 953674'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 9,537e+8'

            elif option_drop_down_2 == 'MebiByte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+9'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,812e+6'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7629'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,451'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 137'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125000'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 140737'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 976563'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 954'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,074'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1100'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Gigabyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126e+6'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,59e+9'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,59e+6'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8,389e+6'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8590'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,59'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 116'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 116415'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 131072'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+6'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1074'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 931'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 931323'

            elif option_drop_down_2 == 'Gibibyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+12'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+9'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,812e+9'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,629e+6'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7451'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 7,276'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 125'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 141'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,766e+8'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 953674'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 931'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1,1'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Terabyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 1126'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,796e+12'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,796e+9'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,59e+9'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,796e+6'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8,389e+6'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8796'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,796'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 114'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 128'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+9'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+6'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Mebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1100'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de armazenamento de dados por 909'

            elif option_drop_down_2 == 'Tebibyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+15'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+12'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,812e+12'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+9'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,629e+9'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8e+6'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,451e+6'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8000'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7276'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 7,105'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+15'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+12'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,766e+11'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+9'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,537e+8'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1e+6'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 931323'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1000'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 909'

            elif option_drop_down_2 == 'Petabyte' and option_drop_down_3 == 'Pebibyte':
                label_formula['text'] = 'Fórmula: divida o valor de armazenamento de dados por 1,126'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Bit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,007e+15'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Kilobit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,007e+12'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Kibibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,796e+12'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Megabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,007e+9'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Mebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8,59e+9'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Gigabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,007e+6'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Gibibit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 8,389e+6'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Terabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9007'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Tebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8192'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Petabit':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 9,007'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Pebibit':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 8'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Byte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+15'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Kilobyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+12'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Kibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,1e+12'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'MegaByte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+9'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'MebiByte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,074e+9'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Gigabyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1,126e+6'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Gibibyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1,049e+6'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Terabyte':
                label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de armazenamento de dados por 1126'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Tebibyte':
                label_formula['text'] = 'Fórmula: multiplique o valor de armazenamento de dados por 1024'

            elif option_drop_down_2 == 'Pebibyte' and option_drop_down_3 == 'Petabyte':
                label_formula['text'] = 'Fórmula: dmultiplique o valor de armazenamento de dados por 1,126'

        elif drop_down_1.get() == 'Comprimento':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'

            elif option_drop_down_2 == 'Quilômetro':
                if option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 100000'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1e+6'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1e+9'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1e+12'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1,609'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1094'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o valor de comprimento por 3281'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 39370'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1,852'

            elif option_drop_down_2 == 'Metro':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comrprimento por 100'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comrpimento por 1e+6'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o valor de comprimento por 1e+9'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1609'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o valor de comprimento por 1,094'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 3,281'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 39,37'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1852'

            elif option_drop_down_2 == 'Centímetro':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 100000'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 100'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 10'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 10000'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1e+7'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: pra um resultado aproximado, divida o valor de comprimento por 160394'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 91,44'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 30,48'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 2,54'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 185200'

            elif option_drop_down_2 == 'Milímetro':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comrpimento por 1e+6'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 10'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1e+6'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1,609e+6'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de comprimento por 914'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de comprimento por 305'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 25,4'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1,852e+6'

            elif option_drop_down_2 == 'Micrômetro':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1e+9'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1e+6'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento 10000'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento 1000'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de comprimento por 1,609e+9'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 914400'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 304800'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 25400'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1,852e+9'

            elif option_drop_down_2 == 'Nanômetro':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1e+12'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor comprimento por 1e+9'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1e+7'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1e+6'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1000'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1,609e+12'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 9,144e+8'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 3,048e+8'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 2,54e+7'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1,852e+12'

            elif option_drop_down_2 == 'Milha':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1,609'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o valor de comprimento por 1609'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 160934'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1,609e+6'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1,609e+9'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1,609e+12'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1760'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 5280'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 63360'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1,151'

            elif option_drop_down_2 == 'Jarda':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1094'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 1,094'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 91,44'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 914'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 914400'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 9,144e+8'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 1760'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 3'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 36'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 2025'

            elif option_drop_down_2 == 'Pé':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 3281'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 3,281'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 30,48'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 305'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 304800'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 3,048e+8'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 5280'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 3'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 12'

                elif option_drop_down_3 == 'Milha naútica':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 6076'

            elif option_drop_down_2 == 'Polegada':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 39370'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 39,37'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 2,54'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 25,4'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 25400'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 2,54e+7'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 63360'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 36'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: divida o valor de comprimento por 12'

                elif option_drop_down_3 == 'Milha náutica':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de comprimento por 72913'

            elif option_drop_down_2 == 'Milha náutica':
                if option_drop_down_3 == 'Quilômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1,852'

                elif option_drop_down_3 == 'Metro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1852'

                elif option_drop_down_3 == 'Centímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 185200'

                elif option_drop_down_3 == 'Milímetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1,852e+6'

                elif option_drop_down_3 == 'Micrômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1,852e+9'

                elif option_drop_down_3 == 'Nanômetro':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comprimento por 1,852e+12'

                elif option_drop_down_3 == 'Milha':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 1,151'

                elif option_drop_down_3 == 'Jarda':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 2025'

                elif option_drop_down_3 == 'Pé':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 6076'

                elif option_drop_down_3 == 'Polegada':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de comprimento por 72913'

        elif drop_down_1.get() == 'Consumo de Combustível':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'

            elif option_drop_down_2 == 'Milha por galão americano':
                if option_drop_down_3 == 'Milhas por galão imperial':
                    label_formula['text'] = 'Fórmula: multiplique o valor de comsumo de combustível por 1,201'

                elif option_drop_down_3 == 'Quilômetro por litro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de consumo de combustível por 2,352'

                elif option_drop_down_3 == 'Litro por 100 quilômetros':
                    label_formula['text'] = 'Fórmula: 235,215/(1 mpg EUA) = 235,215 L/100 km'

            elif option_drop_down_2 == 'Milhas por galão imperial':
                if option_drop_down_3 == 'Milha por galão americano':
                    label_formula['text'] = 'Fórmula: divida o valor de consumo de combustível por 1,201'

                elif option_drop_down_3 == 'Quilômetro por litro':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de consumo de combustível por 2,825'

                elif option_drop_down_3 == 'Litro por 100 quilômetros':
                    label_formula['text'] = 'Fórmula: 282,481/(1 mpg imperial) = 282,481 L/100 km'

            elif option_drop_down_2 == 'Quilômetro por litro':
                if option_drop_down_3 == 'Milha por galão americano':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de consumo de combustível por 2,352'

                elif option_drop_down_3 == 'Milhas por galão imperial':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de consumo de combustível por 2,825'

                elif option_drop_down_3 == 'Litro por 100 quilômetros':
                    label_formula['text'] = 'Fórmula: 100/(1 km/L) = 100 L/100 km'

            elif option_drop_down_2 == 'Litro por 100 quilômetros':
                if option_drop_down_3 == 'Milha por galão americano':
                    label_formula['text'] = 'Fórmula: 235,215/(1 L/100 km) = 235,215 mpg EUA'

                elif option_drop_down_3 == 'Milhas por galão imperial':
                    label_formula['text'] = 'Fórmula: 282,481/(1 L/100 km) = 282,481 mpg imperial'

                elif option_drop_down_3 == 'Quilômetro por litro':
                    label_formula['text'] = 'Fórmula: 100/(1 L/100 km) = 100 km/L'

        elif drop_down_1.get() == 'Energia Mecânica':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'

            elif option_drop_down_2 == 'Joule':
                if option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 1000'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 4,184'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 4184'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 3600'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 3,6e+6'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 6,242e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 1055'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 1,055e+8'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 1,356'

            elif option_drop_down_2 == 'Quilojoule':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 1000'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 239'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 4,184'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 3,6'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 3600'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 1,055'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 105480'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 738'

            elif option_drop_down_2 == 'Gram calorie':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 4,184'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 239'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 1000'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 860'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 860421'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 252'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 2,512e+7'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 3,086'

            elif option_drop_down_2 == 'Quilocaloria':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 4184'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 4,184'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 1000'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 1,162'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 860'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 3,966'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecãnica por 25210'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o valor de energia mecânica por 3086'

            elif option_drop_down_2 == 'Watt-hora':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 3600'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 3,6'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 860'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 1,162'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 1000'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 3,412'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 29300'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 2655'

            elif option_drop_down_2 == 'Quilowatt-hora':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 3,6e+6'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 3600'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 860421'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, multiplique o vaor de energia mecânica por 860'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 1000'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 3412'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 29,3'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 2,655e+6'

            elif option_drop_down_2 == 'Elétron-volt':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 6,242e+18'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 8,462e+18'

            elif option_drop_down_2 == 'BTU':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 1055'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 1,055'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 252'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 3,966'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 3,412'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 3412'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 99976'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 778'

            elif option_drop_down_2 == 'therm (US)':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 1,055e+8'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 105480'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 2,521e+7'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 25210'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: para um resultaod aproximado, multiplique o valor de energia mecânica por 29300'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de energia mecânica por 29,3'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 9,223e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 99976'

                elif option_drop_down_3 == 'Pé-libra força':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 7,78e+7'

            elif option_drop_down_2 == 'Pé-libra força':
                if option_drop_down_3 == 'Joule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 1,356'

                elif option_drop_down_3 == 'Quilojoule':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 738'

                elif option_drop_down_3 == 'Gram calorie':
                    label_formula['text'] = 'Fórmula: divida o valor de energia mecânica por 3,086'

                elif option_drop_down_3 == 'Quilocaloria':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 3086'

                elif option_drop_down_3 == 'Watt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 2655'

                elif option_drop_down_3 == 'Quilowatt-hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 2,655e+6'

                elif option_drop_down_3 == 'Elétron-volt':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de energia mecânica por 8,462e+18'

                elif option_drop_down_3 == 'BTU':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 778'

                elif option_drop_down_3 == 'therm (US)':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de energia mecânica por 7,78e+7'

        elif drop_down_1.get() == 'Frequência':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'

            elif option_drop_down_2 == 'Hertz':
                if option_drop_down_3 == 'Quilo-hertz':
                    label_formula['text'] = 'Fórmula: divida o valor de frequência por 1000'

                elif option_drop_down_3 == 'Mega-hertz':
                    label_formula['text'] = 'Fórmula: divida o valor de frequência por 1e+6'

                elif option_drop_down_3 == 'Gigahertz':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de frequência por 1e+9'

            elif option_drop_down_2 == 'Quilo-hertz':
                if option_drop_down_3 == 'Hertz':
                    label_formula['text'] = 'Fórmula: multiplique o valor de frequência por 1000'

                elif option_drop_down_3 == 'Mega-hertz':
                    label_formula['text'] = 'Fórmula: divida o valor de frequência por 1000'

                elif option_drop_down_3 == 'Gigahertz':
                    label_formula['text'] = 'Fórmula: divida o valor de frequência por 1e+6'

            elif option_drop_down_2 == 'Mega-hertz':
                if option_drop_down_3 == 'Hertz':
                    label_formula['text'] = 'Fórmula: multiplique o valor de frequência por 1e+6'

                elif option_drop_down_3 == 'Quilo-hertz':
                    label_formula['text'] = 'Fórmula: multiplique o valor de frequência por 1000'

                elif option_drop_down_3 == 'Gigahertz':
                    label_formula['text'] = 'Fórmula: divida o valor de frequência por 1000'

            elif option_drop_down_2 == 'Gigahertz':
                if option_drop_down_3 == 'Hertz':
                    label_formula['text'] = 'Fórmula: multiplique o valor de frequência por 1e+9'

                elif option_drop_down_3 == 'Quilo-hertz':
                    label_formula['text'] = 'Fórmula: multiplique o valor de frequência por 1e+6'

                elif option_drop_down_3 == 'Mega-hertz':
                    label_formula['text'] = 'Fórmula: multiplique o valor de frequência por 1000'

        elif drop_down_1.get() == 'Massa':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'

            elif option_drop_down_2 == 'Tonelada':
                if option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1000'

                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1e+6'

                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1e+9'

                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 1e+12'

                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de de massa por 1,016'

                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 1,102'

                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 157'

                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 2205'

                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 35274'

            elif option_drop_down_2 == 'Quilograma':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1000'

                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1000'

                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1e+6'

                elif option_drop_down_3 == 'Microggrama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 1e+9'

                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 1016'

                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 907'

                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 6,35'

                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 2,205'

                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 35,274'

            elif option_drop_down_2 == 'Grama':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1e+6'

                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1000'

                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1000'

                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1e+6'

                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1,016e+6'

                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 907185'

                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 6350'

                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 454'

                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 28,35'

            elif option_drop_down_2 == 'Miligrama':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1e+9'

                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1e+6'

                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1000'

                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1000'

                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1,016e+9'

                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 9,072e+8'

                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 6,35e+6'

                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 453592'

                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 28350'

            elif option_drop_down_2 == 'Micrograma':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1e+12'

                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 1e+9'

                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1e+6'

                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1000'

                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1,016+12'

                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 9,072e+11'

                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 6,35e+9'

                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 4,536e+8'

                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 2,835e+7'

            elif option_drop_down_2 == 'Tonelada de deslocamento':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1,016'

                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 1016'

                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1,016e+6'

                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1,016e+9'

                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1,016e+12'

                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 1,12'

                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 160'

                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 2240'

                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 35840'
            
            elif option_drop_down_2 == 'Tonelada curta':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 1,102'
                
                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 907'
                
                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 907185'
                
                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 9,072e+8'
                
                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 9,072e+11'
                
                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 1,12'
                
                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 143'
                
                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 2000'
                
                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 32000'
            
            elif option_drop_down_2 == 'Stone':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 157'
                
                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 6,35'
                
                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 6350'
                
                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 6,35e+6'
                
                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 6,35e+9'
                
                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 160'
                
                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 143'
                
                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 14'
                
                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 224'
            
            elif option_drop_down_2 == 'Libra':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 2205'
                
                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 2,205'
                
                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 454'
                
                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 453592'
                
                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 4,536e+8'
                
                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 2240'
                
                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 2000'
                
                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 14'
                
                elif option_drop_down_3 == 'Onça':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 16'
            
            elif option_drop_down_2 == 'Onça':
                if option_drop_down_3 == 'Tonelada':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de massa por 35274'
                
                elif option_drop_down_3 == 'Quilograma':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 35,274'
                
                elif option_drop_down_3 == 'Grama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 28,35'
                
                elif option_drop_down_3 == 'Miligrama':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de massa por 28350'
                
                elif option_drop_down_3 == 'Micrograma':
                    label_formula['text'] = 'Fórmula: multiplique o valor de massa por 2,835e+7'
                
                elif option_drop_down_3 == 'Tonelada de deslocamento':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 35840'
                
                elif option_drop_down_3 == 'Tonelada curta':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 32000'
                
                elif option_drop_down_3 == 'Stone':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 224'
                
                elif option_drop_down_3 == 'Libra':
                    label_formula['text'] = 'Fórmula: divida o valor de massa por 16'

        elif drop_down_1.get() == 'Pressão':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'
            
            elif option_drop_down_2 == 'Atmosfera padrão':
                if option_drop_down_3 == 'Bar':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de pressão por 1,013'
                
                elif option_drop_down_3 == 'Pascal':
                    label_formula['text'] = 'Fórmula: multiplique o valor de pressão por 101325'
                
                elif option_drop_down_3 == 'Psi':
                    label_formula['text'] = 'Fórmula: multiplique o valor de pressão por 14,696'
                
                elif option_drop_down_3 == 'Torr':
                    label_formula['text'] = 'Fórmula: multiplique o valor de pressão por 760'
                
            elif option_drop_down_2 == 'Bar':
                if option_drop_down_3 == 'Atmosfera padrão':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de pressão por 1,013'
                
                elif option_drop_down_3 == 'Pascal':
                    label_formula['text'] = 'Fórmula: multiplique o valor de pressão por 100000'
                
                elif option_drop_down_3 == 'Psi':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de pressão por 14,504'
                
                elif option_drop_down_3 == 'Torr':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de pressão por 750'
            
            elif option_drop_down_2 == 'Pascal':
                if option_drop_down_3 == 'Atmosfera padrão':
                    label_formula['text'] = 'Fórmula: divida o valor de pressão por 101325'
                
                elif option_drop_down_3 == 'Bar':
                    label_formula['text'] = 'Fórmula: divida o valor de pressão por 100000'
                
                elif option_drop_down_3 == 'Psi':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de pressão por 6895'
                
                elif option_drop_down_3 == 'Torr':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de pressão por 133'
                
            elif option_drop_down_2 == 'Psi':
                if option_drop_down_3 == 'Atmosfera padrão':
                    label_formula['text'] = 'Fórmula: divida o valor de pressão por 14,696'
                
                elif option_drop_down_3 == 'Bar':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de pressão por 14,504'
                
                elif option_drop_down_3 == 'Pascal':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de pressão por 6895'
                
                elif option_drop_down_3 == 'Torr':
                    label_formula['text'] = 'Fórmula: multiplique o valor de pressão por 51,715'
            
            elif option_drop_down_2 == 'Torr':
                if option_drop_down_3 == 'Atmosfera padrão':
                    label_formula['text'] = 'Fórmula: divida o valor de pressão por 760'
                
                elif option_drop_down_3 == 'Bar':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de pressão por 750'
                
                elif option_drop_down_3 == 'Pascal':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de pressão por 133'
                
                elif option_drop_down_3 == 'Psi':
                    label_formula['text'] = 'Fórmula: divida o valor de pressão por 51,715'

        elif drop_down_1.get() == 'Temperatura':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'
            
            elif option_drop_down_2 == 'Grau Celsius':
                if option_drop_down_3 == 'Grau Fahrenheit':
                    label_formula['text'] = 'Fórmula: (0 °C x 9/5) + 32 = 32 °F'
                
                elif option_drop_down_3 == 'Kelvin':
                    label_formula['text'] = 'Fórmula: 0 °C + 273,15 = 273,15 K'
            
            elif option_drop_down_2 == 'Grau Fahrenheit':
                if option_drop_down_3 == 'Grau Celsius':
                    label_formula['text'] = 'Fórmula: (0 °F - 32) x 5/9 = -17,78 °C'
                
                elif option_drop_down_3 == 'Kelvin':
                    label_formula['text'] = 'Fórmula: (0 °F - 32) x 5/9 + 273,15 = 255,372 K'
                
            elif option_drop_down_2 == 'Kelvin':
                if option_drop_down_3 == 'Grau Celsius':
                    label_formula['text'] = 'Fórmula: 0 K - 273,15 = -273,15 °C'
                
                elif option_drop_down_3 == 'Grau Fahrenheit':
                    label_formula['text'] = 'Fórmula: (0 K - 273,15) x 9/5 + 32 = -459,7 °F'

        elif drop_down_1.get() == 'Tempo':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'
            
            elif option_drop_down_2 == 'Nanosegundo':
                if option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: divida o valor de tempor por 1000'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: divida o valor de tempor por 1e+6'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempor por 1e+9'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: divida o valor de tempor por 6e+10'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 3,6e+12'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 8,64e+13'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 6,048e+14'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: divida o valor de tempor por 2,628e+15'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+16'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+17'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+18'
            
            elif option_drop_down_2 == 'Microssegundo':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 1000'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 1000'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 1e+6'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 6e+7'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 3,6e+9'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 8,64e+10'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 6,048e+11'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 2,628e+12'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+13'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+14'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+15'
            
            elif option_drop_down_2 == 'Milissegundo':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 1e+6'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 1000'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 1000'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: divida o valor tempo por 60000'
            
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 3,6e+6'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 8,64e+7'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 6,048e+8'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 2,628e+9'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+10'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+11'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+12'
            
            elif option_drop_down_2 == 'Segundo':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 1e+9'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 1e+6'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 1000'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 60'
            
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 3600'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 86400'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 604800'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: divida o valor de tempor por 2,628e+6'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+7'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+8'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 3,154e+9'
            
            elif option_drop_down_2 == 'Minuto':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 6e+10'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 6e+7'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 60000'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 60'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 60'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 1440'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 10080'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 43800'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 525600'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 5,256e+6'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 5,256e+7'
                
            elif option_drop_down_2 == 'Hora':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 3,6e+12'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 3,6e+9'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 3,6e+6'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 3600'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 60'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo 24'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo 168'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 730'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 8760'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 87600'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 876000'
                
            elif option_drop_down_2 == 'Dia':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 8,64e+13'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 8,64e+10'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 8,64e+7'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 86400'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 1440'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 24'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 7'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 30,417'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 365'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 3650'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 36500'
                
            elif option_drop_down_2 == 'Semana':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 6,048e+14'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 6,048e+11'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 6,048e+8'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 604800'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 10080'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 168'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 7'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 4,345'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 52,143'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 521'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 5214'
                
            elif option_drop_down_2 == 'Mês':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 2,628e+15'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 2,628e+12'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 2,628e+9'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 2,628e+6'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de de tempo por 43800'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 730'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 30,417'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 4,345'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 12'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 120'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de tempo por 1200'
                
            elif option_drop_down_2 == 'Ano-calendário':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+16'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+13'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+10'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+7'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 525600'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 8760'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 365'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 52,143'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 12'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 10'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 100'
                
            elif option_drop_down_2 == 'Década':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+17'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+14'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+11'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+8'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 5,256e+6'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 87600'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 3650'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 521'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 120'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 10'
                
                elif option_drop_down_3 == 'Século':
                    label_formula['text'] = 'Fórmula: divida o valor de tempo por 10'
            
            elif option_drop_down_2 == 'Século':
                if option_drop_down_3 == 'Nanosegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+18'
                
                elif option_drop_down_3 == 'Microssegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+15'
                
                elif option_drop_down_3 == 'Milissegundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+12'
                
                elif option_drop_down_3 == 'Segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 3,154e+9'
                
                elif option_drop_down_3 == 'Minuto':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 5,256e+7'
                
                elif option_drop_down_3 == 'Hora':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 876000'
                
                elif option_drop_down_3 == 'Dia':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 36500'
                
                elif option_drop_down_3 == 'Semana':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 5214'
                
                elif option_drop_down_3 == 'Mês':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de tempo por 1200'
                
                elif option_drop_down_3 == 'Ano-calendário':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 100'
                
                elif option_drop_down_3 == 'Década':
                    label_formula['text'] = 'Fórmula: multiplique o valor de tempo por 10'

        elif drop_down_1.get() == 'Transmissão de dados':
            if option_drop_down_2 == option_drop_down_3:
                label_formula['text'] = 'Fórmula desnecessária'
            
            elif option_drop_down_2 == 'Bit por segundo':
                if option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8000'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8e+6'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,049e+6'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1e+9'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8e+9'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,074e+9'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1e+12'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8e+12'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,1e+12'
                
            elif option_drop_down_2 == 'Quilobit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1,024'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8000'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1049'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8e+6'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,074e+6'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1e+9'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8e+9'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,1e+9'
                
            elif option_drop_down_2 == 'Quilobyte por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8000'

                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7,812'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 125'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 131'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 125000'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um reusltado aproximado, divida o valor de transmissão de dados por 134218'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1,5e+8'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1e+9'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,347e+8'
            
            elif option_drop_down_2 == 'Kibibit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1,024'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7,812'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 977'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7813'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 976562'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7,812e+6'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,049e+6'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 9,766e+8'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7,812e+9'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,074e+9'
                
            elif option_drop_down_2 == 'Megabit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 125'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 977'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,049'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8000'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1074'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8e+6'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,1e+6'
                
            elif option_drop_down_2 == 'Megabyte por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8e+6'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8000'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7813'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fòrmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7,629'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 125'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 134'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 125000'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 137439'
                
            elif option_drop_down_2 == 'Mebibit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,049e+6'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1049'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 131'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,049'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7,629'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 954'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7629'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 953674'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7,629e+6'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,049e+6'
                
            elif option_drop_down_2 == 'Gigabit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+9'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 125000'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 976563'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'

                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 125'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 954'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,074'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmisssão de dados por 8000'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1100'
            
            elif option_drop_down_2 == 'Gigabyte por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8e+9'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8e+6'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultaod aproximado, multiplique o valor de transmissão de dados por 7,812e+6'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8000'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7629'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7,451'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 125'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 137'
            
            elif option_drop_down_2 == 'Gibibit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,074e+9'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,074e+6'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 134218'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,049e+6'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1074'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 134'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,074'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7,451'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 931'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 7451'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 1024'
                
            elif option_drop_down_2 == 'Terabit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+12'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+9'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1,25e+8'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 9,766e+8'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 125000'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 953674'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 125'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 931'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, divida o valor de transmissão de dados por 1,1'
            
            elif option_drop_down_2  == 'Terabyte por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8e+12'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8e+9'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+9'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7,812e+9'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8e+6'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1e+6'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7,629e+6'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8000'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1000'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 7451'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 8'
                
                elif option_drop_down_3 == 'Tebibit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 7,276'
            
            elif option_drop_down_2 == 'Tebibit por segundo':
                if option_drop_down_3 == 'Bit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,1e+12'
                
                elif option_drop_down_3 == 'Quilobit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,1e+9'
                
                elif option_drop_down_3 == 'Quilobyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,374e+8'
                
                elif option_drop_down_3 == 'Kibibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,074e+9'
                
                elif option_drop_down_3 == 'Megabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,1e+6'
                
                elif option_drop_down_3 == 'Megabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 137439'
                
                elif option_drop_down_3 == 'Mebibit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,049e+6'
                
                elif option_drop_down_3 == 'Gigabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1100'
                
                elif option_drop_down_3 == 'Gigabyte por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 137'
                
                elif option_drop_down_3 == 'Gibibit por segundo':
                    label_formula['text'] = 'Fórmula: multiplique o valor de transmissão de dados por 1024'
                
                elif option_drop_down_3 == 'Terabit por segundo':
                    label_formula['text'] = 'Fórmula: para um resultado aproximado, multiplique o valor de transmissão de dados por 1,1'
                
                elif option_drop_down_3 == 'Terabyte por segundo':
                    label_formula['text'] = 'Fórmula: divida o valor de transmissão de dados por 7,276'

        elif drop_down_1.get() == 'Velocidade':
            pass

        elif drop_down_1.get() == 'Volume':
            pass

        elif drop_down_1.get() == 'Área':
            pass

        elif drop_down_1.get() == 'Ângulo':
            pass
