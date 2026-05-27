from motor_outliers import calcular_metricas
from auditoria_viz import exibir_relatorio

notas_brutas = [100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]
notas_fiscais = []

for nota in notas_brutas:
    if nota > 0:
        notas_fiscais.append(nota)

print(f"Notas processadas: {notas_fiscais}")
print("-" * 30)


media, variancia, qtd = calcular_metricas(notas_fiscais)
print(f"Média calculada: {media:.2f}")

