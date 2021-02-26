import time

# OBJETOS PRINCIPALES SERVIDOR Y APLICACION
class Aplicacion(object):
    proceso=(5+1)
    tiempoProceso = 5 #segundos
    ID="Suma App"
    status=False 

class Servidor(object):
    AppLimite=False
    App=1
    tiempoEjecucion = 6 #segundos
    nombre = "Servidor 1"
    app = Aplicacion()

#METODO PARA OPERAR LA SIMULACION 
def SIMULACION(AplicacionCantidad):
    for x in range(1,(AplicacionCantidad+1)):
        print("_____________________________________________________________")
        SERVIDOR = Servidor()
        print("Aplicacion " + str(x)+" de "+str(AplicacionCantidad) + " activa en " + SERVIDOR.nombre)
        tiempo = SERVIDOR.app.tiempoProceso/100
        puntos=""
        porcentajeAvance=1
        tiempoEjecucionApp = tiempo
        for i in range(1,100):
            puntos=puntos+"."
            porcentajeAvance=porcentajeAvance+1
            tiempoEjecucionApp=tiempoEjecucionApp+tiempo
            print("Proceso: "+str(porcentajeAvance)+"% tiempo "+"{:.2f}".format(tiempoEjecucionApp)+" seg "+puntos, end="")
            print('', end='')
            print('\r', end='', flush=True)
            time.sleep(tiempo)
        print("")
        print("FIN")
        if x < AplicacionCantidad:
            print("en cola: Aplicacion "+str(x+1))
        time.sleep(Servidor.tiempoEjecucion - Servidor.app.tiempoProceso)
        if x == AplicacionCantidad: 
            print("FIN DE LA SIMULACION")
            RESULTADOS((60/Servidor.app.tiempoProceso),(60/Servidor.tiempoEjecucion))

#METODO PARA MOSTRAR LOS RESULTADOS DE LA SIMULACION 
def RESULTADOS(MU, LAMBDA):
    #NO uso del sistema
    PO= 1-(LAMBDA/MU)
    WS= 1/(MU-LAMBDA)
    print('{:^20}{:^20}{:^20}'.format("Tiempo","No uso sistema","Tiempo de espera"))
    print('{:^20}{:^20.2f}{:^20.2f}'.format("Segundos",float(PO),float(WS)))
    print('{:^20}{:^20.2f}{:^20.2f}'.format("Minutos",float(PO*60),float(WS*60)))

#PROGRAMA
AplicacionesASimular= int(input("Ingresa la cantidad de aplicaciones: "))
SIMULACION(AplicacionesASimular)