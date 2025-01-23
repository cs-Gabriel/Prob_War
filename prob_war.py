"""""
O código é para apoiar a decisão se vale apena efetuar um ataque ou não no jogo de tabuleiro War.

    :para ataque: Número de exércitos do atacante (máximo de 3 dados rolados).
    :para defesa: Número de exércitos do defensor (máximo de 3 dados rolados).
    :empate da vitória a defesa.
    :os dados são rolado ate um dos dois lado ficarem sem exércitos.
    :para simulações: Número de simulações para estimar a probabilidade.
    :return: Probabilidade do atacante vencer.
 """

import random

def calcular_probabilidade_vitoria(ataque, defesa, simulacoes=10000):
    vitorias_ataque = 0

    for _ in range(simulacoes):
        ataque_atual = ataque
        defesa_atual = defesa

        while ataque_atual > 0 and defesa_atual > 0:
            dados_ataque = sorted([random.randint(1, 6) for _ in range(min(3, ataque_atual))], reverse=True)
            dados_defesa = sorted([random.randint(1, 6) for _ in range(min(3, defesa_atual))], reverse=True)

            # Comparar os resultados dos dados
            for d_a, d_d in zip(dados_ataque, dados_defesa):
                if d_a > d_d:
                    defesa_atual -= 1
                else:  # Empates favorecem o defensor
                    ataque_atual -= 1

        # Verificar quem venceu
        if ataque_atual > 0:
            vitorias_ataque += 1

    return vitorias_ataque / simulacoes

# Exemplo de uso:
ataque = 13
defesa = 10
probabilidade = calcular_probabilidade_vitoria(ataque, defesa)
print(f"Probabilidade do ataque vencer: {probabilidade:.2%}")