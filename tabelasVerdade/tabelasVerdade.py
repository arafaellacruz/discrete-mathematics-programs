print("::::: Matemática Discreta - Tabela Verdade :::::")
print("\n")


P = True  
Q = False  
R = True   

combinations = [
    (P, Q, R),
    (P, Q, not R),
    (P, not Q, R),
    (P, not Q, not R),
    (not P, Q, R),
    (not P, Q, not R),
    (not P, not Q, R),
    (not P, not Q, not R)
]

print("Considerando os valores abaixo, verifique a tabela verdade: ")
print("\n   P: Verdadeiro")
print("   Q: Falso")
print("   R: Verdadeiro")

print("\nP | Q | R | ¬P | ¬Q | ¬R | P ^ Q | P ^ R | Q ^ R | P v Q | P v R | Q v R | P → Q | P → R | Q → R | P ↔ Q | P ↔ R | Q ↔ R")
print("-------------------------------------------------------------------------------------------------------------------------")

# Função para imprimir cada linha da tabela
def printLines(p, q, r):
    not_p = not p
    not_q = not q
    not_r = not r
    p_and_q = p and q
    p_and_r = p and r
    q_and_r = q and r
    p_or_q = p or q
    p_or_r = p or r
    q_or_r = q or r
    p_implies_q = not p or q
    p_implies_r = not p or r
    q_implies_r = not q or r
    p_iff_q = p == q
    p_iff_r = p == r
    q_iff_r = q == r
    
    return (f"{'V' if p else 'F'} | "
            f"{'V' if q else 'F'} | "
            f"{'V' if r else 'F'} | "
            f"{'V ' if not_p else 'F '} | "
            f"{'V ' if not_q else 'F '} | "
            f"{'V ' if not_r else 'F '} | "
            f"{'  V  ' if p_and_q else '  F  '} | "
            f"{'  V  ' if p_and_r else '  F  '} | "
            f"{'  V  ' if q_and_r else '  F  '} | "
            f"{'  V  ' if p_or_q else '  F  '} | "
            f"{'  V  ' if p_or_r else '  F  '} | "
            f"{'  V  ' if q_or_r else '  F  '} | "
            f"{'  V  ' if p_implies_q else '  F  '} | "
            f"{'  V  ' if p_implies_r else '  F  '} | "
            f"{'  V  ' if q_implies_r else '  F  '} | "
            f"{'  V  ' if p_iff_q else '  F  '} | "
            f"{'  V  ' if p_iff_r else '  F  '} | "
            f"{'  V  ' if q_iff_r else '  F  '} | ")

for p, q, r in combinations:
    print(printLines(p, q, r))

while True:
    encerrarPrograma = input("\nPressione '*' e Enter para encerrar o programa: ")
    if encerrarPrograma == '*':
        break