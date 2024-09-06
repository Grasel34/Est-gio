import json


def calcular_faturamento(faturamentos):

    faturamentos_validos = [valor for valor in faturamentos if valor > 0]

    if not faturamentos_validos:
        return None, None, 0


    menor_faturamento = min(faturamentos_validos)


    maior_faturamento = max(faturamentos_validos)


    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)


    dias_acima_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media


def main():

    with open('faturamento.json', 'r') as arquivo:
        dados = json.load(arquivo)


    faturamentos = [item['valor'] for item in dados['faturamento_diario']]


    menor, maior, dias_acima_media = calcular_faturamento(faturamentos)

    if menor is not None:
        print(f"O menor valor de faturamento ocorrido em um dia do mês é: {menor}")
        print(f"O maior valor de faturamento ocorrido em um dia do mês é: {maior}")
        print(
            f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_media}")
    else:
        print("Não há faturamentos válidos para calcular as estatísticas.")


if __name__ == "__main__":
    main()
