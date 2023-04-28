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
		print(f"Nuevo auto ingresado \nMarca: {self.marca}\n  modelo: {self.modelo}\n Generación: {self.generacion}\n Serie: {self.serie}\n Cilindrada: {self.cilindrada}\n Matrícula: {self.matricula}\n N° de chasis: {self.nro_chasis}\n Equipamiento: {self.equipamiento}")
	