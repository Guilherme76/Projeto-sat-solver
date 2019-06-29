'''*****************************************************
  Processa os inputs do usuário e retorna
uma lista com as linhas digitadas.
'''


# inputs = Primeira linha ( p cnf #vars #clauses)
# qtdVars = Quantidade de variáveis
# qtdClau = Quantidade de clausulas


def readInputs():
    inputs = input("Digite a entrada")
    qtdVars = int(inputs.split()[2])  # Posição 2 = qtdVars
    qtdClau = int(inputs.split()[3])  # Posição 3 = qtdClau
    return [qtdVars, qtdClau]


'''*****************************************************
 Extrai as cláusulas das  entradas do usuário
e produz uma lista com as clausulas.
'''


# LC = Lista com as clausulas

def readClauses(qtdClau):
    clauses = []
    for i in range(qtdClau):
        LC = []
        LC.append(input().split())
        LC[0].remove('0')
        clauses.append(LC[0])
    return clauses


'''*****************************************************
  Processa as clausulas e recebe a quantidade de variáveis 
e produz como resultado uma lista.
'''


def readVariables(clauses, qtdVars):
    variables = []
    for i in range(qtdVars):
        variables.append(False)  # Inicializa as variaveis com (0/False)
    return variables


'''*****************************************************
  Processa a entrada do usuário e devolve um dicionário 
com dois elementos, clauses e variables.

- Clauses guarda uma lista com as clausulas, onde cada 
cláusula é ela própria representada como uma lista 
(que pode ser de números ou de strings).

- Variables guarda uma lista com a quantidade de posições 
igual ao número de variáveis, onde a posição 0 corresponde 
à variável 1, e assim sucessivamente.
'''


# inp = elemento auxiliar que recebe a função(readInputs)
def readFormula():
    inp = readInputs()
    clauses = readClauses(inp[1])
    variables = readVariables(clauses, inp[0])
    result = {'clauses': clauses, 'variables': variables}
    return result


'''*****************************************************
Recebe como entrada a lista contendo a atribuição atual 
de valores às variáveis da fórmula e devolve uma nova lista 
com uma nova atribuição de valores a essas variáveis.
'''


def nextAssignment(currentAssignment, total):
    string = ''
    for i in range(len(currentAssignment)):
        if (currentAssignment[i] == True):
            currentAssignment[i] = '1'
        else:
            currentAssignment[i] = '0'

    for i in range(len(currentAssignment)):
        string = string + currentAssignment[i]

    decimal = int(string, 2)
    decimal += 1
    string = bin(decimal)[2:].zfill(len(currentAssignment))

    for i in range(len(string)):
        if (int(string[i]) > 0):
            currentAssignment[i] = True
        else:
            currentAssignment[i] = False

    return currentAssignment


'''*****************************************************
Essa função recebe como entrada a lista contendo a atribuição
inicial de valores às variáveis da fórmula e outra lista 
contendo as cláusulas. Enquanto a fórmula não for satisfeita 
nem todas as atribuições tiveram sido testadas, ela verifica 
se a atribuição atual satisfaz ou não a fórmula e, se não 
satisfizer, pega a próxima atribuição de valores e tenta novamente
'''


def doSolve(clauses, assignment):
    isSat = False
    formula = []
    total = 0

    while (not isSat and total < 2 ** len(assignment)):
        formula = []

        if (total > 0):
            for i in range(len(clauses)):
                for j in range(len(clauses[i])):
                    if (int(clauses[i][j]) < 0):
                        assignment[int(clauses[i][j])] = not assignment[int(clauses[i][j])]

        for i in range(len(clauses)):
            Form = False
            for j in range(len(clauses[i]) - 1):
                if (assignment[abs(int(clauses[i][j])) - 1] or assignment[abs(int(clauses[i][j + 1])) - 1] == True):
                    Form = True
                    break
            formula.append(Form)

        for n in range(len(formula) - 1):
            if (formula[n] == False):
                isSat = False
                break
            elif (formula[n] and formula[n + 1] == True):
                isSat = True

        if (isSat == False):
            assignment = nextAssignment(assignment, total)

        total += 1

    result = {'isSat': isSat, 'satisfyingAssignment': None}

    if (isSat):
        result['satisfyingAssignment'] = assignment

    return result


def solve():
    formula = readFormula()
    result = doSolve(formula['clauses'], formula['variables'])
    return result


print(solve())