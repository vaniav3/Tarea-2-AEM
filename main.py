import random
import time
import matplotlib.pyplot as plt

def leer_archivo(archivo):
    with open(archivo, 'r') as f:
        data = f.read().splitlines()
        m = int(data[0])
        n = int(data[1])
        costos = []
        demanda = [[] for _ in range(m)]
        cantidad, temp = 0, 0
        for i in data[2:]:
            if len(costos) < n:
                costos.extend(map(int, i.strip().split(' ')))
            else:
                if cantidad == 0:
                    cantidad = int(i)
                    continue
                if len(demanda[temp]) < cantidad:
                    demanda[temp].extend(map(int, i.strip().split(' ')))
                if len(demanda[temp]) == cantidad:
                    cantidad = 0
                    temp += 1
    return m, n, costos, demanda
    
def greedy_det(m, demanda, costos):
    clinicas_comun = []
    clinicas = []
    costos_clinica = [[] for _ in range(m)]
    for d in range(len(demanda)):
        for i in range(len(demanda[d])):
            costos_clinica[d].append({"clinica": demanda[d][i], "costo": costos[demanda[d][i] - 1]})
    
    for i in costos_clinica:
        bandera_clinica = False
        for j in i:
            if j in clinicas_comun:
                clinicas.append(j)
                bandera_clinica = True
                break
            
        if not bandera_clinica:
            menor_clinica = min(i, key=lambda x: x["costo"])
            clinicas.append(menor_clinica)
            clinicas_comun.append(menor_clinica)
            
    costo_total = sum(i["costo"] for i in clinicas_comun)
    return costo_total, clinicas, costos_clinica

def greedy_est(m, demanda, costos, clinicas = []):
    clinicas_comun = []
    costos_clinica = [[] for _ in range(m)]
    costo_total = 0
    
    if len(clinicas) != 0:
        for x in clinicas:
            clinicas_comun.append(x)
            
    for d in range(len(demanda)):
        for i in range(len(demanda[d])):
            costos_clinica[d].append({"clinica": demanda[d][i], "costo": costos[demanda[d][i] - 1]})
    
    for i in range((len(clinicas)), len(costos_clinica)):
        bandera_clinica = False
        for j in costos_clinica[i]:
            if j in clinicas_comun:
                clinicas.append(j)
                bandera_clinica = True
                break
            
        if not bandera_clinica:
            menor_clinica = random.choices(costos_clinica[i], weights=[1 / j["costo"] for j in costos_clinica[i]], k=1)[0]
            clinicas.append(menor_clinica)
            clinicas_comun.append(menor_clinica)
            
    print(clinicas_comun, "\n")
    costo_total = sum(i["costo"] for i in clinicas_comun)
    return costo_total, clinicas, costos_clinica

def hill_climbing_mejora_mejora(m, demanda, costos, num_iteraciones=500, max_iteraciones=500):
    tiempo = []
    fo = []
    tiempo_inicio = time.time()
    costo_total, clinicas, costos_clinica = greedy_est(m, demanda, costos)
    mejor_solucion = clinicas[:]
    mejor_costo = costo_total
    print("---- SOLUCION INICIAL: ", mejor_costo, "\n")
    iteracion = 0
    sin_mejora = 0

    while iteracion < num_iteraciones:
        hubo_mejora = False
        
        if sin_mejora >= max_iteraciones:
            costo_total, clinicas, costos_clinica = greedy_est()
            mejor_solucion = clinicas[:]
            mejor_costo = costo_total
            sin_mejora = 0
            
        for i, actual in enumerate(mejor_solucion):
            mejor_local = actual
            costo_local = mejor_costo

            for nueva_clinica in costos_clinica[i]:
                if nueva_clinica['clinica'] not in [c['clinica'] for c in mejor_solucion]:
                    temp_solucion = mejor_solucion[:]
                    temp_solucion[i] = nueva_clinica
                    nuevo_costo = calcular_costo_unico(temp_solucion)

                    if nuevo_costo < costo_local:
                        mejor_local = nueva_clinica
                        costo_local = nuevo_costo
                        hubo_mejora = True

            if hubo_mejora:
                mejor_solucion[i] = mejor_local
                mejor_costo = costo_local
                tiempo.append(time.time() - tiempo_inicio)
                fo.append(costo_local)
                
        if hubo_mejora:
            sin_mejora = 0
        else:
            sin_mejora += 1

        iteracion += 1

    return mejor_solucion, mejor_costo, tiempo, fo

def calcular_costo_unico(clinicas):
    clinicas_unicas = list({c['clinica']: c for c in clinicas}.values())
    return sum(c['costo'] for c in clinicas_unicas)

def variante(index):
    costo_total, clinicas, costos_clinica = greedy_est()
    clinicas = clinicas[:index]
    costo_total, clinicas, costos_clinica = greedy_est(clinicas)
    return costo_total

def tiempo_ejecucion(tiempo_transcurrido):
    minutos = int(tiempo_transcurrido // 60)
    segundos = int(tiempo_transcurrido % 60)
    milisegundos = int((tiempo_transcurrido * 1000) % 1000)
    formato_tiempo = "{:02}:{:02}:{:03}".format(minutos, segundos, milisegundos)
    return formato_tiempo
    
if __name__ == "__main__":
    m, n, costos, demanda = leer_archivo("C1.txt")
    for _ in range(3):
        print(greedy_est(m, demanda, costos)[0])
    # archivos = ["C1.txt", "C2.txt"]
    # for archivo in archivos:
    #     m, n, costos, demanda = leer_archivo(archivo)
    #     tiempo_inicio = time.time()
    #     costo_total, clinicas, costos_clinica = greedy_det(m, demanda, costos)
    #     tiempo_transcurrido = time.time() - tiempo_inicio
    #     formato_tiempo = tiempo_ejecucion(tiempo_transcurrido)
    #     print(f"GREEDY DETERMINISTA [{archivo}]: [TIEMPO] {formato_tiempo} [F.O] {costo_total}")
        
        # for _ in range(10):
        #     tiempo_inicio = time.time()
        #     costo_total = 0
        #     costo_total = greedy_est(m, demanda, costos)[0]
        #     tiempo_transcurrido = time.time() - tiempo_inicio
        #     formato_tiempo = tiempo_ejecucion(tiempo_transcurrido)
        #     print(f"GREEDY ESTOCASTICO [{archivo}]: [TIEMPO] {formato_tiempo} [F.O] {costo_total}")
        
        # tiempos, fo = [], []
        # for i in range(5):
        #     print(f"\nHILL CLIMBING [{archivo}] ITERACION {i + 1}")
        #     costo_total, clinicas, tiempo, fo = hill_climbing_mejora_mejora(m, demanda, costos)
        #     if tiempo != []:
        #         tiempos.extend(tiempo)
        #         fo.append(fo)

        # promedio_tiempo = sum(tiempos) / len(tiempos)
        # formato_tiempo = tiempo_ejecucion(promedio_tiempo)
        # promedio_costo = sum(fo) / len(fo)
        # print(f"HILL CLIMBING [{archivo}]: [TIEMPO PROMEDIO] {formato_tiempo} [F.O PROMEDIO] {promedio_costo}")

        # plt.plot(tiempos, fo, marker='o')
        # plt.xlabel('Tiempo (s)')
        # plt.ylabel('F.O')
        # plt.title(f"HILL CLIMBING [{archivo}]: [TIEMPO PROMEDIO] {formato_tiempo} [F.O PROMEDIO] {promedio_costo}")
        # plt.show()
        
        # tiempos, fo = [], []
        # for _ in range(5):
        #     tiempo_inicio = time.time()
        #     costo_total = variante(random.choice(range(1, m)))
        #     tiempo_transcurrido = time.time() - tiempo_inicio
        #     tiempos.extend(tiempo_transcurrido)
        #     fo.append(costo_total)
            
        # promedio_tiempo = sum(tiempos) / len(tiempos)
        # formato_tiempo = tiempo_ejecucion(promedio_tiempo)
        # promedio_costo = sum(fo) / len(fo)
        # print(f"VARIANTE [{archivo}]: [TIEMPO PROMEDIO] {formato_tiempo} [F.O PROMEDIO] {promedio_costo}")
        
        # plt.plot(tiempos, fo, marker='o')
        # plt.xlabel('Tiempo (s)')
        # plt.ylabel('F.O')
        # plt.title(f"VARIANTE [{archivo}]: [TIEMPO PROMEDIO] {formato_tiempo} [F.O PROMEDIO] {promedio_costo}")
        # plt.show()
            
        
        
