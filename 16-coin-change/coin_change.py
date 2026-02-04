#Byte Quest
# Lista de monedas disponibles
coins = [1, 2, 5]

# Monto total que queremos formar
amount = 11

# dp[i] = mínimo número de monedas para formar el monto i
dp = [float('inf')] * (amount + 1)

# Caso base: para formar 0 no se necesitan monedas
dp[0] = 0

# Recorremos cada moneda disponible
for coin in coins:
    # Recorremos los montos desde el valor de la moneda hasta el monto objetivo
    for current_amount in range(coin, amount + 1):

        dp[current_amount] = min(
            dp[current_amount],
            dp[current_amount - coin] + 1
        )
        # Comparamos:
        # 1) No usar la moneda → dp[current_amount]
        # 2) Usar la moneda → dp[current_amount - coin] + 1
        # Nos quedamos con el mínimo

# Resultado final
if dp[amount] != float('inf'):
    result = dp[amount]
else:
    result = -1

# Mostramos el resultado
print("Mínimo número de monedas:", result)
