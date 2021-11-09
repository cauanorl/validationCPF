from functionCPF import generatorCPF, validateCPF

cpf = generatorCPF()
print(validateCPF(cpf, formatCPF=True))

print(f'CPF gerado: {cpf}')
