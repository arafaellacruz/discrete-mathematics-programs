print("::::: Matemática Discreta - Condicional (<->)  :::::")
print("Lemos 'P se e somente se Q'.")

while True:
    print("Considerando p e q, informe se são 'V' (verdadeiro) ou 'F' (falso): ")
    p = input("P: ")
    q = input("Q: ")

    if (p == "V" or p == "v") and (q == "V" or q == "v"):
        print("P → Q = V")
        
    elif (p == "V" or p == "v") and (q == "F" or q == "f"):    
        print("P → Q = F")
        
    elif (p == "F" or p == "f") and (q == "V" or q == "v"):    
        print("P → Q = F")
        
    elif (p == "F" or p == "f") and (q == "F" or q == "f"):
        print("P → Q = V")   
        
    else:    
        print("Valor inválido. Por favor, informe apenas 'V' ou 'F'.")
        
    encerrarPrograma = input("Pressione '*' para sair ou qualquer outro caracter para informar os valores de P e Q novamente: ")    

    if encerrarPrograma.lower() == "*":
        print("Programa finalizado!")
        break