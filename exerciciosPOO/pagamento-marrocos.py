def pagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao

    multa = valor_prestacao * 0.03
    juros = valor_prestacao * 0.001 * dias_atraso

    return valor_prestacao + multa + juros


quantidade_prestacoes = 0
total_pago = 0

while True:
    valor = float(input("Digite o valor da prestação: R$ "))

    if valor == 0:
        break

    dias = int(input("Digite a quantidade de dias em atraso: "))

    valor_pago = pagamento(valor, dias)

    print(f"Valor a ser pago: R$ {valor_pago:.2f}")

    quantidade_prestacoes += 1
    total_pago += valor_pago


print("\n--- Relatório do dia ---")
print(f"Quantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total recebido: R$ {total_pago:.2f}")