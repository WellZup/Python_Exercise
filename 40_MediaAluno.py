nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if 7 > media >= 5:
    print('Recuperação')
elif media < 5:
    print('Reprovado')
elif media >= 7:
    print('Aprovado!')