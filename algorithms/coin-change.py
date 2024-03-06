def coin_change(coins, amount):
    # Inicializamos la matriz dp con tamaño (len(coins) + 1) x (amount + 1)
    dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]
    print(dp)
    # Caso base: Si la cantidad es 0, no se necesitan monedas
    for i in range(len(coins) + 1):
        dp[i][0] = 0
    print(dp)
    # Llenamos la tabla utilizando programación dinámica
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j - coins[i - 1] >= 0:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    # Si dp[len(coins)][amount] es infinito, significa que no se puede formar la cantidad deseada
    return dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1

# Ejemplo de uso
denominaciones = [1, 2, 5]
cantidad = 11

print("Cantidad mínima de monedas necesarias:", coin_change(denominaciones, cantidad))
