Eu comecei criando uma pasta chamada sisvenda pra guardar todos os arquivos do projeto. Dentro dela eu criei quatro arquivos: produto.py, item_venda.py, venda.py e main.py. Cada arquivo representa uma classe que aparecia no diagrama UML que o professor passou.

No arquivo produto.py eu criei a classe Produto, que guarda a descrição, o preço unitário e o estoque. Nela eu fiz o método decrementar_estoque, que serve pra tirar produtos do estoque quando alguém compra, retornando True se deu certo ou False se não tinha o suficiente.

No item_venda.py eu fiz a classe ItemVenda, que representa cada item dentro de uma venda. Ela guarda o produto, a quantidade e já calcula o valor do item multiplicando o preço pela quantidade. Também tem o método calcular_subtotal.

No venda.py eu fiz a classe Venda, que é a principal. Ela guarda a data (peguei com datetime.now()), o valor total e uma lista de itens. Fiz três métodos: adicionar_item, que antes de adicionar chama o decrementar_estoque do produto; remover_item, que tira o produto da venda e devolve a quantidade pro estoque; e calcular_total, que percorre todos os itens e soma os subtotais.

Por fim, no main.py eu fiz os testes. Criei três produtos (Camiseta, Calça e Boné), criei uma venda, adicionei alguns itens, tentei adicionar uma quantidade maior do que tinha no estoque pra ver se o sistema bloqueava, removi um item e no final calculei o total. Rodei tudo com o comando python main.py e deu certo.
