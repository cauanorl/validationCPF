from functionCPF import validateCPF

while True:
    cpf = str(input('Digite seu CPF: '))

    if len(cpf) != 11:
        print('CPF inválido!')
        continue
    break

if validateCPF(cpf):
    print(f'O CPF {cpf} é válido!')
else:
    print(f'O CPF {cpf} é inválido! Veja se foi digitado corretamente...')
