#Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad = int(input("Por favor ingresa tu edad: "))

#Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca

permitido = True if edad >= 18 else False  #Esto se llama ternario

#Paso 3: Mostrar al usuario si el usuario puede o no ingresar a la discoteca

if permitido:
    print("Pueden ingresar")
else: 
    print("No puedes ingresar")

