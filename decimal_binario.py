def decimal_binario(num_decimal):
    num_decimal = int(num_decimal)
    if num_decimal == 0:
        return "0"
    
    binario = ""
    while num_decimal > 0:
        resto = num_decimal % 2
        binario = str(resto) + binario
        num_decimal = num_decimal // 2
    return binario

def binario_decimal(num_binario):
    decimal = 0
    longitud = len(num_binario)

    for i in range(longitud):
        bit = num_binario[i]
        if bit == '1':
            decimal += 2 ** (longitud - 1 - i)
        elif bit != '0':
            raise ValueError("El número binario ingresado es inválido.")
    return decimal

def validar_decimal(num_decimal):
    try:
        num = int(num_decimal)
        if num < 0:
            print("El número debe ser positivo.")
            return False
        return True
    except ValueError:
        print("Por favor, ingresar un número entero válido.")
        return False

def validar_binario(num_binario):
    for bit in num_binario:
        if bit not in ('0', '1'):
            print("Número o caracteres no válidos. Solo se aceptan 0 y 1.")
            return False
    return True



opcion = input("Elija una opción: \n1 - Decimal a binario \n2 - Binario a decimal\n")

if opcion == '1':
    num_decimal = input("Ingrese un número decimal: ")
    if validar_decimal(num_decimal):
        num_binario = decimal_binario(num_decimal)
        print(f"El número {num_decimal} en binario es: {num_binario}")

elif opcion == '2':
    num_binario = input("Ingrese un número binario: ")
    if validar_binario(num_binario):
        try:
            num_decimal = binario_decimal(num_binario)
            print(f"El número {num_binario} en decimal es: {num_decimal}")
        except ValueError as e:
            print(e)

else:
    print("Opción inválida. Por favor, elija 1 o 2.")