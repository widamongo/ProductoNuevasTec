'''


El objetivo de este proyecto es desarrollar un sistema de administración para un parqueadero que permita gestionar de manera eficiente la entrada y salida de vehículos (carros y motos). El sistema debe registrar la información relevante de los vehículos, como el tipo de vehículo (carro o moto), la placa, y las horas de entrada y salida. Este proyecto tiene como fin consolidar los conocimientos adquiridos en el curso, utilizando herramientas y conceptos de programación en Python, tales como listas, diccionarios, y tuplas.

Requisitos del Programa:

1.	Estructura de Datos:
o	Utiliza listas para almacenar los vehículos estacionados. Cada vehículo debe ser representado como un diccionario con los siguientes campos:
	Placa (cadena de texto)
	Tipo de vehículo (cadena de texto: "Carro" o "Moto")
	Hora de entrada (hora en formato HH:MM)
	Hora de salida (hora en formato HH:MM, si ya ha salido)
o	Utiliza tuplas para almacenar los datos inmutables del vehículo (como la placa y el tipo de vehículo).
2.	Funcionalidades:
o	Registro de vehículos:

	Al ingresar un vehículo, el sistema debe pedir la placa, el tipo de vehículo (carro o moto) y la hora de entrada.
	El vehículo debe ser añadido a la lista de vehículos estacionados y asignado a un espacio disponible.
o	Registro de salida:
	Al registrar la salida de un vehículo, el sistema debe pedir la placa y la hora de salida.
	El vehículo debe ser removido de la lista de estacionados y el sistema debe calcular el tiempo que estuvo estacionado (diferencia entre la hora de entrada y salida).
o	Visualización de vehículos estacionados:
	El sistema debe permitir visualizar todos los vehículos actualmente estacionados, mostrando su placa, tipo de vehículo, hora de entrada y hora de salida (si ya ha salido).
o	Control de capacidad:
	El parqueadero tiene una capacidad máxima de vehículos (carros y motos). Si el parqueadero está lleno, el sistema debe mostrar el mensaje: "PARQUEADERO LLENO".
o	Verificación de disponibilidad de espacio:
	El sistema debe comprobar si hay espacios disponibles antes de permitir el ingreso de un vehículo.
3.	Requisitos Adicionales:
o	Validaciones:
	No se debe permitir que un vehículo se registre si ya está estacionado.
	No se debe permitir el registro de salida de un vehículo que no esté estacionado.
	No se puede permitir el ingreso de un vehículo si no hay espacio disponible en el parqueadero.
o	Cálculo de tarifas:
	Implementa un sistema de tarifas por hora, donde el costo de la estancia de un vehículo se calcule según su tipo (carro o moto) y el tiempo que estuvo estacionado.
o	Informe de actividades (Opcional):

	Desarrolla una funcionalidad que permita generar un informe detallado de las actividades del parqueadero. Este informe debe mostrar la información relevante, como vehículos registrados, tiempos de estancia, tarifas cobradas, entre otros.

Consideraciones:

•	El sistema debe ser flexible y fácil de mantener.
•	Asegúrese de realizar pruebas adecuadas para verificar que todas las funcionalidades estén implementadas correctamente.

Este proyecto les brindará la oportunidad de aplicar los conceptos aprendidos en el curso, al mismo tiempo que desarrollan una solución práctica y funcional

'''
import datetime
from typing import List, Dict, Tuple
# Definición de constantes
maximaCapacidad = 10  # Capacidad máxima del parqueadero
# Estructura de datos para almacenar los vehículos
vehiculosEstacionados: List[Dict[str, str]] = []
tarifas = {'Carro': 5000, 'Moto': 3000}  # Tarifas por hora
# Función para registrar la entrada de un vehículo
def registrarEntrada(placa: str, tipo: str, horaEntrada: str) -> None:
    if len(vehiculosEstacionados) >= maximaCapacidad:
        print("PARQUEADERO LLENO")
        return
    for vehiculo in vehiculosEstacionados:
        if vehiculo['Placa'] == placa:
            print("El vehículo ya está estacionado.")
            return
    horaEntradaObj = datetime.datetime.strptime(horaEntrada, "%H:%M")
    vehiculo = {
        'Placa': placa,
        'Tipo': tipo,
        'HoraEntrada': horaEntradaObj,
        'HoraSalida': None
    }
    vehiculosEstacionados.append(vehiculo)
    print(f"Vehículo {placa} registrado a las {horaEntrada}.")