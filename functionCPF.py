def generatorCPF():
    from random import randint

    cpf = ''
    for num in range(0, 9):
        cpf += str(randint(0, 9))
    cpf = validateCPF(cpf, generator=True)
    return cpf


def validateCPF(cpf, formatCPF=False, generator=False):
    listCpf = []
    listCpfV2 = []
    digit = ''
    digitG = ''
    if formatCPF:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
    oldCpf = cpf
    if not generator:
        cpf = cpf[:-2]

    for ind, num in enumerate(range(10, 1, -1)):
        listCpf.append(int(cpf[ind]) * num)

    varTotal = 11 - (sum(listCpf) % 11)
    if varTotal > 9:
        varTotal = 0
    digit += str(varTotal)
    digitG += str(varTotal)
    cpf += digit

    for ind, num in enumerate(range(11, 1, -1)):
        listCpfV2.append(int(cpf[ind]) * num)

    varTotal2 = 11 - (sum(listCpfV2) % 11)
    if varTotal2 > 9:
        varTotal2 = 0
    digit = str(varTotal2)
    digitG += str(varTotal2)
    cpf += str(digit)

    sequence = cpf == str(cpf[0]) * len(cpf)

    if not generator:
        if cpf == oldCpf and not sequence:
            return True
        else:
            return False
    else:
        cpf = [cpf[:3] + '.', cpf[3:6] + '.', cpf[6:9] + '-', cpf[9:]]
        cpf = ''.join(cpf)
        return cpf

