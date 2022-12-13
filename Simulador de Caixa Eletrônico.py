#Programa principal
print('='*20)
print('    BANCO CEV    ')
print('='*20)

valor=int(input('Qual valor você quer sacar? R$'))
total = valor
ced= 50
totced = 0

while True:
    if total >= ced:
        total-=ced
        totced+=1
    else:
        print('Total de {} cédulas de R${}'.format(totced,ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced=0
        if total == 0:
            break
print('='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
