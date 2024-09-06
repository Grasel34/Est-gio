
faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


total_mensal = sum(faturamentos.values())


percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamentos.items()}


print("Percentual de representação de cada estado no valor total mensal:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
