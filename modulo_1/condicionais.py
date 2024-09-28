

# if, elif e else

#exemplo de IF
idade = 12
print("Exemplo de comando if")
if idade >= 18: 
    print("Você é maior de idade.")
elif idade >=12:
    print("Você é um adolecente")
else:
    print("Você é menor de idade.")

mens = "pode tirar a carteira de habilitação" if idade >=18 else "Você não pode tirar a Habilitação"
print(mens)