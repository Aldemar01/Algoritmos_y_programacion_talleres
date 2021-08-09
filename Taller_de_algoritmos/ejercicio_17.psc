Algoritmo Distancia_vehiculos_minutos
	Escribir "Digite la velocidad del vehiculo que va adelante en Km/h " 
	Leer v1
	Escribir "Digite la velocidad del vehiculo que  por detras  en Km/h " 
	Leer v2 
	Escribir "Digite la distancia entre los vehiculos en Km" 
	leer dis
	vt<-(v2-v1)
	t<- dis/vt
	tm <- t*60
	Escribir "El tiempo en minutos en que el segundo vehiculo alcanza al primero es: " tm " minutos"	
FinAlgoritmo
