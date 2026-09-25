vagoes = [("V1", 45), ("V2", 52), ("V3", 48), ("V4", 60), ("V5", 49)]
limite_seguranca = 50

excedentes = 0
pode_acoplar = True

for nome, peso in vagoes:
    if peso > limite_seguranca:
        excedentes += 1
        pode_acoplar = False

total_peso = sum(p for _, p in vagoes)

print(f"Vagões excedentes: {excedentes}")
print(f"Total de peso: {total_peso}t")
print(f"Trem seguro: {'Sim' if pode_acoplar else 'Não'}")