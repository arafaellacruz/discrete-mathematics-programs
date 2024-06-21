print("::::: Matemática Discreta - Indução Matemática :::::")
print("\n")

print("Teste seus conhecimentos sobre Indução Matemática: ")

perguntas = [
    {
        "mensagem": "\nO que é P.P.I.M? \na) Para Poder Ir a Madrid \nb) Primeiro Principio de Indução Matemática \nResposta: ",
        "respostaCorreta" : 'b' or 'B',
        "acertos": "Parabéns, você acertou! (:\n"

    },
    {
        "mensagem": "\nA 1ª parte de PPIM é a validação da Base, onde mostrar que a propriedade que se quer provar é válida para o \nmenor valor possível do conjunto de números naturais. Geralmente, verifica-se se a propriedade é verdadeira \npara n=1 ou n=0, quando não há uma condição para n. A afirmação está: \na) Verdadeiro \nb) Falso \nResposta: ",
        "respostaCorreta" : 'a' or 'A',
        "acertos": "Parabéns, você acertou! (:\n"

    },
    {
        "mensagem": "\nA 2ª parte de PPIM é a Hipostese Indutiva, onde supõe-se que a propriedade seja válida para um número \nnatural k arbitrário, ou seja: \na) Assumimos que a propriedade é verdadeira para um valor n = k. \nb) Escolhemos um número natural qualquer para n. \nResposta: ",
        "respostaCorreta" : 'a' or 'A',
        "acertos": "Parabéns, você acertou! (:\n"
    },
    {
        "mensagem": "\nA 3ª parte de PPIM é a Tese, onde demonstramos que, se a propriedade é válida para n=k, então ela também é \nválida para n = k + 1, e essencialmente, mostra-se que a validade da propriedade para k implica a validade \npara k+1, e substituimos todo k por k + 1. A afirmação está:\na) Correta \nb) Incorreta \nResposta: ",
        "respostaCorreta" : 'a' or 'A',
        "acertos": "Parabéns, você acertou! (:\n"
    },   
]

for pergunta in perguntas:
    while True:
        resposta = input(pergunta["mensagem"]).strip().lower()
        if resposta == pergunta["respostaCorreta"]:
            print(pergunta["acertos"])
            break
        else:
            print("Ops, pense melhor e tente novamente.\n")

while True:
    encerrarPrograma = input("\nPressione '*' e Enter para encerrar o programa: ")
    if encerrarPrograma == '*':
        break    
    