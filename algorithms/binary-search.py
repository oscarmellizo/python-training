def binary_search(arr, low, high, target):
    # Verifica si el subarray tiene al menos un elemento
    if high >= low:
        mid = (high + low) // 2
        
        # Si el elemento objetivo está en el medio, retorna su índice
        if arr[mid] == target:
            return mid
        
        # Si el elemento objetivo es menor que el valor medio, busca en la mitad izquierda
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        
        # Si el elemento objetivo es mayor que el valor medio, busca en la mitad derecha
        else:
            return binary_search(arr, mid + 1, high, target)
    
    else:
        # El elemento objetivo no está presente en el array
        return -1

# Ejemplo de uso
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Elemento encontrado en el índice:", result)
else:
    print("Elemento no encontrado en el array")
