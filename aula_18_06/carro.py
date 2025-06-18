class Carro:
    def __init__(self, modelo,consumo):
        self.modelo = modelo
        self.consumo = consumo

    def calcular_consumo(self, distancia):
        return distancia / self.consumo

carro1 = Carro("Fusca", 12)
print("Litros necessários:", carro1.calcular_consumo(240))