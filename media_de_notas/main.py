nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média é: {media} ")

if media >= 7:
    print("Aluno aprovado")

else:
    print("Aluno reprovado")    