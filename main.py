def calcular_media(notas):
    soma = 0
    for i in range(len(notas)):
        soma += notas[i]
    media = soma / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    alunos = {
        "João": [8.5, 7.0, 6.5],
        "Maria": [9.0, 8.5, 9.5],
        "Pedro": [4.0, 5.5, 6.0],
        "Ana": [7.5, 8.0, 7.0]
    }
    
    resultados = []
    
    for nome, notas in alunos.items():
        try:
            media = calcular_media(notas)
            situacao = verificar_aprovacao(media)
            resultados.append({"nome": nome, "media": media, "situacao": situacao})
        except Exception as e:
            print(f"Erro ao processar {nome}: {str(e)}")
    
    print("Resultados finais:")
    for resultado in resultados:
        print(f"{resultado['nome']}: Média {resultado['media']:.2f} - {resultado['situacao']}")

if __name__ == "__main__":
    main()

