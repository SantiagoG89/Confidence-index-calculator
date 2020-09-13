import pandas

class ICEA:
    def __init__(self, base, muestra):
        self.base = base
        self.muestra = muestra


    def setear_base(self):
        if self.muestra == 456:
            self.base = self.base[(self.base["AGRICULTURA"] == "Sí") | (self.base["AGRICULTURA"] == "Si")]


        if self.muestra == 415:
            self.base = self.base[(self.base["GANADERIA"] == "Sí") | (self.base["GANADERIA"] == "Si")]


        if self.muestra == 182:
            self.base = self.base[(self.base["TAMBO"] == "Sí") | (self.base["TAMBO"] == "Si")]



    def setear_muestra(self):

        if len(self.base.index) < self.muestra:
            self.muestra = len(self.base.index)
            self.base = self.base.sample(self.muestra)
        else:
            self.base = self.base.sample(self.muestra)



    def calcular_parcial_pais1(self):
        return 50 * (self.base["SIT PAIS 1"].value_counts()[
                         'Mejor'] / self.muestra
                     - self.base["SIT PAIS 1"].value_counts()[
                         'Peor'] / self.muestra + 1)

    def calcular_parcial_pais2(self):
        return 50 * (self.base["SIT PAIS 2"].value_counts()[
                         'Mejor'] / self.muestra
                     - self.base["SIT PAIS 2"].value_counts()[
                         'Peor'] / self.muestra + 1)

    def calcular_pais(self):
        return (self.calcular_parcial_pais1() + self.calcular_parcial_pais2())/2

    def calcular_parcial_empresa1(self):
        return 50 * (self.base["SIT EMPRESA 1"].value_counts()[
                         'Mejor'] / self.muestra
                     - self.base["SIT EMPRESA 1"].value_counts()[
                         'Peor'] / self.muestra + 1)

    def calcular_parcial_empresa2(self):
        return 50 * (self.base["SIT EMPRESA 2"].value_counts()[
                         'Mejor'] / self.muestra
                     - self.base["SIT EMPRESA 2"].value_counts()[
                         'Peor'] / self.muestra + 1)


    def calcular_empresa(self):
        return (self.calcular_parcial_empresa1() + self.calcular_parcial_empresa2())/2



    def calcular_parcial_agro1(self):
        return 50 * (self.base["SIT AGRO 1"].value_counts()[
                         'Bueno'] / self.muestra
                     - self.base["SIT AGRO 1"].value_counts()[
                         'Malo'] / self.muestra + 1)

    def calcular_parcial_agro2(self):
        return 50 * (self.base["SIT AGRO 2"].value_counts()[
                         'Mayor'] / self.muestra
                     - self.base["SIT AGRO 2"].value_counts()[
                         'Menor'] / self.muestra + 1)


    def calcular_agro(self):
        return (self.calcular_parcial_agro1() + self.calcular_parcial_agro2())/2

    def calcular_presente(self):
        return (self.calcular_parcial_agro1() + self.calcular_parcial_empresa1() + self.calcular_parcial_pais1())/3

    def calcular_expectativas(self):
        return (self.calcular_parcial_agro2() + self.calcular_parcial_empresa2() + self.calcular_parcial_pais2())/3

    def calcular_indice(self):
        return (self.calcular_pais() + self.calcular_empresa() + self.calcular_agro()) / 3


    def calcular_icea(self):
        self.setear_base()
        self.setear_muestra()

        return {"Índice general": [self.calcular_indice()],
                "Índice pais": [self.calcular_pais()],
                "Sit pais 1": [self.calcular_parcial_pais1()],
                "Sit pais 2": [self.calcular_parcial_pais2()],
                "Índice empresa": [self.calcular_empresa()],
                "Sit empresa 1": [self.calcular_parcial_empresa1()],
                "Sit empresa 2": [self.calcular_parcial_empresa2()],
                "Índice agro": [self.calcular_agro()],
                "Sit agro 1": [self.calcular_parcial_agro1()],
                "Sit agro 2": [self.calcular_parcial_agro2()],
                "Condiciones presentes": [self.calcular_presente()],
                "Expectativas": [self.calcular_expectativas()]}