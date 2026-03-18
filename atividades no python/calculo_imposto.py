def somaimposto():
    custo = float(input('Custo da venda: '))
    taxaimposto = float(input('Taxa de imposto: '))
    decimal = taxaimposto/100
    valor_total = custo + decimal
print(somaimposto)
