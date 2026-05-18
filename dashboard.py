import matplotlib.pyplot as plt


def gerar_grafico(dados):

    if not dados:
        print("Nenhum gasto cadastrado.")
        return

    categorias = {}

    for item in dados:
        categoria = item["categoria"] or "Sem categoria"
        valor = float(item["valor"].replace(",", "."))

        categorias[categoria] = categorias.get(categoria, 0) + valor

    plt.figure(figsize=(5, 5))
    plt.pie(
        categorias.values(),
        labels=categorias.keys(),
        autopct="%1.1f%%"
    )
    plt.title("Distribuição de gastos")
    plt.show()