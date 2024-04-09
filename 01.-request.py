import requests
#Script para generar consultas post des de python utilizado para mandar impresiones

for i in range(7):
	#lista 	= ["A","B","C","D","E","F","G","H","I","J","K","L"]
	data 	= {"tipo":"Etiqueta","numero_rack":"180","columna":lista[i],"nivel":"2","impresora":"ip impresora"}
	resp 	= requests.post('url_peticion',data=data)
	print(resp.status_code)



