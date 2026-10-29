#!/usr/bin/env python3
"""Diagrama relacional no estilo IE (pata de galinha), como uma exportação
de Oracle SQL Developer Data Modeler: caixa branca, traço preto, PK/FK,
tipo vindo do dicionário (VARCHAR2, NUMBER, DATE, TIMESTAMP).

Linha cheia: FK faz parte da PK. Linha tracejada: FK fora da PK.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
FONT = "Liberation Sans, Arial, Helvetica, sans-serif"

# (nome, [(flag, coluna, tipo)])  flag: PK, FK, PK FK, ""
TABLES = {
    "FEDERACAO": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "ID_FED", "NUMBER"),
    ],
    "PRESIDENTE_DA_FEDERACAO": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "ID", "NUMBER"),
        ("FK", "ID_FED", "NUMBER"),
    ],
    "ARBITRO": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "CODIGO", "NUMBER"),
        ("", "DT_NASCIMENTO", "DATE"),
        ("", "NACIONALIDADE", "VARCHAR2(30)"),
    ],
    "FAZ_PARTE": [
        ("PK FK", "CODIGO_ARBITRO", "NUMBER"),
        ("PK FK", "ID_FED", "NUMBER"),
    ],
    "COMPETICAO": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "ID_ARTIFICIAL", "NUMBER"),
        ("PK FK", "ID_FED", "NUMBER"),
        ("", "TEMPORADA", "NUMBER"),
    ],
    "GARANTE_VAGA": [
        ("PK FK", "ID_ARTIFICIAL_MAIOR", "NUMBER"),
        ("PK FK", "ID_FED_MAIOR", "NUMBER"),
        ("PK FK", "ID_ARTIFICIAL_MENOR", "NUMBER"),
        ("PK FK", "ID_FED_MENOR", "NUMBER"),
    ],
    "EMPRESA": [
        ("UQ", "NOME", "VARCHAR2(30)"),
        ("PK", "CNPJ", "NUMBER"),
    ],
    "CLUBE": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "CODIGO", "NUMBER"),
        ("", "MASCOTE", "VARCHAR2(30)"),
        ("", "SEDE", "VARCHAR2(30)"),
    ],
    "PAT_CLUBE": [
        ("PK FK", "CODIGO_CLUBE", "NUMBER"),
        ("PK FK", "CNPJ_EMPRESA", "NUMBER"),
        ("PK", "DT_CONTRATO", "DATE"),
        ("", "VALOR", "NUMBER"),
        ("", "DURACAO", "NUMBER"),
    ],
    "PAT_COMP": [
        ("PK FK", "ID_COMP", "NUMBER"),
        ("PK FK", "ID_FED", "NUMBER"),
        ("PK FK", "CNPJ_EMPRESA", "NUMBER"),
        ("PK", "DT_CONTRATO", "DATE"),
        ("", "VALOR", "NUMBER"),
        ("", "DURACAO", "NUMBER"),
    ],
    "TROFEU": [
        ("PK", "NOME", "VARCHAR2(30)"),
        ("", "VALOR", "NUMBER"),
    ],
    "PARTICIPA": [
        ("PK FK", "CODIGO", "NUMBER"),
        ("PK FK", "ID_ARTIFICIAL", "NUMBER"),
        ("PK FK", "ID_FED", "NUMBER"),
        ("FK", "NOME_TROFEU", "VARCHAR2(30)"),
        ("", "COLOCACAO", "VARCHAR2(30)"),
    ],
    "FUNCIONARIO": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "ID_FUNC", "NUMBER"),
        ("", "SALARIO", "NUMBER"),
        ("", "DT_NASCIMENTO", "DATE"),
        ("", "NACIONALIDADE", "VARCHAR2(30)"),
    ],
    "JOGADOR": [
        ("PK FK", "ID_JOGADOR", "NUMBER"),
    ],
    "LIGADO": [
        ("PK FK", "ID_FUNC", "NUMBER"),
        ("PK FK", "CODIGO_CLUBE", "NUMBER"),
        ("PK", "TEMPORADA", "NUMBER"),
        ("PK", "FUNCAO", "VARCHAR2(30)"),
    ],
    "JOGADOR_PARTICIPA": [
        ("PK FK", "ID_FUNC", "NUMBER"),
        ("PK FK", "CODIGO_JOGO", "NUMBER"),
        ("", "N_GOLS", "NUMBER"),
        ("", "N_ASSIST", "NUMBER"),
        ("", "POSICAO", "VARCHAR2(30)"),
    ],
    "CARTOES": [
        ("PK FK", "ID_FUNC", "NUMBER"),
        ("PK FK", "COD_JOGO", "NUMBER"),
        ("PK", "COR", "VARCHAR2(50)"),
        ("PK", "MINUTO", "TIMESTAMP(6)"),
    ],
    "ESTADIO": [
        ("", "NOME", "VARCHAR2(30)"),
        ("PK", "COD_ESTADIO", "NUMBER"),
        ("", "CAPACIDADE", "NUMBER"),
        ("", "END_PAIS", "VARCHAR2(30)"),
        ("", "END_CIDADE", "VARCHAR2(30)"),
        ("", "END_CEP", "NUMBER"),
        ("", "END_NUMERO", "NUMBER"),
    ],
    "JOGO": [
        ("PK", "CODIGO", "NUMBER"),
        ("", "DATA_", "DATE"),
        ("", "FASE", "VARCHAR2(30)"),
        ("FK", "ID_ARTIFICIAL", "NUMBER"),
        ("FK", "ID_FED", "NUMBER"),
        ("FK", "CODIGO_VISITANTE", "NUMBER"),
        ("FK", "CODIGO_MANDANTE", "NUMBER"),
    ],
    "TEM": [
        ("PK FK", "COD_ARBITRO", "NUMBER"),
        ("PK FK", "COD_JOGO", "NUMBER"),
        ("", "FUNCAO_ARBITRO", "VARCHAR2(30)"),
        ("", "PLACAR", "VARCHAR2(30)"),
        ("FK", "COD_ESTADIO", "NUMBER"),
    ],
}

# ordem de desenho, por coluna
COLUMNS = [
    ["FEDERACAO", "PRESIDENTE_DA_FEDERACAO", "ARBITRO", "FAZ_PARTE", "COMPETICAO", "GARANTE_VAGA"],
    ["EMPRESA", "CLUBE", "PAT_CLUBE", "PAT_COMP", "TROFEU", "PARTICIPA"],
    ["FUNCIONARIO", "JOGADOR", "LIGADO", "JOGADOR_PARTICIPA", "CARTOES"],
    ["ESTADIO", "JOGO", "TEM"],
]

# (filho, coluna_fk, pai, identificadora, lado_filho, lado_pai, rotulo)
# identificadora True = linha cheia
EDGES = [
    ("PRESIDENTE_DA_FEDERACAO", "ID_FED", "FEDERACAO", False, "right", "right", ""),
    ("COMPETICAO", "ID_FED", "FEDERACAO", True, "left", "left", ""),
    ("FAZ_PARTE", "ID_FED", "FEDERACAO", True, "left", "left", ""),
    ("FAZ_PARTE", "CODIGO_ARBITRO", "ARBITRO", True, "right", "right", ""),
    ("GARANTE_VAGA", "ID_FED_MAIOR", "COMPETICAO", True, "right", "right", "maior"),
    ("GARANTE_VAGA", "ID_FED_MENOR", "COMPETICAO", True, "left", "left", "menor"),
    ("PAT_COMP", "ID_FED", "COMPETICAO", True, "left", "right", ""),
    ("PAT_COMP", "CNPJ_EMPRESA", "EMPRESA", True, "left", "left", ""),
    ("PAT_CLUBE", "CNPJ_EMPRESA", "EMPRESA", True, "left", "right", ""),
    ("PAT_CLUBE", "CODIGO_CLUBE", "CLUBE", True, "right", "right", ""),
    ("PARTICIPA", "CODIGO", "CLUBE", True, "left", "left", ""),
    ("PARTICIPA", "ID_FED", "COMPETICAO", True, "left", "right", ""),
    ("PARTICIPA", "NOME_TROFEU", "TROFEU", False, "right", "right", ""),
    ("LIGADO", "ID_FUNC", "FUNCIONARIO", True, "left", "left", ""),
    ("LIGADO", "CODIGO_CLUBE", "CLUBE", True, "left", "right", ""),
    ("JOGADOR", "ID_JOGADOR", "FUNCIONARIO", True, "right", "right", "1:1"),
    ("JOGADOR_PARTICIPA", "ID_FUNC", "FUNCIONARIO", True, "left", "right", ""),
    ("JOGADOR_PARTICIPA", "CODIGO_JOGO", "JOGO", True, "right", "left", ""),
    ("CARTOES", "ID_FUNC", "JOGADOR_PARTICIPA", True, "right", "right", ""),
    ("JOGO", "ID_FED", "COMPETICAO", False, "left", "left", ""),
    ("JOGO", "CODIGO_MANDANTE", "CLUBE", False, "left", "left", "mandante"),
    ("JOGO", "CODIGO_VISITANTE", "CLUBE", False, "right", "right", "visitante"),
    ("TEM", "COD_JOGO", "JOGO", True, "left", "right", ""),
    ("TEM", "COD_ARBITRO", "ARBITRO", True, "left", "right", ""),
    ("TEM", "COD_ESTADIO", "ESTADIO", False, "right", "right", ""),
]


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;")


def table_height(cols):
    return 26 + 18 * len(cols) + 8


def layout():
    col_w = 300
    gap_x = 70
    margin_x = 56
    y0 = 52
    gap_y = 22
    pos = {}
    max_bottom = y0
    for i, names in enumerate(COLUMNS):
        x = margin_x + i * (col_w + gap_x)
        y = y0
        for name in names:
            h = table_height(TABLES[name])
            pos[name] = (x, y, col_w, h)
            y += h + gap_y
        max_bottom = max(max_bottom, y)
    gutters = [margin_x + i * (col_w + gap_x) - gap_x / 2 for i in range(5)]
    width = int(gutters[-1] + 36)
    height = max_bottom + 78
    return pos, width, height, gutters, max_bottom


def col_y(pos, table, column):
    x, y, w, h = pos[table]
    cols = TABLES[table]
    idx = next(i for i, c in enumerate(cols) if c[1] == column)
    return x, y, w, y + 26 + 8 + idx * 18 + 9


def marker(x, y, side, kind):
    """kind: one | zo | om | zm  (exatamente um, zero ou um, um ou mais, zero ou mais).
    side: lado da tabela em que o marcador encosta (left/right).
    """
    # o traço chega pela direção oposta ao lado
    sign = 1 if side == "left" else -1  # positivo = para a direita, para dentro da tabela à esquerda
    # na borda esquerda, os dedos abrem em direção à tabela (para a direita)
    out = []
    if kind in ("om", "zm"):
        heel = x - sign * 12
        out.append(f'<line x1="{heel}" y1="{y}" x2="{x}" y2="{y-6}" stroke="#000" stroke-width="1"/>')
        out.append(f'<line x1="{heel}" y1="{y}" x2="{x}" y2="{y}" stroke="#000" stroke-width="1"/>')
        out.append(f'<line x1="{heel}" y1="{y}" x2="{x}" y2="{y+6}" stroke="#000" stroke-width="1"/>')
    if kind in ("one", "om"):
        bx = x - sign * (16 if kind == "om" else 8)
        out.append(f'<line x1="{bx}" y1="{y-7}" x2="{bx}" y2="{y+7}" stroke="#000" stroke-width="1.2"/>')
        if kind == "one":
            bx2 = x - sign * 13
            out.append(f'<line x1="{bx2}" y1="{y-7}" x2="{bx2}" y2="{y+7}" stroke="#000" stroke-width="1.2"/>')
    if kind == "zo":
        bx = x - sign * 8
        out.append(f'<line x1="{bx}" y1="{y-7}" x2="{bx}" y2="{y+7}" stroke="#000" stroke-width="1.2"/>')
        cr = x - sign * 16
        out.append(f'<circle cx="{cr}" cy="{y}" r="4" fill="#fff" stroke="#000" stroke-width="1"/>')
    if kind == "zm":
        cr = x - sign * 20
        out.append(f'<circle cx="{cr}" cy="{y}" r="4" fill="#fff" stroke="#000" stroke-width="1"/>')
    return "\n".join(out), (x - sign * (24 if kind in ("zm", "zo", "om") else 18))


def column_index(name):
    for i, names in enumerate(COLUMNS):
        if name in names:
            return i
    raise KeyError(name)


def build():
    pos, width, height, gutters, floor = layout()
    chunks = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="28" y="28" fill="#000" font-family="{FONT}" font-size="14" font-weight="700">'
        "Esquema relacional — notação IE (pata de galinha)</text>",
    ]
    edge_svg = []
    lane_use = {}
    for n, (child, col, parent, ident, _cside, _pside, label) in enumerate(EDGES):
        c_col = column_index(child)
        p_col = column_index(parent)
        cx, _cy, cw, y1 = col_y(pos, child, col)
        px0, py0, pw, ph = pos[parent]
        y2 = py0 + 26 + 14
        if p_col > c_col:
            cside, pside = "right", "left"
            x1, x2 = cx + cw, px0
            g1, g2 = gutters[c_col + 1], gutters[p_col]
        elif p_col < c_col:
            cside, pside = "left", "right"
            x1, x2 = cx, px0 + pw
            g1, g2 = gutters[c_col], gutters[p_col + 1]
        else:
            # mesma coluna: sai pela direita e volta pela direita
            cside, pside = "right", "right"
            x1, x2 = cx + cw, px0 + pw
            g1 = g2 = gutters[c_col + 1]
        lane_use[g1] = lane_use.get(g1, 0) + 1
        shift = (lane_use[g1] - 1) * 5 - 4
        bus1 = g1 + shift
        bus2 = g2 + shift
        dash = "" if ident else ' stroke-dasharray="4 3"'
        if abs(bus1 - bus2) < 2:
            d = f"M {x1} {y1} L {bus1} {y1} L {bus1} {y2} L {x2} {y2}"
        else:
            channel = floor + 10 + (n % 4) * 6
            d = (
                f"M {x1} {y1} L {bus1} {y1} L {bus1} {channel} "
                f"L {bus2} {channel} L {bus2} {y2} L {x2} {y2}"
            )
        edge_svg.append(f'<path d="{d}" fill="none" stroke="#000" stroke-width="1"{dash}/>')
        child_kind = "zo" if child == "JOGADOR" else "zm"
        parent_kind = "one"
        if (child, col) in {
            ("JOGO", "ID_FED"),
            ("JOGO", "ID_ARTIFICIAL"),
            ("PRESIDENTE_DA_FEDERACAO", "ID_FED"),
            ("PARTICIPA", "NOME_TROFEU"),
        }:
            parent_kind = "zo"
        edge_svg.append(marker(x1, y1, cside, child_kind)[0])
        edge_svg.append(marker(x2, y2, pside, parent_kind)[0])
        if label:
            edge_svg.append(
                f'<text x="{x1 + (18 if cside=="right" else -18)}" y="{y1 - 6}" '
                f'text-anchor="{"start" if cside=="right" else "end"}" fill="#000" '
                f'font-family="{FONT}" font-size="10">{esc(label)}</text>'
            )
    chunks.extend(edge_svg)
    for name, (x, y, w, h) in pos.items():
        chunks.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="#000" stroke-width="1.1"/>'
        )
        chunks.append(
            f'<line x1="{x}" y1="{y+24}" x2="{x+w}" y2="{y+24}" stroke="#000" stroke-width="1"/>'
        )
        chunks.append(
            f'<text x="{x+w/2}" y="{y+16}" text-anchor="middle" fill="#000" '
            f'font-family="{FONT}" font-size="12" font-weight="700">{esc(name)}</text>'
        )
        ry = y + 24 + 14
        for flag, col, typ in TABLES[name]:
            chunks.append(
                f'<text x="{x+6}" y="{ry}" fill="#000" font-family="{FONT}" font-size="10">{esc(flag)}</text>'
            )
            weight = ' font-weight="700"' if "PK" in flag else ""
            chunks.append(
                f'<text x="{x+48}" y="{ry}" fill="#000" font-family="{FONT}" font-size="11"{weight}>{esc(col)}</text>'
            )
            chunks.append(
                f'<text x="{x+w-6}" y="{ry}" text-anchor="end" fill="#000" font-family="{FONT}" font-size="10">{esc(typ)}</text>'
            )
            ry += 18
    chunks.append(
        f'<text x="28" y="{height-16}" fill="#000" font-family="{FONT}" font-size="11">'
        "Linha cheia: a FK entra na PK. Linha tracejada: FK fora da PK. "
        "Dois traços = exatamente um. Círculo e traço = zero ou um. "
        "Pé de galinha = muitos. Tipos lidos do dicionário do Oracle."
        "</text>"
    )
    chunks.append("</svg>")
    return "\n".join(chunks)


def main():
    path = ROOT / "diagrama-logico.svg"
    path.write_text(build(), encoding="utf-8")
    print(path, path.stat().st_size)


if __name__ == "__main__":
    main()
