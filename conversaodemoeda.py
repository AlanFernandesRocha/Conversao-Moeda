real = float(input('Quando de dinheiro você tem na carteira? R$'))
dolar =  real / 5.62
print('Com o valor de R${:.2f}, você pode comprar US${:.2f}'.format(real, dolar))