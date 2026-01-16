import chromadb

try:
    # 1. Inicializa o cliente (em memória para este teste rápido)
    chroma_client = chromadb.Client()

    # 2. Cria uma coleção
    collection = chroma_client.create_collection(name="teste_conexao")

    # 3. Adiciona alguns documentos
    collection.add(
        documents=["Este é um documento de teste", "ChromaDB está funcionando"],
        metadatas=[{"source": "teste"}, {"source": "teste"}],
        ids=["id1", "id2"]
    )

    # 4. Realiza uma consulta
    results = collection.query(
        query_texts=["O sistema está ok?"],
        n_results=1
    )

    print("✅ Sucesso! O ChromaDB está configurado e funcionando.")
    print(f"Resultado do teste: {results['documents'][0][0]}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")