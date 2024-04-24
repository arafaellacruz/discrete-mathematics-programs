print("::::: Matemática Discreta - Cardinalidade :::::")

def contador(elementos):

    return elementos.strip().count(",") + 1

while True:
    elementos = input("Informe os elementos do conjunto separando-os por uma vírgula: ")
    
    cardinalidade = contador(str(elementos))
    
    print("O conjunto informado possui a cardinalidade =", cardinalidade)
            
    encerrarPrograma = input("Pressione '*' para sair ou qualquer outro caracter para informar novos elementos de um conjunto: ")    

    if encerrarPrograma.lower() == "*":
        print("Programa finalizado!")
        break