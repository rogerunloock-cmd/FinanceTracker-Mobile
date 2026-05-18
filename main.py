import flet as ft
from database import salvar, carregar
from dashboard import gerar_grafico


def main(page: ft.Page):

    page.title = "Finance Tracker"
    page.theme_mode = "dark"

    dados = carregar()

    nome = ft.TextField(label="Descrição")
    valor = ft.TextField(label="Valor")

    categoria = ft.Dropdown(
        label="Categoria",

        options=[
            ft.dropdown.Option("Alimentação"),
            ft.dropdown.Option("Transporte"),
            ft.dropdown.Option("Lazer"),
            ft.dropdown.Option("Saúde"),
            ft.dropdown.Option("Outros")
        ]
    )

    gastos = ft.Column()

    total = sum(
        float(x["valor"])
        for x in dados
    )

    texto_total = ft.Text(
        f"Total gasto: R${total}"
    )

    for item in dados:

        gastos.controls.append(

            ft.Text(
                f'{item["nome"]} | '
                f'R${item["valor"]} | '
                f'{item["categoria"]}'
            )
        )

    def adicionar(e):

        nonlocal total

        novo = {

            "nome": nome.value,
            "valor": valor.value,
            "categoria": categoria.value

        }

        dados.append(novo)

        salvar(dados)

        total += float(valor.value)

        gastos.controls.append(

            ft.Text(
                f"{nome.value} | "
                f"R${valor.value} | "
                f"{categoria.value}"
            )
        )

        texto_total.value = (
            f"Total gasto: R${total}"
        )

        nome.value = ""
        valor.value = ""

        page.update()

    page.add(

        ft.Text(
            "Finance Tracker 💰",
            size=30,
            weight="bold"
        ),

        nome,
        valor,
        categoria,

       ft.ElevatedButton(
    "Ver gráfico",
    on_click=lambda e:
        gerar_grafico(dados)
),

        texto_total,

        gastos
    )


ft.run(main)