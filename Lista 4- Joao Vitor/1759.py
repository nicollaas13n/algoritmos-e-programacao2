#https://www.beecrowd.com.br/judge/en/problems/view/1759

ano = int (input ())

salarioBase = 1000
percentual = 0.015

if ano < 2006:
    print ("O ano informado deverá ser › 2005!")

else:
    salarioFinal = salarioBase + (percentual * salarioBase)

for n in range(2007, ano + 1):
    percentual = percentual + 0.01
    salarioFinal = salarioFinal + (percentual * salarioFinal)

print("Salário atual: R$%.2f " %(salarioFinal))