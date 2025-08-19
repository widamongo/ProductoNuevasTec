from Vehiculo import Vehiculo

class Parqueadero:
    def __init__(self, capacidad_maxima, tarifas):
        self.capacidad_maxima = capacidad_maxima
        self.vehiculos_estacionados = []
        self.tarifas = tarifas

    def registrar_entrada(self, placa, tipo, hora_entrada):
        if len(self.vehiculos_estacionados) >= self.capacidad_maxima:
            print("PARQUEADERO LLENO")
            return
        for vehiculo in self.vehiculos_estacionados:
            if vehiculo.placa == placa:
                print("El vehículo ya está registrado")
                return
        nuevo_vehiculo = Vehiculo(placa, tipo, hora_entrada)
        self.vehiculos_estacionados.append(nuevo_vehiculo)
        print("Vehículo registrado exitosamente")

    def registrar_salida(self, placa, hora_salida):
        for vehiculo in self.vehiculos_estacionados:
            if vehiculo.placa == placa:
                vehiculo.hora_salida = hora_salida
                tarifa = vehiculo.calcular_tarifa(self.tarifas)
                tiempo_estacionado = vehiculo.calcular_tiempo_estacionado()
                print(f"Tiempo estacionado: {tiempo_estacionado}, Tarifa: {tarifa}")
                self.vehiculos_estacionados.remove(vehiculo)
                print("Salida registrada exitosamente")
                return
        print("El vehículo no está registrado")

    def mostrar_vehiculos(self):
        if not self.vehiculos_estacionados:
            print("No hay vehículos estacionados")
            return
        for vehiculo in self.vehiculos_estacionados:
            hora_salida = vehiculo.hora_salida if vehiculo.hora_salida else "Aún estacionado"
            print(f"Placa: {vehiculo.placa}, Tipo: {vehiculo.tipo}, Hora de entrada: {vehiculo.hora_entrada}, Hora de salida: {hora_salida}")

    def verificar_disponibilidad(self):
        if len(self.vehiculos_estacionados) < self.capacidad_maxima:
            print("Espacio disponible")
            return True
        else:
            print("PARQUEADERO LLENO")
            return False
