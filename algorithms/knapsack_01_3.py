def knapsack_01(beneficios, volumenes, capacidadMaximaVolumen):
    n = len(beneficios)
    # Inicializa una matriz para almacenar los resultados de los subproblemas
    dp = [[0] * (capacidadMaximaVolumen + 1) for _ in range(n + 1)]

    # Llena la matriz dp usando programación dinámica
    for beneficioIndex in range(1, n + 1):
        for volumenIndex in range(1, capacidadMaximaVolumen + 1):
            print(f"beneficioIndex={beneficioIndex} volumenIndex={volumenIndex}")
            print(f"dp={dp}")
            print(f"if={volumenes[beneficioIndex - 1] <= volumenIndex}")
            volumenActual = volumenes[beneficioIndex - 1]
            if volumenActual <= volumenIndex:
                # Si el peso del elemento actual es menor o igual a la capacidad actual,
                # considera tomarlo o dejarlo
                dp[beneficioIndex][volumenIndex] = max(beneficios[beneficioIndex - 1] + dp[beneficioIndex - 1][volumenIndex - volumenes[beneficioIndex - 1]], 
                                              dp[beneficioIndex - 1][volumenIndex])
            else:
                # Si el peso del elemento actual es mayor que la capacidad actual,
                # entonces no lo podemos incluir, así que tomamos el valor del subproblema anterior
                print(f"ELSE dp[beneficioIndex - 1][volumenIndex]={dp[beneficioIndex - 1][volumenIndex]}")
                dp[beneficioIndex][volumenIndex] = dp[beneficioIndex - 1][volumenIndex]
            print(f"DP={dp}")
    
    # La solución estará en el último elemento de la matriz
    return dp[n][capacidadMaximaVolumen]

# Ejemplo de uso
beneficios = [2, 5, 6, 10, 13, 16]
volumenes = [1, 2, 4, 5, 7, 9]
capacidadMaximaVolumen = 8

print("El valor máximo que se puede obtener es:", knapsack_01(beneficios, volumenes, capacidadMaximaVolumen))
