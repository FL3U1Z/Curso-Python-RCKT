#exemplo de modulos
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz de 25 é {raiz_quadrada}")

#exemplo de criação e utilização de modulo persnolalizado
from meu_modulo import dobro, saudacao

mensagem = saudacao("Flávio")
double = dobro(21)
print(mensagem)
print(f"O dobro da minha idade é {double}")
