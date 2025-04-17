class Carteira:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(transacao)

    def exibir_transacoes(self):
        for transacao in self.transacoes:
            print(transacao.resumo())

    def saldo(self):
        return sum(transacao.valor for transacao in self.transacoes)

    def filtrar_por_categoria(self, categoria):
        filtradas = [t for t in self.transacoes if t.categoria == categoria]
        for transacao in filtradas:
            print(transacao.resumo())

    def gastos_totais(self):
        return sum(t.valor for t in self.transacoes if t.valor < 0)

    def renda_total(self):
        return sum(t.valor for t in self.transacoes if t.valor > 0)

    def resumo_geral(self):
        print(f"Total de transações: {len(self.transacoes)}")
        print(f"Renda total: {self.renda_total()}")
        print(f"Gastos totais: {self.gastos_totais()}")
        print(f"Saldo final: {self.saldo()}")