# Ejercicio 1: Básico
print("Ejercicio 1: Básico")
for i in range(10):
    print(i)

# Ejercicio 2: Múltiples de 2
print("\nEjercicio 2: Múltiples de 2")
for i in range(2, 51, 2):
    print(i)

# Ejercicio 3: Contando Vanilla Ice
print("\nEjercicio 3: Contando Vanilla Ice")
for i in range(1, 51):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Ejercicio 4: Wow. Número gigante a la vista
print("\nEjercicio 4: Wow. Número gigante a la vista")
suma = 0
for i in range(0, 5001, 2):
    suma += i
print(suma)

# Ejercicio 5: Regrésame al 3
print("\nEjercicio 5: Regrésame al 3")
for i in range(99, 0, -3):
    print(i)

# Ejercicio 6: Contador dinámico
print("\nEjercicio 6: Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)