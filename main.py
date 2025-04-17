from transacao import Transacao
from carteira import Carteira

if __name__ == "__main__":

    carteira = Carteira()

    t1 = Transacao("Salário", 2500, "Renda", "10/04/2025")
    t2 = Transacao("Mercado", -300, "Alimentação", "12/04/2025")
    t3 = Transacao("Aluguel", -1200, "Moradia", "01/04/2025")

    carteira.adicionar(t1)
    carteira.adicionar(t2)
    carteira.adicionar(t3)

    print("Transações:")
    carteira.exibir_transacoes()

    print("\nSaldo total:", carteira.saldo())

    print("\nFiltrar por categoria 'Alimentação':")
    carteira.filtrar_por_categoria("Alimentação")

    print("\nResumo geral:")
    carteira.resumo_geral()