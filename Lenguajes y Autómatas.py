import re

entrada = input("Ingrese el texto Deseado: ")

opcion = int(input("Seleccione lo que desea encontrar en el Texto:" 
+ "\n1. Todas las palabras que tengan una longitud de 7 o más letras"
+ "\n2. Expresiones que NO finalicen con una vocal."
+ "\n3. Las palabras que inicien con ""M"" donde la segunda letra no sea vocal"
+ "\n4. Expresiones encerradas entre comillas"
+ "\n5. Ip’s"
+ "\n6. Horas"
+ "\n7. Telefonos"
+ "\n8. Correos electrónicos"
+ "\n9. Url’s"
+ "\n10. Código postal"
+ "\nOpcion= "))

if opcion == 1:
	print("Todas las palabras que tengan una longitud de 7 o más letras")
	#entre las letras pueden encontrarse acentuadas o con ñÑ
	busqueda = re.findall("[a-zA-Z_ÑñÁáÉéÍíÓóÚú]{7,}",entrada)
	print(busqueda)

elif opcion ==2:
	print("Expresiones que NO finalicen con una vocal.")
	busqueda = re.findall(r"\w+[b-df-hj-np-tv-z]\b",entrada)
	print(busqueda)

elif opcion == 3:
	print("Las palabras que inicien con ""M"" donde la segunda letra no sea vocal")
	#Pueden iniciar con M o m y la segunda letra en consonante
	busqueda = re.findall('[Mm][^aeiou][a-z]*',entrada)
	print(busqueda)

elif opcion == 4:
	print("Expresiones encerradas entre comillas")
	busqueda = re.findall(r"(\"[\w\s]+\")",entrada)
	print(busqueda)

elif opcion == 5:
    print("Ip´s")
    busqueda = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", entrada)
    print(busqueda)

elif opcion == 6:
	print("Horas")
	#para formato de 24 horas
	busqueda = re.findall("(?:[01]\d|2[0-3]):[0-5]\d",entrada)
	print(busqueda)

elif opcion == 7:
	print("Telefonos")
	#numeros seguidos 1234567891
	busqueda = re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',entrada)
	print(busqueda)

elif opcion == 8:
    print("Correos electronicos")
    busqueda = re.findall(r'[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}', entrada)
    print(busqueda)

elif opcion == 9:
    print("Url´s")
    busqueda = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', entrada)
    print(busqueda)
	
elif opcion == 10:
	print("Código postal")
	#codigos postales en el interior del país México son de 5 dígitos
	busqueda = re.findall(r"\d{5,5}",entrada)
	print(busqueda)

else:
	print("VALOR FUERA DE RANGO")
