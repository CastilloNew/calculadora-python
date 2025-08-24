# Calculadora básica
# ¡Hola! Esta es una calculadora que hace operaciones matemáticas como las que aprendes en el colegio.

# Funciones para cada operación (cada una es como una máquina pequeña que hace una operación diferente)
def sumar(a, b):
    # Esta máquina suma dos números 
    return a + b  # Devuelve el resultado de la suma

def restar(a, b):
    # Esta máquina resta 
    return a - b  # Devuelve el resultado de la resta

def multiplicar(a, b):
    # Esta máquina multiplica 
    return a * b  # Devuelve el resultado de la multiplicación

def dividir(a, b):
    # Esta máquina divide, pero tiene cuidado con una cosa importante:
    if b != 0:  # Si el segundo número NO es cero (porque no se puede dividir entre cero)
        return a / b  # Devuelve el resultado de la división
    else:
        return "Error: No se puede dividir entre 0"  # ¡Cuidado! División entre cero no se puede

def potencia(a, b):
    # Esta máquina calcula potencias (como multiplicar un número por sí mismo varias veces)
    return a ** b  # Ejemplo: 2^3 = 2 × 2 × 2 = 8

def porcentaje(a, b):
    # Esta máquina calcula porcentajes (como calcular el 10% de 100)
    return (a * b) / 100  # Ejemplo: 20% de 50 = (20 × 50) ÷ 100 = 10

# ¡Ahora empieza la parte divertida! La calculadora se enciende:
while True:  # Esto significa "repetir para siempre"
    print("\n--- Calculadora ---")  # Dibujamos un título bonito
    print("Opciones:")  # Mostramos las opciones como un menú 
    print("1. Sumar")           
    print("2. Restar")          
    print("3. Multiplicar")     
    print("4. Dividir")         
    print("5. Potencia")        
    print("6. Porcentaje")      
    print("7. Salir")           
    
    opcion = input("Elige una opción (1-7): ")  # Preguntamos qué quiere hacer
    
    if opcion == "7":  # Si elige 7...
        print("¡Adiós!")  # Nos despedimos
        break  # Y apagamos la calculadora

    # Si eligió una operación matemática (1-6):
    if opcion in ["1","2","3","4","5","6"]:
        # Pedimos los números :
        num1 = float(input("Ingresa el primer número: "))  # Primer número
        num2 = float(input("Ingresa el segundo número: ")) # Segundo número

        # ¡Ahora usamos la máquina correspondiente!
        if opcion == "1":
            print("Resultado:", sumar(num1, num2))  # Usamos la máquina de sumar
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))  # Usamos la máquina de restar
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))  # Usamos la máquina de multiplicar
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))  # Usamos la máquina de dividir
        elif opcion == "5":
            print("Resultado:", potencia(num1, num2))  # Usamos la máquina de potencias
        elif opcion == "6":
            print("Resultado:", porcentaje(num1, num2))  # Usamos la máquina de porcentajes
    else:
        print("Opción inválida, intenta de nuevo.")  # ¡Ups! Número equivocado