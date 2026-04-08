# Define a classe Bicicleta
class Bicicleta:
    
    # Método construtor: inicializa os atributos da bicicleta
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor          # Cor da bicicleta
        self.modelo = modelo    # Modelo da bicicleta
        self.ano = ano          # Ano de fabricação
        self.valor = valor      # Valor da bicicleta
    
    # Método que simula o som da buzina
    def buzinar(self):
        print("Plim plim")

    # Método que simula a ação de parar a bicicleta
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")

    # Método que simula a bicicleta em movimento
    def correr(self):
        print("Vrummm ...")   

    # Método especial que define como o objeto será exibido ao usar print()
    def __str__(self):
        return f"{self.__class__.__name__}: {',  '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Criação do primeiro objeto da classe Bicicleta
b1 = Bicicleta("vermelho", "caloi", 2022, 600)

# Chamando métodos do objeto b1
b1.buzinar()   # Emite som da buzina
b1.parar()     # Simula parada
b1.correr()    # Simula movimento

# Exibe os dados do objeto b1
print(b1)


# Criação do segundo objeto da classe Bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)

# Chamando métodos do objeto b2
b2.buzinar()
b2.parar()
b2.correr()

# Exibe os dados do objeto b2
print(b2)
