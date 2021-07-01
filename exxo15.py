dias=int(input('Quantos dias usou o veículo?  '))
km=float(input('Quantos quilometros foram rodados? '))
diar=dias*60
kmt=km*0.15
print('O valor das diárias foi R$ {:.2f} e o valor da quilometragem usada foi R$ {:.2f}.\n'
      'O total a pagar é R${:.2f}.\nObrigado!\n'
      'Volte sempre!'.format(diar,kmt,diar+kmt))
