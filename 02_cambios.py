# calcula el cambio de una cantidad de dinero en una moneda a otra moneda
# el usuario ingresa la cantidad de dinero y la moneda de origen y destino
co = int(input('cantidad de pesos colombianos:'))
print(co)

pe = int(input('cantidad de suelas peruanas:'))
print(pe)

br = int(input('cantidad de reais brasileños:'))
print(br)
 
un_co = 0.00030
un_pe = 0.29
un_br = 0.17
total_usd = float(co * un_co) + (pe * un_pe) + (br * un_br)
 
print (total_usd)
