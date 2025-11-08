
"""
Proyecto: Casa Inteligente con Dispositivos

Autor: [Alonso Jaen Elisa Damari, Ceron Dauzon Jorge Uriel, Nevraumont Ceballos Sara Crystel, Trujillo Franco Karla Yorleni, Zamora Toral Fernanda]
Materia: [Programacion orientada a Objetos]
Fecha: [7/NOV/2025]
Descripción:
Este programa simula una casa inteligente con distintos tipos de dispositivos.
Se implementa una clase abstracta base y varias subclases concretas. Además,
se modela una clase CasaInteligente que controla los dispositivos y ejecuta
escenas automáticas basadas en condiciones.
"""


# Importaciones necesarias

from abc import ABC, abstractmethod

# Clase abstracta 
class Dispositivo(ABC):

    def __init__(self, id_dispositivo):
        self.__id_dispositivo = id_dispositivo   # Atributo privado
        self.__estado = False                    # False = apagado, True = encendido
    
    
    # Métodos abstractos
    
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def mostrar_datos(self):
        pass

    
    # Métodos comunes (no abstractos)
   
    def get_id(self):
        """Devuelve el identificador"""
        return self.__id_dispositivo

    def get_estado(self):
        """Devuelve el estado actual"""
        return self.__estado

    def set_estado(self, estado):
        """Cambia el estado"""
        self.__estado = estado


# Subclase LuzInteligente

class LuzInteligente(Dispositivo):
    """
    con control de intensidad.
    """
    def __init__(self, id_dispositivo, intensidad=0):
        super().__init__(id_dispositivo)
        self.intensidad = intensidad  # 0 a 100 %

    def encender(self):
        self.set_estado(True)
        self.intensidad = 80  # Intensidad por defecto al encender
        print(f"Luz {self.get_id()} encendida con intensidad {self.intensidad}%")

    def apagar(self):
        self.set_estado(False)
        self.intensidad = 0
        print(f"Luz {self.get_id()} apagada.")

    def mostrar_datos(self):
        estado = "Encendida" if self.get_estado() else "Apagada"
        print(f"[Luz Inteligente] ID: {self.get_id()} | Estado: {estado} | Intensidad: {self.intensidad}%")


# Subclase CamaraSeguridad

class CamaraSeguridad(Dispositivo):
    """
    Representa una cámara de seguridad con estado de grabación.
    """
    def __init__(self, id_dispositivo, grabando=False):
        super().__init__(id_dispositivo)
        self.grabando = grabando

    def encender(self):
        self.set_estado(True)
        self.grabando = True
        print(f"Cámara {self.get_id()} encendida y grabando.")

    def apagar(self):
        self.set_estado(False)
        self.grabando = False
        print(f"Cámara {self.get_id()} apagada.")

    def mostrar_datos(self):
        estado = "Encendida" if self.get_estado() else "Apagada"
        grabacion = "Grabando" if self.grabando else "Inactiva"
        print(f"[Cámara Seguridad] ID: {self.get_id()} | Estado: {estado} | {grabacion}")


# Subclase SensorMovimiento

class SensorMovimiento(Dispositivo):
    """
    Representa un sensor de movimiento
    """
    def __init__(self, id_dispositivo, movimiento_detectado=False):
        super().__init__(id_dispositivo)
        self.movimiento_detectado = movimiento_detectado

    def encender(self):
        self.set_estado(True)
        print(f"Sensor {self.get_id()} activado.")

    def apagar(self):
        self.set_estado(False)
        print(f"Sensor {self.get_id()} desactivado.")

    def detectar_movimiento(self):
        
        """Simula la detección de movimiento."""
        if self.get_estado():
            self.movimiento_detectado = True
            print(f"Sensor {self.get_id()} ha detectado movimiento.")
        else:
            print(f"Sensor {self.get_id()} está apagado, no puede detectar movimiento.")

    def mostrar_datos(self):
        estado = "Encendido" if self.get_estado() else "Apagado"
        movimiento = "Sí" if self.movimiento_detectado else "No"
        print(f"[Sensor Movimiento] ID: {self.get_id()} | Estado: {estado} | Movimiento detectado: {movimiento}")


# (Composición de la casa inteligente)

class CasaInteligente:
    """
    Representa una casa inteligente que contiene múltiples dispositivos.
    """
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        
        """Agrega un nuevo dispositivo a la casa."""
        
        self.dispositivos.append(dispositivo)
        print(f"Dispositivo '{dispositivo.get_id()}' agregado a la casa.")

    def mostrar_todos(self):
        
        """Muestra la información de los dispositivos."""
        
        print("\n=== Estado de todos los dispositivos ===")
        for disp in self.dispositivos:
            disp.mostrar_datos()

    def ejecutar_escena(self):
        """
        Escena automática:
        Si algún sensor detecta movimiento → encender luces y cámaras.
        """
        print("\n=== Ejecutando escena automática ===")
        for disp in self.dispositivos:
            if isinstance(disp, SensorMovimiento) and disp.movimiento_detectado:
                print(f"Acción: Movimiento detectado por {disp.get_id()} → Encendiendo luces y cámaras.")
                for d in self.dispositivos:
                    if isinstance(d, LuzInteligente):
                        d.encender()
                    elif isinstance(d, CamaraSeguridad):
                        d.encender()
                break  # Ejecutar solo una vez al detectar movimiento


# Simulación principal

if __name__ == "__main__":
    
    # Crear la casa inteligente
    casa = CasaInteligente()

    # Crear dispositivos
    luz1 = LuzInteligente("Luz_Sala")
    luz2 = LuzInteligente("Luz_Cocina")
    cam1 = CamaraSeguridad("Camara_Entrada")
    sensor1 = SensorMovimiento("Sensor_Pasillo")
    sensor2 = SensorMovimiento("Sensor_Patio")

    # Agregar los dispositivos a la casa
    casa.agregar_dispositivo(luz1)
    casa.agregar_dispositivo(luz2)
    casa.agregar_dispositivo(cam1)
    casa.agregar_dispositivo(sensor1)
    casa.agregar_dispositivo(sensor2)

    # Encender algunos dispositivos
    sensor1.encender()
    sensor2.encender()

    # Simular detección de movimiento
    sensor1.detectar_movimiento()

    # Mostrar el estado inicial
    casa.mostrar_todos()

    # Ejecutar la escena automática
    casa.ejecutar_escena()

    # Mostrar el estado final
    casa.mostrar_todos()
