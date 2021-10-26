class Cheltuiala:

    def __init__(self, id_cheltuiala, suma, desc, data):
        self.id_cheltuiala = id_cheltuiala # name mangling folosind __: self.__id_cheltuiala
        self.suma = suma
        self.descriere = desc
        self.data = data

    def get_suma(self):
        return self.suma

    def set_suma(self, suma):
        if abs(suma) > 10000:
            raise ValueError('Valoarea sumei este prea mare!')
        self.suma = suma

    def __str__(self):
        return f'id={self.id_cheltuiala}, desc={self.descriere}, suma={self.suma}, data={self.data}'

    def __repr__(self):
        return str(self)