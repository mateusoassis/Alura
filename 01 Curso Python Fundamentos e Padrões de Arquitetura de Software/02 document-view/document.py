atendentes = []

def adicionar_atendente(nome):
    if not nome:
        return "vazio"

    if nome in [a["nome"] for a in atendentes]:
        return "duplicado"

    atendentes.append({"nome": nome, "vendas": 0})
    return "ok"

def resetar_atendentes():
    atendentes.clear()

def incrementar_vendas(indice):
    atendentes[indice]["vendas"] += 1

def obter_atendentes():
    return atendentes