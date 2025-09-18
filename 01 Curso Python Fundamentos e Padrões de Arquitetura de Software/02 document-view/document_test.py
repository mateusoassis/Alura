import document

def testar_adicao_e_duplicacao():
    document.resetar_atendentes()
    assert document.adicionar_atendente("Pessoa") == "ok"
    assert document.adicionar_atendente("") == "vazio"
    assert document.adicionar_atendente("Pessoa") == "duplicado"

def testar_incremento():
    document.resetar_atendentes()
    document.adicionar_atendente("Pessoa")
    document.incrementar_vendas(0)
    assert document.obter_atendentes()[0]["vendas"] == 1

if __name__ == "__main__":
    testar_adicao_e_duplicacao()
    testar_incremento()
    print("Todos os testes passaram!")