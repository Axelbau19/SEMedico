
from experta import  *
#Creacion de nuestra variables
#lista
listaEnfermedad = []
sintomasDeenfermedad = []
mapeoSintomas = {}
diccionarioDescripcionEnfermedad = {}

def procesarInformacion():
    global  listaEnfermedad,sintomasDeenfermedad,mapeoSintomas,diccionarioDescripcionEnfermedad
    #Abrimos el fichero y guardaremos el contenido
    #puntero
    enfermedades = open("enfermedades.txt")
    #Guardar el contenido
    enfermedadesTexto = enfermedades.read()
    listaEnfermedad = enfermedadesTexto.split("\n")
    enfermedades.close()
    for enfermedad in listaEnfermedad:
        enfermedad_textoArchivo = open("SintomasEnfermedad/" + enfermedad +".txt")
        enfermedadSintomasData = enfermedad_textoArchivo.read()
        sintomasLista=enfermedadSintomasData.split("\n")
        sintomasDeenfermedad.append(sintomasLista)
        mapeoSintomas[str(sintomasLista)]= enfermedad
        enfermedad_textoArchivo.close()
        enfermedadArchivo= open("DescripcionEnfermedad/"+enfermedad+".txt")
        enfermedadesData = enfermedadArchivo.read()
        diccionarioDescripcionEnfermedad[enfermedad] = enfermedadesData
        enfermedadArchivo.close()
#
def identificarEnfermedad(*arguments):
    listaSintomas = []
    for sintoma in arguments:
        listaSintomas.append(sintoma)

    return mapeoSintomas[str(listaSintomas)]

def detallesEnfermedad(enfermedad):
    return diccionarioDescripcionEnfermedad[enfermedad]

def siNohayMatch(enfermedad):
    print("")
    idEnfermedad = enfermedad
    descripcionEnfermedad=detallesEnfermedad(idEnfermedad)
    print("")
    print("Puede ser que la enfermedad que tiene el paciente es: %s\n"%(idEnfermedad))
    print("Descripcion de la enfermedad: \n")
    print(descripcionEnfermedad+"\n")

class Diagnostico(Fact):
    pass


class SistemaMedico(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hola, Soy el doctor Neskz y estoy aqui para ayudarte y cuidar de tu salud")
        print("Me gustaria preguntarte sobre la condición de tu salud ")
        print("Sientes algunos de los siguientes sintomas")
        print("")
        yield Diagnostico(action="buscarEnfermedad")

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(cubiertoPuntos=W())),salience=1)
    def sintoma0(self):
        self.declare(Diagnostico(cubiertoPuntos=input("¿Esta cubierto de puntos?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(temperaturaAlta=W())),salience=1)
    def sintoma1(self):
        self.declare(Diagnostico(temperaturaAlta=input("¿Tiene temperatura alta?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(ojosRojos=W())),salience=1)
    def sintoma2(self):
        self.declare(Diagnostico(ojosRojos=input("¿Tiene los ojos rojos?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(tosSeca=W())),salience=1)
    def sintoma3(self):
        self.declare(Diagnostico(tosSeca=input("¿Tiene tos seca?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(dolorArticulacion=W())),salience=1)
    def sintoma4(self):
        self.declare(Diagnostico(dolorArticulacion=input("¿Tiene dolor de articulación?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(muchoEstornudo=W())),salience=1)
    def sintoma5(self):
        self.declare(Diagnostico(muchoEstornudo=input("¿Tiene mucho estornudo?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(dolorCabeza=W())),salience=1)
    def sintoma6(self):
        self.declare(Diagnostico(dolorCabeza=input("¿Tiene dolor de cabeza?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(temblorViolento=W())),salience=1)
    def sintoma7(self):
        self.declare(Diagnostico(temblorViolento=input("¿Tiembla violentamente?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(escalofrios=W())),salience=1)
    def sintoma8(self):
        self.declare(Diagnostico(escalofrios=input("¿Tiene escalofrios?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(cuerpoCortado=W())),salience=1)
    def sintoma9(self):
        self.declare(Diagnostico(cuerpoCortado=input("¿Tiene cuerpo cortado?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(faltaApetito=W())),salience=1)
    def sintoma10(self):
        self.declare(Diagnostico(faltaApetito=input("¿Tiene falta de apetito?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(dolorAbdominal=W())),salience=1)
    def sintoma11(self):
        self.declare(Diagnostico(dolorAbdominal=input("¿Tiene dolor abdominal?: ")))

    @Rule(Diagnostico(action='buscarEnfermedad'), NOT(Diagnostico(diarrea=W())),salience=1)
    def sintoma12(self):
        self.declare(Diagnostico(diarrea=input("¿Tiene diarrea?: ")))

    @Rule(Diagnostico(action="buscarEnfermedad"),Diagnostico(cubiertoPuntos="si"),Diagnostico(temperaturaAlta="si"),Diagnostico(ojosRojos="si"),Diagnostico(tosSeca="si"),Diagnostico(dolorArticulacion="no"),Diagnostico(muchoEstornudo="no"),Diagnostico(dolorCabeza="no"),Diagnostico(temblorViolento="no"),Diagnostico(escalofrios="no"),Diagnostico(cuerpoCortado="no"),Diagnostico(faltaApetito="no"),Diagnostico(dolorAbdominal="no"),Diagnostico(diarrea="no"))
    def enfermedad0(self):
        self.declare(Diagnostico(enfermedad="Sarampion"))

    @Rule(Diagnostico(action="buscarEnfermedad"),Diagnostico(cubiertoPuntos="no"),Diagnostico(temperaturaAlta="no"),Diagnostico(ojosRojos="no"),Diagnostico(tosSeca="no"),Diagnostico(dolorArticulacion="si"),Diagnostico(muchoEstornudo="si"),Diagnostico(dolorCabeza="si"),Diagnostico(temblorViolento="no"),Diagnostico(escalofrios="no"),Diagnostico(cuerpoCortado="no"),Diagnostico(faltaApetito="no"),Diagnostico(dolorAbdominal="no"),Diagnostico(diarrea="no"))
    def enfermedad1(self):
        self.declare(Diagnostico(enfermedad="Influenza"))

    @Rule(Diagnostico(action="buscarEnfermedad"),Diagnostico(cubiertoPuntos="no"),Diagnostico(temperaturaAlta="si"),Diagnostico(ojosRojos="no"),Diagnostico(tosSeca="no"),Diagnostico(dolorArticulacion="si"),Diagnostico(muchoEstornudo="no"),Diagnostico(dolorCabeza="no"),Diagnostico(temblorViolento="si"),Diagnostico(escalofrios="si"),Diagnostico(cuerpoCortado="no"),Diagnostico(faltaApetito="no"),Diagnostico(dolorAbdominal="no"),Diagnostico(diarrea="no"))
    def enfermedad2(self):
        self.declare(Diagnostico(enfermedad="Malaria"))

    @Rule(Diagnostico(action="buscarEnfermedad"),Diagnostico(cubiertoPuntos="no"),Diagnostico(temperaturaAlta="si"),Diagnostico(ojosRojos="no"),Diagnostico(tosSeca="no"),Diagnostico(dolorArticulacion="no"),Diagnostico(muchoEstornudo="no"),Diagnostico(dolorCabeza="si"),Diagnostico(temblorViolento="no"),Diagnostico(escalofrios="no"),Diagnostico(cuerpoCortado="si"),Diagnostico(faltaApetito="no"),Diagnostico(dolorAbdominal="no"),Diagnostico(diarrea="no"))
    def enfermedad3(self):
        self.declare(Diagnostico(enfermedad="Gripe"))

    @Rule(Diagnostico(action="buscarEnfermedad"),Diagnostico(cubiertoPuntos="no"),Diagnostico(temperaturaAlta="si"),Diagnostico(ojosRojos="no"),Diagnostico(tosSeca="no"),Diagnostico(dolorArticulacion="no"),Diagnostico(muchoEstornudo="no"),Diagnostico(dolorCabeza="si"),Diagnostico(temblorViolento="no"),Diagnostico(escalofrios="no"),Diagnostico(cuerpoCortado="no"),Diagnostico(faltaApetito="si"),Diagnostico(dolorAbdominal="si"),Diagnostico(diarrea="si"))
    def enfermedad4(self):
        self.declare(Diagnostico(enfermedad="Tifoidea"))

    @Rule(Diagnostico(action="buscarEnfermedad"),Diagnostico(enfermedad=MATCH.enfermedad),salience= -998)
    def enfermedad(self,enfermedad):
        print("")
        idEnfermedad = enfermedad
        descripcionEnfermedad = detallesEnfermedad(idEnfermedad)
        print("")
        print("Puede ser que la enfermedad que tiene el paciente es: %s\n" % (idEnfermedad))
        print("Descripcion de la enfermedad: \n")
        print(descripcionEnfermedad + "\n")

    @Rule(Diagnostico(action="buscarEnfermedad"),
          Diagnostico(cubiertoPuntos=MATCH.cubiertoPuntos),
          Diagnostico(ojosRojos=MATCH.ojosRojos),
          Diagnostico(tosSeca=MATCH.tosSeca),
          Diagnostico(dolorArticulacion=MATCH.dolorArticulacion),
          Diagnostico(muchoEstornudo=MATCH.muchoEstornudo),
          Diagnostico(dolorCabeza=MATCH.dolorCabeza),
          Diagnostico(temblorViolento=MATCH.temblorViolento),
          Diagnostico(escalofrios=MATCH.escalofrios),
          Diagnostico(cuerpoCortado=MATCH.cuerpoCortado),
          Diagnostico(dolorAbdominal=MATCH.dolorAbdominal),
          Diagnostico(diarrea=MATCH.diarrea),
          NOT(Diagnostico(enfermedad=MATCH.enfermedad)),salience= - 999)
    def notMatche(self,cubiertoPuntos,ojosRojos,tosSeca,dolorArticulacion,muchoEstornudo,dolorCabeza,temblorViolento,escalofrios,cuerpoCortado,dolorAbdominal,diarrea):
        print("\nNo se encontro ninguna enfermedad con los sintomas anteriores")
        lista = [cubiertoPuntos,ojosRojos,tosSeca,dolorArticulacion,muchoEstornudo,dolorCabeza,temblorViolento,escalofrios,cuerpoCortado,dolorAbdominal,diarrea]
        maxCuenta = 0
        maximaEnferemdad = ""
        for key,val in mapeoSintomas.items():
            cuenta= 0
            lista2 = eval(key)
            for j in range(0,len(lista)):
                if(lista2[j] == lista[j] and lista[j] == "si"):
                    cuenta+=1
            if cuenta > maxCuenta:
                maxCuenta = cuenta
                maximaEnferemdad = val
        siNohayMatch(maximaEnferemdad)







if __name__ == "__main__":
    procesarInformacion()
    motor = SistemaMedico()
    while(1):
        motor.reset()
        motor.run()
        print("¿Le gustaria diagnosticar otro sintomas?")
        if input()=="no":
          exit()

