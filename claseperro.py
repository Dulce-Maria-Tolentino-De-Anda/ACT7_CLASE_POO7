print("programacion POO")
# definicion clase 
class Perro:
  # funciones dentro de la clases
   def morder (self):
        print ("el perro me mordio")
   def Datos_perro(self, nombre, edad):
        print(f" Nombre : {nombre} edad : {edad}")


#  zona de creacion de objeto
pitbull=Perro()


# zona de uso de objeto
pitbull.Datos_perro("bobby" , 4)
pitbull.morder()
