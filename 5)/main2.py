def inverter_string(s):

    lista_caracteres = list(s)

    inicio = 0
    fim = len(lista_caracteres) - 1

    while inicio < fim:

        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        inicio += 1
        fim -= 1

    return ''.join(lista_caracteres)

def main():

    string_original = input("Digite a string para ser invertida: ")

    string_invertida = inverter_string(string_original)

    print(f"A string invertida é: {string_invertida}")

if __name__ == "__main__":
    main()
