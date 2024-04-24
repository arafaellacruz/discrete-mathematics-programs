print("::::: Matemática Discreta - Cardinalidade :::::")

while True:
    elementos = input("Informe os elementos do conjunto separando-os por uma virgula: ")
    
    elementosClean = elementos.replace(" ", "").split(",")
    conjunto = set(elementosClean)
    cardinalidade = len(conjunto)
    
    print("O conjunto informado possui a cardinalidade =", cardinalidade)
            
    encerrarPrograma = input("Pressione '*' para sair ou qualquer outro caracter para informar novos elementos de um conjunto: ")    

    if encerrarPrograma.lower() == "*":
        print("Programa finalizado!")
        break