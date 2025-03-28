from database import (
    create_connection, create_table, inserir_produto,
    listar_produtos, atualizar_produto, deletar_produto,
    buscar_produto_por_nome, filtrar_produtos_por_preco,
    filtrar_produtos_por_quantidade
)

def menu():
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\n" + "="*33)
        print("      SISTEMA DE PRODUTOS      ")
        print("="*33)
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Buscar produto por nome")
        print("6 - Filtrar produtos por preço")
        print("7 - Filtrar produtos por quantidade")
        print("0 - Sair")
        print("="*33)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            print("\n--- Adicionar Produto ---")
            nome = input("Nome do produto: ").strip()
            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                inserir_produto(conn, nome, quantidade, preco)
                print("Produto adicionado com sucesso!")
            except ValueError:
                print("Erro: Quantidade deve ser um inteiro e preço um número (ex.: 10.5).")
                
        elif opcao == '2':
            print("\n--- Lista de Produtos ---")
            listar_produtos(conn)
            
        elif opcao == '3':
            print("\n--- Atualizar Produto ---")
            try:
                produto_id = int(input("ID do produto para atualizar: "))
                nova_quantidade = int(input("Nova quantidade: "))
                novo_preco = float(input("Novo preço: "))
                atualizar_produto(conn, produto_id, nova_quantidade, novo_preco)
                print("Produto atualizado com sucesso!")
            except ValueError:
                print("Erro: Certifique-se de inserir valores numéricos para ID, quantidade e preço.")
                
        elif opcao == '4':
            print("\n--- Deletar Produto ---")
            try:
                produto_id = int(input("ID do produto para deletar: "))
                deletar_produto(conn, produto_id)
                print("Produto deletado com sucesso!")
            except ValueError:
                print("Erro: Insira um ID numérico.")
                
        elif opcao == '5':
            print("\n--- Buscar Produto por Nome ---")
            nome = input("Digite o nome ou parte do nome do produto: ").strip()
            buscar_produto_por_nome(conn, nome)
            
        elif opcao == '6':
            print("\n--- Filtrar Produtos por Preço ---")
            try:
                preco_min = float(input("Preço mínimo: "))
                preco_max = float(input("Preço máximo: "))
                filtrar_produtos_por_preco(conn, preco_min, preco_max)
            except ValueError:
                print("Erro: Insira valores numéricos para os preços.")
                
        elif opcao == '7':
            print("\n--- Filtrar Produtos por Quantidade ---")
            try:
                quant_min = int(input("Quantidade mínima: "))
                quant_max = int(input("Quantidade máxima: "))
                filtrar_produtos_por_quantidade(conn, quant_min, quant_max)
            except ValueError:
                print("Erro: Insira valores numéricos para as quantidades.")
                
        elif opcao == '0':
            print("\nEncerrando o programa. Até logo :)")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
    
    conn.close()