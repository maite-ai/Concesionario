class Auto:
	new = True
	motor = False
	
	def __init__(self, marca, modelo, generacion, serie, cilindrada, matricula, nro_chasis, equipamiento):
		self.marca = marca
		self.modelo = modelo
		self.generacion = generacion
		self.serie = serie
		self.cilindrada = cilindrada
		self.matricula =  matricula
		self.nro_chasis = nro_chasis
		self.equipamiento = equipamiento

	def arrancar(self, motor):
		if motor:
			motor = False
		else:
			motor = True

	def detener(self, motor):
		motor = True

	def show(self):
		print(f"Nuevo auto ingresado \nMarca: {self.marca}\nModelo: {self.modelo}\nGeneración: {self.generacion}\nSerie: {self.serie}\nCilindrada: {self.cilindrada}\nMatrícula: {self.matricula}\nN° de chasis: {self.nro_chasis}\nEquipamiento: {self.equipamiento}")
	
auto1 = Auto("Honda", "City", "GX 2014", "Sedán 4 puertas", 1.6, "AF 566 IA", "472254152574", "Básico")

auto1.show()