def knapsack_01(values, weights, capacity):
    n = len(values)
    # Inicializa una matriz para almacenar los resultados de los subproblemas
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Llena la matriz dp usando programación dinámica
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            print(f"i={i} w={w}")
            print(f"dp={dp}")
            print(f"if={weights[i - 1] <= w}")
            if weights[i - 1] <= w:
                # Si el peso del elemento actual es menor o igual a la capacidad actual,
                # considera tomarlo o dejarlo
                
                print(f"values[i - 1]={values[i - 1]} .... dp[i - 1][w - weights[i - 1]={dp[i - 1][w - weights[i - 1]]}")
                print(f"dp[i - 1][w]={dp[i - 1][w]}")
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Si el peso del elemento actual es mayor que la capacidad actual,
                # entonces no lo podemos incluir, así que tomamos el valor del subproblema anterior
                print(f"ELSE dp[i - 1][w]={dp[i - 1][w]}")
                dp[i][w] = dp[i - 1][w]
            print(f"DP={dp}")
    
    # La solución estará en el último elemento de la matriz
    return dp[n][capacity]

# Ejemplo de uso
values = [2, 5, 6, 10, 13, 16]
weights = [1, 2, 4, 5, 7, 9]
capacity = 8

print("El valor máximo que se puede obtener es:", knapsack_01(values, weights, capacity))
