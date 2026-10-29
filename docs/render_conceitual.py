#!/usr/bin/env python3
"""Esquema conceitual em três recortes do mesmo mini-mundo.

(mín, máx) ao lado da entidade = em quantos vínculos daquele relacionamento
uma ocorrência dela entra. A leitura segue o texto do README e o projeto
lógico, não as omissões do DDL.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
W, H = 1680, 1360


def e(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


parts = []


def add(fragment):
    parts.append(fragment)


def panel(x, y, w, h, title):
    add(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" '
        'fill="#eef2f6" stroke="#d5dde6"/>'
    )
    add(
        f'<text x="{x + 22}" y="{y + 28}" fill="#1e3a5f" '
        'font-family="Inter, DejaVu Sans, sans-serif" font-size="15" font-weight="650">'
        f"{e(title)}</text>"
    )


def entity(x, y, w, h, title, lines):
    add(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" '
        'fill="#ffffff" stroke="#1e3a5f" stroke-width="1.4"/>'
    )
    add(f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="#1e3a5f"/>')
    add(f'<rect x="{x}" y="{y + 14}" width="{w}" height="14" fill="#1e3a5f"/>')
    add(
        f'<text x="{x + 12}" y="{y + 19}" fill="#ffffff" '
        'font-family="Inter, DejaVu Sans, sans-serif" font-size="13" font-weight="650">'
        f"{e(title)}</text>"
    )
    yy = y + 48
    for line, underline in lines:
        deco = ' text-decoration="underline"' if underline else ""
        add(
            f'<text x="{x + 12}" y="{yy}" fill="#243140"{deco} '
            'font-family="Inter, DejaVu Sans, sans-serif" font-size="12">'
            f"{e(line)}</text>"
        )
        yy += 18


def diamond(cx, cy, rw, rh, title, sub=None):
    pts = f"{cx},{cy - rh} {cx + rw},{cy} {cx},{cy + rh} {cx - rw},{cy}"
    add(f'<polygon points="{pts}" fill="#e7f3ec" stroke="#1f6b4a" stroke-width="1.3"/>')
    dy = -3 if sub else 4
    add(
        f'<text x="{cx}" y="{cy + dy}" text-anchor="middle" fill="#143024" '
        'font-family="Inter, DejaVu Sans, sans-serif" font-size="12" font-weight="650">'
        f"{e(title)}</text>"
    )
    if sub:
        add(
            f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" fill="#3d5c4c" '
            'font-family="Inter, DejaVu Sans, sans-serif" font-size="10" font-style="italic">'
            f"{e(sub)}</text>"
        )


def poly(points, dashed=False):
    pts = " ".join(f"{x},{y}" for x, y in points)
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    add(
        f'<polyline points="{pts}" fill="none" stroke="#4d6270" stroke-width="1.4"{dash}/>'
    )


def label(x, y, text, anchor="start"):
    add(
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="#1e3a5f" '
        'font-family="Inter, DejaVu Sans, sans-serif" font-size="11" font-weight="600">'
        f"{e(text)}</text>"
    )


def build():
    parts.clear()
    add(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">'
    )
    add(f'<rect width="{W}" height="{H}" fill="#f6f3ec"/>')
    add(
        '<text x="48" y="42" fill="#1e3a5f" font-family="Inter, DejaVu Sans, sans-serif" '
        'font-size="26" font-weight="700">Mini-Mundo Futebol — esquema conceitual</text>'
    )
    add(
        '<text x="48" y="68" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" '
        'font-size="14">Gerenciamento de Dados e Informação · CIn-UFPE · o mesmo nome, nos três recortes, é a mesma entidade</text>'
    )

    # Recorte 1. Entidades ancoradas em y visual, losangos no meio do segmento.
    panel(32, 92, 1616, 300, "1    Federações, árbitros e competições")
    entity(52, 148, 200, 84, "PRESIDENTE", [("id", True), ("nome", False)])
    diamond(348, 190, 74, 34, "preside")
    entity(448, 148, 210, 84, "FEDERAÇÃO", [("id", True), ("nome", False)])
    diamond(748, 190, 74, 34, "realiza")
    entity(848, 140, 290, 100, "COMPETIÇÃO", [
        ("id da federação + id artificial", True),
        ("nome, temporada", False),
    ])
    diamond(1405, 190, 96, 40, "garante vaga", "menor × maior")
    poly([(252, 190), (274, 190)])
    poly([(422, 190), (448, 190)])
    poly([(658, 190), (674, 190)])
    poly([(822, 190), (848, 190)])
    poly([(1138, 170), (1309, 170)])
    poly([(1138, 210), (1309, 210)])
    label(258, 182, "(1,1)")
    label(428, 182, "(1,1)")
    label(680, 182, "(0,N)")
    label(854, 182, "(1,1)")
    label(1142, 162, "menor (0,N)")
    label(1142, 228, "maior (0,N)")

    entity(52, 268, 240, 92, "ÁRBITRO", [
        ("código", True),
        ("nome, nascimento, nacionalidade", False),
    ])
    diamond(400, 314, 76, 32, "faz parte")
    poly([(292, 314), (324, 314)])
    poly([(476, 314), (553, 314), (553, 232)])
    label(298, 306, "(0,N)")
    label(490, 306, "(0,N)")

    # Recorte 2.
    panel(32, 412, 1616, 400, "2    Clubes, pessoas, patrocínio e troféu")
    entity(52, 468, 250, 100, "FUNCIONÁRIO", [
        ("id", True),
        ("salário, nome", False),
        ("nascimento, nacionalidade", False),
    ])
    entity(52, 640, 250, 80, "JOGADOR", [
        ("sem atributos próprios", False),
        ("especialização parcial", False),
    ])
    poly([(177, 568), (177, 640)], dashed=True)
    label(190, 612, "pode ser")

    diamond(378, 518, 70, 32, "ligado", "temporada, função")
    entity(470, 468, 210, 100, "CLUBE", [("código", True), ("nome, mascote, sede", False)])
    diamond(760, 518, 74, 34, "participa", "colocação")
    entity(860, 456, 270, 116, "COMPETIÇÃO", [
        ("id da federação + id artificial", True),
        ("nome, temporada", False),
    ])
    diamond(1230, 514, 78, 36, "patrocina", "competição")
    entity(1336, 468, 200, 92, "EMPRESA", [("CNPJ", True), ("nome", False)])

    poly([(302, 518), (308, 518)])
    poly([(448, 518), (470, 518)])
    poly([(680, 518), (686, 518)])
    poly([(834, 518), (860, 518)])
    poly([(1130, 514), (1152, 514)])
    poly([(1308, 514), (1336, 514)])
    label(308, 508, "(0,N)")
    label(452, 508, "(0,N)")
    label(690, 508, "(0,N)")
    label(866, 508, "(0,N)")
    label(1136, 504, "(0,N)")
    label(1314, 504, "(0,N)")

    diamond(760, 700, 70, 30, "recebe")
    entity(900, 662, 180, 78, "TROFÉU", [("nome", True), ("valor", False)])
    poly([(760, 552), (760, 670)])
    poly([(830, 700), (900, 700)])
    label(768, 630, "(0,1)")
    label(848, 692, "(0,1)")

    diamond(1040, 760, 78, 32, "patrocina", "clube")
    poly([(575, 568), (575, 760), (962, 760)])
    poly([(1118, 760), (1436, 760), (1436, 560)])
    label(588, 748, "(0,N)")
    label(1288, 748, "(0,N)")

    # Recorte 3.
    panel(32, 832, 1616, 430, "3    Partidas, estádio e escalação")
    entity(52, 900, 230, 90, "ÁRBITRO", [
        ("código", True),
        ("nome, nascimento, nacionalidade", False),
    ])
    entity(52, 1060, 250, 108, "ESTÁDIO", [
        ("código", True),
        ("nome, capacidade", False),
        ("endereço (país, cidade, CEP, nº)", False),
    ])
    diamond(420, 1024, 80, 38, "tem", "função do árbitro")
    poly([(282, 945), (360, 945), (360, 1000), (340, 1000)])
    poly([(302, 1114), (360, 1114), (360, 1048), (340, 1048)])
    poly([(500, 1024), (860, 1024), (860, 990)])
    label(368, 990, "(0,N)")
    label(368, 1130, "(0,N)")
    label(620, 1014, "jogo (1,N)")

    entity(520, 888, 220, 86, "JOGADOR", [("especialização parcial", False)])
    diamond(830, 931, 72, 32, "joga", "gols, assist., posição")
    entity(930, 868, 250, 122, "JOGO", [
        ("código", True),
        ("placar, data, hora, fase", False),
    ])
    diamond(1288, 929, 70, 30, "pertence")
    entity(1390, 888, 210, 96, "COMPETIÇÃO", [
        ("id composto", True),
        ("nome, temporada", False),
    ])
    poly([(740, 931), (758, 931)])
    poly([(902, 931), (930, 931)])
    poly([(1180, 929), (1218, 929)])
    poly([(1358, 929), (1390, 929)])
    label(746, 922, "(0,N)")
    label(906, 922, "(0,N)")
    label(1186, 918, "(1,1)")
    label(1364, 918, "(1,N)")

    diamond(1040, 1124, 74, 30, "mandante")
    diamond(1200, 1124, 74, 30, "visitante")
    entity(1360, 1088, 210, 88, "CLUBE", [("código", True), ("nome, mascote, sede", False)])
    poly([(1055, 990), (1055, 1094)])
    poly([(1114, 1124), (1360, 1124)])
    poly([(1055, 1008), (1160, 1008), (1160, 1094)])
    poly([(1274, 1124), (1360, 1132)])
    label(1064, 1060, "(1,1)")
    label(1280, 1114, "(0,N)")
    label(1168, 1068, "(1,1)")

    add(
        '<text x="48" y="1296" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" font-size="13">'
        "(mín, máx) fica ao lado da entidade e conta em quantos vínculos daquele relacionamento ela entra. "
        "Cartão é multivalorado em joga: vários por partida, cada um com cor e minuto."
        "</text>"
    )
    add(
        '<text x="48" y="1320" fill="#5c6b7a" font-family="Inter, DejaVu Sans, sans-serif" font-size="13">'
        "TEM é ternário (árbitro, jogo e estádio). Presidente e federação são 1:1. "
        "Um jogo tem um mandante, um visitante e uma competição."
        "</text>"
    )
    add("</svg>")
    return "\n".join(parts)


def main():
    path = ROOT / "diagrama-conceitual.svg"
    path.write_text(build(), encoding="utf-8")
    print(path, path.stat().st_size)


if __name__ == "__main__":
    main()
