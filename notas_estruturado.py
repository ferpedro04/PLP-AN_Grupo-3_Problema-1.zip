def calcular_media(notas):
    #Calcula a média aritmética de uma lista de notas.
    if not notas:
        return 0.0
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)


def determinar_situacao(media):
    # Se media > 7, será aprovado. Caso contrário, reprovado
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


def calcular_estatisticas_turma(alunos):
    #Calcula a média geral, a maior nota e a menor nota da turma.
    soma_medias = 0
    maior_nota = alunos[0]["notas"][0]
    menor_nota = alunos[0]["notas"][0]

    for aluno in list(alunos):
        soma_medias += aluno["media"]
        for nota in aluno["notas"]:
            if nota > maior_nota:
                maior_nota = nota
            if nota < menor_nota:
                menor_nota = nota

    media_geral = soma_medias / len(alunos)
    return media_geral, maior_nota, menor_nota


def ordenar_alunos_por_nome(alunos):
    #nova lista ordenada em ordem alfabética pelo nome.
    return sorted(alunos, key=lambda x: x["nome"])


def principal():
    print("=" * 50)
    print("SISTEMA DE NOTAS E MÉDIAS")
    print("=" * 50)

    notas_alunos = [
        {"nome": "Lucas Almeida", "notas": [8.5, 7.0, 9.0]},
        {"nome": "Ana Beatriz", "notas": [6.0, 5.5, 6.5]},
        {"nome": "Carlos Eduardo", "notas": [9.5, 10.0, 9.0]},
        {"nome": "Mariana Souza", "notas": [4.0, 7.5, 5.0]},
        {"nome": "Beatriz Costa", "notas": [7.0, 8.0, 7.5]}
    ]

    alunos_processados = []

    for nota in notas_alunos:
        media = calcular_media(nota["notas"])
        situacao = determinar_situacao(media)

        aluno = {
            "nome": nota["nome"],
            "notas": nota["notas"],
            "media": media,
            "situacao": situacao
        }
        alunos_processados.append(aluno)

    # Cálculos estatísticos gerais da turma
    media_geral, maior_nota, menor_nota = calcular_estatisticas_turma(alunos_processados)

    # Ordem alfabética
    alunos_ordenados = ordenar_alunos_por_nome(alunos_processados)

    # Exibe a listagem por ordem alfabetica
    print("\n" + "=" * 50)
    print("LISTAGEM DE ALUNOS")
    print("=" * 50)
    for aluno in alunos_ordenados:
        print(f"Nome: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f} -> Situação: {aluno['situacao']}")
        print("-" * 50)

    # Exibe as estatísticas gerais
    print("\n" + "=" * 50)
    print("ESTATÍSTICAS GERAIS DA TURMA")
    print("=" * 50)
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Maior nota registrada: {maior_nota:.2f}")
    print(f"Menor nota registrada: {menor_nota:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    principal()
