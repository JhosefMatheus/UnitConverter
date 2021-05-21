

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

    def change_label_formula_text(self, label_formula, drop_down_2, drop_down_3):
        print(drop_down_2.get_value())
