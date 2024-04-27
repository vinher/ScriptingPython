import requests
#Script para generar consultas post des de python utilizado para mandar impresiones
nivel = 4
lista = ['A','B','A','B']
rack_id = 189
for i in range(nivel):
	#lista 	= ["A","B","C","D","E","F","G","H","I","J","K","L"]
	data 	= {"tipo":"Etiqueta","numero_rack":rack_id,"columna":lista[i],"nivel":nivel,"impresora":"192.168.14.38"}
	resp 	= requests.post('https://skynet.skytex.com.mx/imprimir/etiquetas/racks',data=data)
	print(resp.status_code)


