class Alunos:
    def __init__(self, nome, *notas):
        self.nome = nome
        self.notas = list(notas)
    def media_aluno(self):
        return sum(self.notas) / len(self.notas)
    def aprovado(self):
        return self.media_aluno() >= 6

alunos = [
    Alunos("Gabriel", 8.5, 7.0, 9.0, 6.5),
    Alunos("João", 6.0, 6.0, 6.0, 4.5),
    Alunos("Maria", 9.2, 8.8, 7.5, 10.0),
    Alunos("Lucas", 7.8, 9.3, 5.9, 10.0),
    Alunos("Livia", 9.0, 8.9, 9.5, 9.4)
]
alunos.sort(key=lambda aluno: aluno.media_aluno(), reverse=True)
soma_medias = 0
for aluno in alunos:
            
            print(f"Nome: {aluno.nome}")
            print(f"Notas: {aluno.notas}")
            print(f"Média do aluno: {aluno.media_aluno():.2f}")

            soma_medias += aluno.media_aluno()

            
            if aluno.aprovado():
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print()
media_turma = soma_medias / len(alunos)
print(f"A média da turma foi: {media_turma:.2f}")

maior_media = max(alunos, key=lambda aluno: aluno.media_aluno())
menor_media = min(alunos, key=lambda aluno: aluno.media_aluno())


print(f"Maior média: {maior_media.nome} ({maior_media.media_aluno():.2f})")
print(f"Menor média: {menor_media.nome} ({menor_media.media_aluno():.2f})")