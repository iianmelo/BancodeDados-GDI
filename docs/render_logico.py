#!/usr/bin/env python3
"""Cartões do esquema implementado em SQL/create.sql.

Cada chave estrangeira nomeia a tabela referenciada, em vez de uma teia de
arestas. Os nomes e os tipos são os do DDL.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

GROUPS = [
    ("Instituições e competições", "#e7eef6", [
        ("FEDERACAO", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "ID_FED", "INT", ""),
        ]),
        ("PRESIDENTE_DA_FEDERACAO", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "ID", "INT", ""),
            ("FK", "ID_FED", "INT", "FEDERACAO"),
        ]),
        ("ARBITRO", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "CODIGO", "INT", ""),
            ("", "DT_NASCIMENTO", "DATE", ""),
            ("", "NACIONALIDADE", "VARCHAR(30)", ""),
        ]),
        ("FAZ_PARTE", [
            ("PK FK", "CODIGO_ARBITRO", "INT", "ARBITRO"),
            ("PK FK", "ID_FED", "INT", "FEDERACAO"),
        ]),
        ("COMPETICAO", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "ID_ARTIFICIAL", "INT", ""),
            ("PK FK", "ID_FED", "INT", "FEDERACAO"),
            ("", "TEMPORADA", "INT", ""),
        ]),
        ("GARANTE_VAGA", [
            ("PK FK", "ID_ARTIFICIAL_MAIOR", "INT", "COMPETICAO"),
            ("PK FK", "ID_FED_MAIOR", "INT", "COMPETICAO"),
            ("PK FK", "ID_ARTIFICIAL_MENOR", "INT", "COMPETICAO"),
            ("PK FK", "ID_FED_MENOR", "INT", "COMPETICAO"),
        ]),
    ]),
    ("Clubes, patrocínio e troféus", "#e7f3ec", [
        ("CLUBE", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "CODIGO", "INT", ""),
            ("", "MASCOTE", "VARCHAR(30)", ""),
            ("", "SEDE", "VARCHAR(30)", ""),
        ]),
        ("EMPRESA", [
            ("UQ", "NOME", "VARCHAR(30)", ""),
            ("PK", "CNPJ", "INT", ""),
        ]),
        ("PAT_CLUBE", [
            ("PK FK", "CODIGO_CLUBE", "INT", "CLUBE"),
            ("PK FK", "CNPJ_EMPRESA", "INT", "EMPRESA"),
            ("PK", "DT_CONTRATO", "DATE", ""),
            ("", "VALOR", "INT", ""),
            ("", "DURACAO", "INT", ""),
        ]),
        ("PAT_COMP", [
            ("PK FK", "ID_COMP", "INT", "COMPETICAO"),
            ("PK FK", "ID_FED", "INT", "COMPETICAO"),
            ("PK FK", "CNPJ_EMPRESA", "INT", "EMPRESA"),
            ("PK", "DT_CONTRATO", "DATE", ""),
            ("", "VALOR", "INT", ""),
            ("", "DURACAO", "INT", ""),
        ]),
        ("TROFEU", [
            ("PK", "NOME", "VARCHAR(30)", ""),
            ("", "VALOR", "INT", ""),
        ]),
        ("PARTICIPA", [
            ("PK FK", "CODIGO", "INT", "CLUBE"),
            ("PK FK", "ID_ARTIFICIAL", "INT", "COMPETICAO"),
            ("PK FK", "ID_FED", "INT", "COMPETICAO"),
            ("FK", "NOME_TROFEU", "VARCHAR(30)", "TROFEU"),
            ("", "COLOCACAO", "VARCHAR(30)", ""),
        ]),
    ]),
    ("Pessoas e elencos", "#f8efe6", [
        ("FUNCIONARIO", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "ID_FUNC", "INT", ""),
            ("", "SALARIO", "INT", ""),
            ("", "DT_NASCIMENTO", "DATE", ""),
            ("", "NACIONALIDADE", "VARCHAR(30)", ""),
        ]),
        ("JOGADOR", [
            ("PK FK", "ID_JOGADOR", "INT", "FUNCIONARIO"),
        ]),
        ("LIGADO", [
            ("PK FK", "ID_FUNC", "INT", "FUNCIONARIO"),
            ("PK FK", "CODIGO_CLUBE", "INT", "CLUBE"),
            ("PK", "TEMPORADA", "INT", ""),
            ("PK", "FUNCAO", "VARCHAR(30)", ""),
        ]),
        ("JOGADOR_PARTICIPA", [
            ("PK FK", "ID_FUNC", "INT", "FUNCIONARIO"),
            ("PK FK", "CODIGO_JOGO", "INT", "JOGO"),
            ("", "N_GOLS", "INT", ""),
            ("", "N_ASSIST", "INT", ""),
            ("", "POSICAO", "VARCHAR(30)", ""),
        ]),
        ("CARTOES", [
            ("PK FK", "ID_FUNC", "INT", "JOGADOR_PARTICIPA"),
            ("PK FK", "COD_JOGO", "INT", "JOGADOR_PARTICIPA"),
            ("PK", "COR", "VARCHAR(50)", ""),
            ("PK", "MINUTO", "TIMESTAMP", ""),
        ]),
    ]),
    ("Partidas e estádios", "#eef0f6", [
        ("ESTADIO", [
            ("", "NOME", "VARCHAR(30)", ""),
            ("PK", "COD_ESTADIO", "INT", ""),
            ("", "CAPACIDADE", "INT", ""),
            ("", "END_PAIS", "VARCHAR(30)", ""),
            ("", "END_CIDADE", "VARCHAR(30)", ""),
            ("", "END_CEP", "INT", ""),
            ("", "END_NUMERO", "INT", ""),
        ]),
        ("JOGO", [
            ("PK", "CODIGO", "INT", ""),
            ("", "DATA_", "DATE", ""),
            ("", "FASE", "VARCHAR(30)", ""),
            ("FK", "ID_ARTIFICIAL", "INT", "COMPETICAO"),
            ("FK", "ID_FED", "INT", "COMPETICAO"),
            ("FK NN", "CODIGO_VISITANTE", "INT", "CLUBE"),
            ("FK NN", "CODIGO_MANDANTE", "INT", "CLUBE"),
        ]),
        ("TEM", [
            ("PK FK", "COD_ARBITRO", "INT", "ARBITRO"),
            ("PK FK", "COD_JOGO", "INT", "JOGO"),
            ("", "FUNCAO_ARBITRO", "VARCHAR(30)", ""),
            ("", "PLACAR", "VARCHAR(30)", ""),
            ("FK NN", "COD_ESTADIO", "INT", "ESTADIO"),
        ]),
    ]),
]


def e(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def table_height(cols):
    return 36 + 26 * len(cols) + 8


def build():
    col_w = 620
    gap = 22
    margin = 32
    width = margin * 2 + col_w * 2 + gap
    heights = [[table_height(cols) for _name, cols in tables] for _t, _f, tables in GROUPS]

    def stack(hs):
        return 44 + sum(hs) + 14 * (len(hs) - 1) + 22

    row_h = [max(stack(heights[0]), stack(heights[1])), max(stack(heights[2]), stack(heights[3]))]
    height = 96 + row_h[0] + gap + row_h[1] + 72
    origins = [
        (margin, 96),
        (margin + col_w + gap, 96),
        (margin, 96 + row_h[0] + gap),
        (margin + col_w + gap, 96 + row_h[0] + gap),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="{width}" height="{height}" fill="#f6f3ec"/>',
        '<text x="32" y="42" fill="#1e3a5f" font-family="Inter, DejaVu Sans, sans-serif" font-size="26" font-weight="700">Esquema relacional implementado</text>',
        '<text x="32" y="68" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" font-size="14">20 tabelas de SQL/create.sql · PK chave primária · FK chave estrangeira · NN NOT NULL · UQ UNIQUE · a seta nomeia a tabela referenciada</text>',
    ]
    for (title, fill, tables), hs, (x, y0), block_h in zip(GROUPS, heights, origins, [row_h[0], row_h[0], row_h[1], row_h[1]]):
        parts.append(
            f'<rect x="{x}" y="{y0}" width="{col_w}" height="{block_h}" rx="16" fill="{fill}" stroke="#d5dde6"/>'
        )
        parts.append(
            f'<text x="{x + 16}" y="{y0 + 28}" fill="#1e3a5f" font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="650">{e(title)}</text>'
        )
        y = y0 + 46
        for (name, cols), h in zip(tables, hs):
            parts.append(
                f'<rect x="{x + 14}" y="{y}" width="{col_w - 28}" height="{h}" rx="8" fill="#ffffff" stroke="#c5ced6"/>'
            )
            parts.append(f'<rect x="{x + 14}" y="{y}" width="{col_w - 28}" height="30" rx="8" fill="#1e3a5f"/>')
            parts.append(f'<rect x="{x + 14}" y="{y + 16}" width="{col_w - 28}" height="14" fill="#1e3a5f"/>')
            parts.append(
                f'<text x="{x + 26}" y="{y + 20}" fill="#ffffff" font-family="Inter, DejaVu Sans, sans-serif" font-size="13" font-weight="700">{e(name)}</text>'
            )
            ry = y + 48
            for flag, col, typ, target in cols:
                flag_color = "#8a6232" if flag else "#b0b8c0"
                parts.append(
                    f'<text x="{x + 26}" y="{ry}" fill="{flag_color}" font-family="Inter, DejaVu Sans, sans-serif" font-size="10" font-weight="700">{e(flag or "·")}</text>'
                )
                parts.append(
                    f'<text x="{x + 84}" y="{ry}" fill="#243140" font-family="JetBrains Mono, DejaVu Sans Mono, monospace" font-size="12">{e(col)}</text>'
                )
                parts.append(
                    f'<text x="{x + 300}" y="{ry}" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" font-size="12">{e(typ)}</text>'
                )
                if target:
                    parts.append(
                        f'<text x="{x + col_w - 26}" y="{ry}" text-anchor="end" fill="#1f6b4a" font-family="Inter, DejaVu Sans, sans-serif" font-size="12" font-weight="600">→ {e(target)}</text>'
                    )
                ry += 26
            y += h + 14
    parts.append(
        f'<text x="32" y="{height - 40}" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" font-size="13">'
        "JOGADOR_PARTICIPA referencia FUNCIONARIO, não JOGADOR. CARTOES referencia o par (ID_FUNC, COD_JOGO) de JOGADOR_PARTICIPA."
        "</text>"
    )
    parts.append(
        f'<text x="32" y="{height - 20}" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" font-size="13">'
        "CODIGO_MANDANTE, CODIGO_VISITANTE e COD_ESTADIO são NOT NULL. NOME de EMPRESA é UNIQUE. ID_FED do presidente não é NOT NULL nem UNIQUE no DDL."
        "</text>"
    )
    parts.append("</svg>")
    return "\n".join(parts), width


def main():
    svg, _width = build()
    path = ROOT / "diagrama-logico.svg"
    path.write_text(svg, encoding="utf-8")
    print(path, path.stat().st_size)


if __name__ == "__main__":
    main()
