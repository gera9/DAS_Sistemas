class Automovil:

    def __init__(self, Vel, Kilometraje_Marcado, Cupo_Max):
        self.Vel = Vel
        self.Kilometraje_Marcado = Kilometraje_Marcado
        self.Cupo_Max = Cupo_Max
   
    def Costo(self, Cupo_Max):
        Costo = self.Cupo_Max*100
        return Costo

    def Precio(self, Cupo_Max):
        Precio = self.Cupo_Max*100
        Precio1 = (Precio*.1) + Precio
        return Precio1 

    random=(50)

    def __str__(self):
       return f"AUTOMOVIL CON VELOCIDAD MAXIMA DE: {self.Vel}\n Kilometraje_Marcado MARCADO: {self.Kilometraje_Marcado}\n Cupo_Max TOTAL: {self.Cupo_Max}\n "

class Camion(Automovil):
    def __init__(self, Vel, Kilometraje_Marcado, Cupo_Max):
        Automovil.__init__(self, Vel, Kilometraje_Marcado, Cupo_Max)
    def __str__(self):
        return f"CAMION CON VELOCIDAD MAXIMA DE: {self.Vel}\n Kilometraje_Marcado MARCADO: {self.Kilometraje_Marcado}\n Cupo_Max TOTAL: {self.Cupo_Max}\n"

if __name__ == "__main__":
        Camion1=Camion(300,100000,45)
        Auto1=Automovil(150,3251212,4)
        Camion2=Camion(400,60000,50)
        Auto2=Automovil(100,5160,8)
        
        Lista_Chida = [Camion1,Auto1,Camion2,Auto2]

        for z in Lista_Chida:
            if isinstance(z, Camion):
                m = z.Precio(z.Cupo_Max)
                print(f"{z} EL TOTAL EN ESTA OCACION ES DE: {m} ")
            
            elif isinstance(z, Automovil):
                n = z.Costo(z.Cupo_Max)
                print(f"{z} EL TOTAL EN ESTA OCACION ES DE: {n} ")