from datetime import datetime

class Venda:
    def __init__(self):
        self.data = datetime.now()
        self.valor_total = 0.0
        self.itens = []

    def adicionar_item(self, produto, quant):
        if produto.decrementar_estoque(quant):
            item = ItemVenda(produto, quant)
            self.itens.append(item)
            print(f"Item adicionado: {quant}x {produto.descricao}")

    def remover_item(self, produto):
        for item in self.itens:
            if item.produto == produto:
                self.itens.remove(item)
                produto.estoque += item.quantidade
                print(f"Item removido: {produto.descricao}")
                return
        print(f"Produto {produto.descricao} não encontrado na venda.")

    def calcular_total(self):
        self.valor_total = 0.0
        for item in self.itens:
            self.valor_total += item.calcular_subtotal()
        return self.valor_total
