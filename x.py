# def hill_climbing(max_iter=30000, max_iter_sin_mejora=1000):
#     costo_total, clinicas, costos_clinica = greedy_est()
#     print("INICIAL ", costo_total, clinicas, "\n")

#     iteraciones_sin_mejora = 0
#     mejor_costo = costo_total
#     mejor_clinicas = clinicas.copy()

#     for _ in range(max_iter):
#         if iteraciones_sin_mejora >= max_iter_sin_mejora:
#             costo_total, clinicas, costos_clinica = greedy_est()
#             iteraciones_sin_mejora = 0

#         clinicas_temp = clinicas.copy()
#         vecinos = generar_vecinos(clinicas_temp, costos_clinica)
#         mejor_vecino_costo = float('inf')
#         mejor_vecino_clinicas = None

#         for vecino in vecinos:
#             costo_temp = sum(costo[j - 1] for j in vecino)
#             if costo_temp < mejor_vecino_costo:
#                 mejor_vecino_costo = costo_temp
#                 mejor_vecino_clinicas = vecino.copy()

#         if mejor_vecino_costo < mejor_costo:
#             mejor_costo = mejor_vecino_costo
#             mejor_clinicas = mejor_vecino_clinicas.copy()
#             iteraciones_sin_mejora = 0
#         else:
#             iteraciones_sin_mejora += 1

#         costo_total = mejor_costo
#         clinicas = mejor_clinicas.copy()

#     return mejor_costo, mejor_clinicas

# def generar_vecinos(clinicas, costos_clinica):
#     vecinos = []
#     for i in range(len(clinicas)):
#         index = costos_clinica[i].index(clinicas[i])
#         if index + 1 < len(costos_clinica[i]):
#             vecino = clinicas.copy()
#             vecino[i] = costos_clinica[i][index + 1]
#             vecinos.append(vecino)
#         if index - 1 >= 0:
#             vecino = clinicas.copy()
#             vecino[i] = costos_clinica[i][index - 1]
#             vecinos.append(vecino)
#     return vecinos

# resultado = []
# for i in range(10):
#     resultado.append(greedy_est())
# print(min(resultado))
# print(max(resultado))
# print(greedy_est()[2])
# print(sum(costo[i - 1] for i in encontrar_clinicas_mas_comunes()))
# for i in range(10):
#     print(greedy_est())
