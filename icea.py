from clases.auxiliares import ICEA
import pandas
import random

#Muestras necesarias para los distintos ICEAS
mgeneral99 = 492
magro99 = 456
mgan99 = 415
mlech99 = 182
mvalles = 62
mparaguay = 35

running = True

print("Bienvenido al calculador de Índice de confianza del empresario agropecuario (ICEA), "
      "¿qué índice desea calcular?")
print("1 _ ICEA CREA (general + agr + gan + lech)")
print("2 _ ICEA Valles ")
print("3 _ ICEA Paraguay ")

while running:


    opcion = int(input("Elija opción: ")) - 1

    if opcion == 0:
            print("Escriba la ruta al archivo donde se encuentra la base de datos, tal como se baja de Encuesta Facil"
              " por ejemplo: C:/Users/user/Downloads/BASE_SEA_MAR20 v3(1).xlsx")
            ruta = input("Ruta: ")

            #Importacion y filtrado de las bases
            base = pandas.read_excel(ruta)
            columnas = (base.iloc[2].astype(str) + " " + base.iloc[3].astype(str)).str.replace("nan", '')
            base.columns = columnas
            base = base.drop([0, 1, 2, 3, 4, 5])

            basef = base[["REGION_CREA ", "SITUACION_PAIS PERCEPCION", " EXPECTATIVAS",
                          "SITUACION_EMPRESA PERCEPCION", "PERCEPCION_INVERSION ",
                          "EXPECTATIVAS_PRECIOS ", "ACT_AGRICOLA ", "ACT_GANADERA ",
                          "ACT_TAMBO "]].dropna()

            basef.columns = ["REGIÓN", "SIT PAIS 1", "SIT PAIS 2", "SIT EMPRESA 2", "SIT EMPRESA 1",  "SIT AGRO 1",
                             "SIT AGRO 2", "AGRICULTURA", "GANADERIA", "TAMBO"]



            #Creo los distintos ICEAS particulares a partir de la clase "ICEA"
            general = ICEA(basef, mgeneral99)
            agricultura = ICEA(basef, magro99)
            ganaderia = ICEA(basef, mgan99)
            lecheria = ICEA(basef, mlech99)

            #Se crea la tabla que contiene los resultados
            resultado = pandas.concat([pandas.DataFrame(general.calcular_icea()), pandas.DataFrame(agricultura.calcular_icea()),
                                       pandas.DataFrame(ganaderia.calcular_icea()), pandas.DataFrame(lecheria.calcular_icea())],
                                      axis=1)

            #Se manda el resultado a excel
            resultado.to_excel("C:/Users/user/Documents/RESULTADOS ICEA.xlsx")

            running = False

    if opcion == 1:
        print("Escriba la ruta al archivo donde se encuentra la base de datos, tal como se baja de Encuesta Facil"
              " por ejemplo: C:/Users/user/Downloads/BASE_SEA_MAR20 v3(1).xlsx")
        ruta = input("Ruta: ")

        # Importacion y filtrado de las bases

        base = pandas.read_excel(ruta)
        columnas = (base.iloc[2].astype(str) + " " + base.iloc[3].astype(str)).str.replace("nan", '')
        base.columns = columnas
        base = base.drop([0, 1, 2, 3, 4, 5])

        basef = base[["REGION_CREA ", "SITUACION_PAIS PERCEPCION", " EXPECTATIVAS",
                      "SITUACION_EMPRESA PERCEPCION", "PERCEPCION_INVERSION ",
                      "EXPECTATIVAS_PRECIOS "]].dropna()

        basef.columns = ["REGIÓN", "SIT PAIS 1", "SIT PAIS 2", "SIT EMPRESA 2", "SIT EMPRESA 1", "SIT AGRO 1",
                         "SIT AGRO 2"]

        # Creo los distintos ICEAS particulares a partir de la clase "ICEA"
        general = ICEA(basef, mvalles)


        # Se crea la tabla que contiene los resultados
        resultado = pandas.DataFrame(general.calcular_icea())

        # Se manda el resultado a excel
        resultado.to_excel("C:/Users/user/Documents/RESULTADOS ICEA.xlsx")

        running = False

    if opcion == 2:
        print("Escriba la ruta al archivo donde se encuentra la base de datos, tal como se baja de Encuesta Facil"
              " por ejemplo: C:/Users/user/Downloads/BASE_SEA_MAR20 v3(1).xlsx")
        ruta = input("Ruta: ")

        # Importacion y filtrado de las bases
        base = pandas.read_excel(ruta)
        columnas = (base.iloc[2].astype(str) + " " + base.iloc[3].astype(str)).str.replace("nan", '')
        base.columns = columnas
        base = base.drop([0, 1, 2, 3, 4, 5])

        basef = base[["SITUACION_PAIS PERCEPCION", " EXPECTATIVAS",
                      "SITUACION_EMPRESA PERCEPCION", "PERCEPCION_INVERSION ",
                      "EXPECTATIVAS_PRECIOS "]].dropna()

        basef.columns = ["SIT PAIS 1", "SIT PAIS 2", "SIT EMPRESA 2", "SIT EMPRESA 1", "SIT AGRO 1",
                         "SIT AGRO 2"]

        # Creo los distintos ICEAS particulares a partir de la clase "ICEA"
        general = ICEA(basef, mparaguay)


        # Se crea la tabla que contiene los resultados
        resultado = pandas.DataFrame(general.calcular_icea())

        # Se manda el resultado a excel
        resultado.to_excel("C:/Users/user/Documents/RESULTADOS ICEA.xlsx")

        running = False