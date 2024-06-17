def main():
    print("::::: Matemática Discreta - Fechos nas Endorrelações :::::")
    print("\n")
    print("Um fecho é a menor combinação possível para completar uma relação para satisfazer uma propriedade, \nou seja, dado uma propriedade seja ela reflexiva, simétrica ou transitiva, precisamos adicionar \nos elementos que satisfaçam as propriedades conforme se pede.")
    print("\nConsiderando que as propriedades:")
    print("  \n- Reflexiva: quando todo x se relaciona consigo mesmo. \n    Ex: Conjunto A = {1; 2; 3}.\n    Relações: (1;1);(2;2);(3;3).")
    print("  \n- Simétrica: quando se (x;y) então (y;x). \n    Ex: Conjunto A = {1; 2; 3}.\n    Relações: (1;2);(2;1);(2;3);(3;2).")
    print("  \n- Transitica: quando se (x;y) e (y;z) então (x;z). \n    Ex: Conjunto A = {1; 2; 3}.\n    Relações: (1;2);(1;3);(2;3);(3;2).")
    
    print("\nEscolha abaixo a opção correta para cada fecho:")
    
    perguntas = [
        {
            "mensagem": "\nConjunto: A={1,2,3,4}\nFecho: R={(1,1),(2,2),(3,3),(4,4),(1,2),(2,3),(3,4)}\n\nO fecho informado é: \na) Reflexiva \nb) Simétrica \nc) Transitiva: \nResposta: ",
            "respostaCorreta": 'a' or 'A',
            "acertos": "Parabéns, você acertou! A relação é reflexiva.\n"
        },
        {
            "mensagem": "\nConjunto: B={a,b,c,d}\nFecho: S={(a,b),(b,a),(c,d),(d,c)}\nO fecho informado é: \na) Reflexiva \nb) Simétrica \nc) Transitiva: \nResposta: ",
            "respostaCorreta": 'b' or 'B',
            "acertos": "Parabéns, você acertou! A relação é simétrica.\n"
        },
        {
            "mensagem": "\nConjunto: C={x,y,z,w}\nFecho: T={(x,y),(y,z),(x,z),(w,w)}\nO fecho informado é: \na) Reflexiva \nb) Simétrica \nc) Transitiva: \nResposta: ",
            "respostaCorreta": 'c' or 'C',
            "acertos": "Parabéns, você acertou! A relação é transitiva.\n"
        }
    ]
    
    for pergunta in perguntas:
        while True:
            resposta = input(pergunta["mensagem"]).strip().lower()
            if resposta == pergunta["respostaCorreta"]:
                print(pergunta["acertos"])
                break
            else:
                print("Ops, pense melhor e tente novamente.\n")
                
    

if __name__ == "__main__":
    main()

while True:
    encerrarPrograma = input("\nPressione '*' e Enter para encerrar o programa: ")
    if encerrarPrograma == '*':
        break    
    
    
