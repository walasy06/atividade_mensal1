class Produto:
    def __init__(self, descricao, preco_unitario, estoque):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.estoque = estoque

    def decrementar_estoque(self, quant):
        if quant <= self.estoque:
            self.estoque -= quant
            return True
        else:
            print(f"Estoque insuficiente para {self.descricao}.")
            return False
