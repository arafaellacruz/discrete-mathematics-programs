print("::::: Matemática Discreta - Continência :::::")
while True:
    elementosA = input("Informe os elementos do conjunto A separando-os por uma vírgula: ")
    elementosB = input("Informe os elementos do conjunto B separando-os por uma vírgula: ")

    conjuntoA = elementosA.split(',')
    conjuntoB = elementosB.split(',')

    print("O conjunto é A é: ", conjuntoA)
    print("O conjunto é B é: ", conjuntoB)

    if set(conjuntoA).issubset(set(conjuntoB)):
        print("O conjunto A é um subconjunto de B.")
    else: 
        print("O conjunto A não é um subconjunto de B.")
    
    if set(conjuntoB).issubset(set(conjuntoA)):
        print("O conjunto B é um subconjunto de A.")
    else: 
        print("O conjunto B não é um subconjunto de A.")
        
    encerrarPrograma = input("Pressione '*' para sair ou qualquer outro caracter para informar novos elementos de um conjunto: ")    

    if encerrarPrograma.lower() == "*":
        print("Programa finalizado!")
        break
    
        
