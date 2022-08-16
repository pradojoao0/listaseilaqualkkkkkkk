
def lerMatriz():
    m, ler_linha = [], input()
    while ler_linha: 
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m 
def escreverMatriz(m):
    for linha in m:
        print(*linha)




matriz = lerMatriz();

linhas = len(matriz);
colunas = len(matriz[0])


multBranco = 1
multPreto = 1

for linha in range(0, linhas):
    for coluna in range(0, colunas):
        if(linha % 2 == 0):
            if(coluna % 2 == 0):
                if(matriz[linha][coluna] % 2 == 0):
                    multBranco *= matriz[linha][coluna]
            else:
                if(matriz[linha][coluna] % 2 == 0):
                    multPreto *= matriz[linha][coluna]
        else:
            if(coluna % 2 == 0):
                if(matriz[linha][coluna] % 2 == 0):
                    multPreto *= matriz[linha][coluna]
            else:
                if(matriz[linha][coluna] % 2 == 0):
                    multBranco *= matriz[linha][coluna]

print(f"multiplicação pares na cor=1 é {multPreto}; e na outra cor é {multBranco}")
