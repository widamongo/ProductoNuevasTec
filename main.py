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


pseudocodigo del proyecto:

🔧 Inicialización
Definir lista vehículos_estacionados = []
Definir capacidad_maxima = número máximo de vehículos permitidos
Definir tarifas = {"Carro": tarifa_por_hora_carro, "Moto": tarifa_por_hora_moto}

🚗 Función: registrar_entrada()
Solicitar placa
Solicitar tipo de vehículo ("Carro" o "Moto")
Solicitar hora de entrada (formato HH:MM)

Si vehículo ya está en vehículos_estacionados:
    Mostrar "El vehículo ya está registrado"
    Salir

Si len(vehículos_estacionados) >= capacidad_maxima:
    Mostrar "PARQUEADERO LLENO"
    Salir

Crear tupla datos_inmutables = (placa, tipo)
Crear diccionario vehiculo = {
    "placa": placa,
    "tipo": tipo,
    "hora_entrada": hora_entrada,
    "hora_salida": None
}

Agregar vehiculo a vehículos_estacionados
Mostrar "Vehículo registrado exitosamente"



🕒 Función: registrar_salida()
Solicitar placa
Solicitar hora de salida (formato HH:MM)

Buscar vehículo en vehículos_estacionados por placa

Si no se encuentra:
    Mostrar "El vehículo no está registrado"
    Salir

Actualizar hora_salida en el diccionario del vehículo

Calcular tiempo_estacionado = hora_salida - hora_entrada
Calcular tarifa = tiempo_estacionado * tarifas[tipo]

Mostrar tiempo_estacionado y tarifa

Eliminar vehículo de vehículos_estacionados
Mostrar "Salida registrada exitosamente"



📋 Función: mostrar_vehículos_estacionados()
Si vehículos_estacionados está vacío:
    Mostrar "No hay vehículos estacionados"
    Salir

Para cada vehículo en vehículos_estacionados:
    Mostrar placa, tipo, hora_entrada, hora_salida


📦 Función: verificar_disponibilidad()
Si len(vehículos_estacionados) < capacidad_maxima:
    Mostrar "Espacio disponible"
    Retornar True
Sino:
    Mostrar "PARQUEADERO LLENO"
    Retornar False


POO

🧭 Ruta para desarrollar el proyecto con POO
1. Diseño de Clases
Define las clases principales que representarán los elementos del sistema:

🔹 Vehiculo
Atributos:
placa (str)
tipo (str: "Carro" o "Moto")
hora_entrada (datetime)
hora_salida (datetime o None)
Métodos:
calcular_tiempo_estacionado()
calcular_tarifa(tarifas)
🔹 Parqueadero
Atributos:
capacidad_maxima (int)
vehiculos_estacionados (list de objetos Vehiculo)
tarifas (dict: {"Carro": valor, "Moto": valor})
Métodos:
registrar_entrada(placa, tipo, hora)
registrar_salida(placa, hora)
mostrar_vehiculos()
verificar_disponibilidad()


2. Validaciones
Implementa validaciones dentro de los métodos:

Verificar si el vehículo ya está registrado.
Verificar si hay espacio disponible.
Verificar si el vehículo existe al registrar salida.

3. Interfaz de Usuario (CLI)
Crea un menú interactivo en consola para que el usuario pueda:

Registrar entrada
Registrar salida
Ver vehículos estacionados
Ver disponibilidad
Salir del programa
4. Manejo de Fechas y Horas
Usa el módulo datetime para convertir cadenas en objetos de hora y calcular diferencias.

5. Buenas Prácticas
Usa nombres de clases en PascalCase (Vehiculo, Parqueadero)
Usa nombres de métodos y variables en snake_case (registrar_entrada, hora_salida)
Documenta tus clases y métodos con docstrings
Maneja errores con try-except donde sea necesario
Separa tu código en módulos si crece mucho (por ejemplo, vehiculo.py, parqueadero.py, main.py)
6. Pruebas
Haz pruebas unitarias simples para verificar:

Registro correcto
Cálculo de tarifas
Validaciones

'''
from datetime import datetime
from Parqueadero import Parqueadero

def main():
    capacidad_maxima = 5
    tarifas = {"Carro": 2000, "Moto": 1000}
    parqueadero = Parqueadero(capacidad_maxima, tarifas)

    while True:
        print("\nMenú:")
        print("1. Registrar entrada")
        print("2. Registrar salida y generar cobro")
        print("3. Mostrar vehículos estacionados")
        print("4. Verificar disponibilidad")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            placa = input("Ingrese la placa del vehículo: ")
            tipo = input("Ingrese el tipo de vehículo (Carro/Moto): ")
            hora_entrada_str = input("Ingrese la hora de entrada (HH:MM): ")
            hora_entrada = datetime.strptime(hora_entrada_str, "%H:%M")
            parqueadero.registrar_entrada(placa, tipo, hora_entrada)

        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo: ")
            hora_salida_str = input("Ingrese la hora de salida (HH:MM): ")
            hora_salida = datetime.strptime(hora_salida_str, "%H:%M")
            parqueadero.registrar_salida(placa, hora_salida)

        elif opcion == "3":
            parqueadero.mostrar_vehiculos()

        elif opcion == "4":
            parqueadero.verificar_disponibilidad()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()

        

