# Juego del Ahorcado - Avance básico
# Estructuras: decisiones (if/elif/else) y repetitivas (while)
# Comentarios añadidos para comprensión

# Palabra fija (simple). Se puede cambiar o leer desde input si se desea.
palabra = "CASA".upper()

# Construimos la "máscara" con guiones bajos (mismo tamaño que la palabra)
mascara = "_" * len(palabra)

# Cantidad de intentos permitidos
intentos = 6

# Conjunto para guardar letras ya probadas
probadas = set()

print("=== Ahorcado (avance) ===")
print("Pista:", " ".join(mascara))
print("Intentos:", intentos)

# Bucle principal: se repite mientras queden intentos y no se haya adivinado
while intentos > 0 and mascara != palabra:
    letra = input("Ingrese una letra: ").strip().upper()

    # Validaciones simples
    if len(letra) != 1 or not letra.isalpha():
        print("Ingrese SOLO una letra A-Z.")
        continue

    if letra in probadas:
        print("Ya probaste esa letra. Intenta otra.")
        continue

    probadas.add(letra)

    # Verificamos si la letra está en la palabra
    if letra in palabra:
        # Construimos una nueva máscara revelando las posiciones correctas
        nueva = list(mascara)
        for i, ch in enumerate(palabra):
            if ch == letra:
                nueva[i] = letra
        mascara = "".join(nueva)
        print("¡Bien! Ahora:", " ".join(mascara))
    else:
        intentos -= 1
        print("Letra incorrecta. Intentos restantes:", intentos)

# Salida final
if mascara == palabra:
    print("¡Ganaste! La palabra era:", palabra)
else:
    print("Perdiste. La palabra era:", palabra)
