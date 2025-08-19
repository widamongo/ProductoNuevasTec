from datetime import datetime

class Vehiculo:
    def __init__(self, placa, tipo, hora_entrada):
        self.placa = placa
        self.tipo = tipo
        self.hora_entrada = hora_entrada
        self.hora_salida = None

    def calcular_tiempo_estacionado(self):
        if self.hora_salida:
            return self.hora_salida - self.hora_entrada
        return None

    def calcular_tarifa(self, tarifas):
        tiempo_estacionado = self.calcular_tiempo_estacionado()
        if tiempo_estacionado:
            horas = tiempo_estacionado.total_seconds() / 3600
            tarifa_por_hora = tarifas.get(self.tipo, 0)
            return horas * tarifa_por_hora
        return 0
