import json

ARQUIVO = "gastos.json"


def salvar(dados):

    with open(
        ARQUIVO,
        "w"
    ) as f:

        json.dump(
            dados,
            f
        )


def carregar():

    try:

        with open(
            ARQUIVO,
            "r"
        ) as f:

            return json.load(f)

    except:

        return []