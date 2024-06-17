print("::::: Matemática Discreta - Conjunto Vazio :::::")

print("\nUm conjunto é conhecido como vazio quando ele não possui nenhum elemento. \nEle pode ser representado por { } ou pelo símbolo Ø — ambos possuem o mesmo \nsignificado. O conjunto vazio está contido em todo e qualquer conjunto.")

perguntas = [
        {
            "mensagem": "\nConsidere o conjunto A={1,2,3,4}\n\nÉ correto afirmar que o conjunto vazio está contido no conjunto A. Afirmação está: \na) Correta \nb) Incorreta \nResposta: ",
            "respostaCorreta": 'a' or 'A',
            "acertos": "Parabéns, você acertou! O conjunto vazio está em TODOS os conjuntos.\n"
        },
        {
            "mensagem": "Se A={1,2,3} e B={4,5,6}, então a interseção desses conjuntos é o conjunto vazio, pois não \nhá elementos comuns entre A e B: A∩B = Ø. Afirmação está: \na) Correta \nb) Incorreta \nResposta: ",
            "respostaCorreta": 'a' or 'A',
            "acertos": "Parabéns, você acertou! O conjunto vazio está em TODOS os conjuntos.\n"
        },
        {
            "mensagem": "Qual o conjunto dos números primos entre 11 e 13? \na) 12 \nb) Ø, pois não existem números primos ENTRE 11 e 13. \nResposta: ",
            "respostaCorreta": 'b' or 'B',
            "acertos": "Parabéns, você acertou! O conjunto vazio está em TODOS os conjuntos.\n"
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


