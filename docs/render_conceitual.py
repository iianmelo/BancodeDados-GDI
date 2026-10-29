#!/usr/bin/env python3
"""Esquema conceitual em notação de Chen / Elmasri-Navathe.

Retângulos, losangos e elipses, traço preto, fundo branco, fonte sem serifa.
Cardinalidade (mín, máx) ao lado da entidade.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
FONT = "Liberation Sans, Arial, Helvetica, sans-serif"

W, H = 1860, 1500


def esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


parts = []
boxes = []  # (x, y, w, h, name) for a rough overlap check


def add(fragment):
    parts.append(fragment)


def entity(x, y, w, h, name, weak=False):
    boxes.append((x, y, w, h, name))
    add(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" '
        f'stroke="#000000" stroke-width="1.2"/>'
    )
    if weak:
        add(
            f'<rect x="{x+4}" y="{y+4}" width="{w-8}" height="{h-8}" fill="none" '
            f'stroke="#000000" stroke-width="1"/>'
        )
    add(
        f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" fill="#000000" '
        f'font-family="{FONT}" font-size="13" font-weight="700">{esc(name)}</text>'
    )
    return (x + w / 2, y + h / 2, w, h)


def oval(cx, cy, w, h, text, key=False, partial=False, multi=False):
    x, y = cx - w / 2, cy - h / 2
    boxes.append((x, y, w, h, text))
    add(
        f'<ellipse cx="{cx}" cy="{cy}" rx="{w/2}" ry="{h/2}" fill="#ffffff" '
        f'stroke="#000000" stroke-width="1.1"/>'
    )
    if multi:
        add(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{w/2-4}" ry="{h/2-3.5}" fill="none" '
            f'stroke="#000000" stroke-width="1"/>'
        )
    deco = ""
    if key and not partial:
        deco = ' text-decoration="underline"'
    add(
        f'<text x="{cx}" y="{cy+4}" text-anchor="middle" fill="#000000"{deco} '
        f'font-family="{FONT}" font-size="12">{esc(text)}</text>'
    )
    if partial:
        # chave parcial: sublinhado tracejado
        tw = max(28, len(text) * 6.2)
        add(
            f'<line x1="{cx-tw/2}" y1="{cy+7}" x2="{cx+tw/2}" y2="{cy+7}" '
            f'stroke="#000000" stroke-width="1" stroke-dasharray="3 2"/>'
        )
    return (cx, cy, w, h)


def diamond(cx, cy, w, h, text, identifying=False):
    pts = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    boxes.append((cx - w / 2, cy - h / 2, w, h, text))
    add(f'<polygon points="{pts}" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>')
    if identifying:
        iw, ih = w * 0.78, h * 0.62
        pts2 = f"{cx},{cy-ih/2} {cx+iw/2},{cy} {cx},{cy+ih/2} {cx-iw/2},{cy}"
        add(f'<polygon points="{pts2}" fill="none" stroke="#000000" stroke-width="1"/>')
    add(
        f'<text x="{cx}" y="{cy+4}" text-anchor="middle" fill="#000000" '
        f'font-family="{FONT}" font-size="12">{esc(text)}</text>'
    )
    return (cx, cy, w, h)


def edge_rect(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (w / 2) / abs(dx) if dx else 1e9
    sy = (h / 2) / abs(dy) if dy else 1e9
    t = min(sx, sy)
    return cx + dx * t, cy + dy * t


def edge_diamond(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    denom = abs(dx) / (w / 2) + abs(dy) / (h / 2)
    t = 1 / denom
    return cx + dx * t, cy + dy * t


def line(x1, y1, x2, y2):
    add(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="#000000" stroke-width="1.15"/>'
    )


def card(px, py, text):
    add(
        f'<text x="{px}" y="{py}" fill="#000000" font-family="{FONT}" '
        f'font-size="11">{esc(text)}</text>'
    )


def connect(ent, dia, label, toward="auto"):
    ecx, ecy, ew, eh = ent
    dcx, dcy, dw, dh = dia
    x1, y1 = edge_rect(ecx, ecy, ew, eh, dcx, dcy)
    x2, y2 = edge_diamond(dcx, dcy, dw, dh, ecx, ecy)
    line(x1, y1, x2, y2)
    # rótulo perto da entidade, deslocado para não sentar no traço
    vx, vy = x2 - x1, y2 - y1
    length = (vx * vx + vy * vy) ** 0.5 or 1
    ux, uy = vx / length, vy / length
    px, py = -uy, ux
    lx = x1 + ux * 16 + px * 8
    ly = y1 + uy * 16 + py * 8
    anchor = "start" if px >= 0 else "end"
    add(
        f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" fill="#000000" '
        f'font-family="{FONT}" font-size="11">{esc(label)}</text>'
    )


def link_oval(shape, target, diamond_target=False):
    sx, sy, sw, sh = shape
    tx, ty, tw, th = target
    if diamond_target:
        x2, y2 = edge_diamond(tx, ty, tw, th, sx, sy)
    else:
        x2, y2 = edge_rect(tx, ty, tw, th, sx, sy)
    # borda da elipse
    dx, dy = x2 - sx, y2 - sy
    if dx == 0 and dy == 0:
        return
    # ellipse |dx|/(sw/2) normalized roughly along the ray
    denom = (dx / (sw / 2)) ** 2 + (dy / (sh / 2)) ** 2
    t = 1 / (denom ** 0.5)
    x1, y1 = sx + dx * t, sy + dy * t
    line(x1, y1, x2, y2)


def attrs_column(ent, items, side):
    ecx, ecy, ew, eh = ent
    gap_y = 34
    block = (len(items) - 1) * gap_y
    cy = ecy - block / 2
    shapes = []
    for text, key, partial, multi, w in items:
        if side == "left":
            cx = ecx - ew / 2 - 20 - w / 2
        else:
            cx = ecx + ew / 2 + 20 + w / 2
        shapes.append(oval(cx, cy, w, 28, text, key, partial, multi))
        cy += gap_y
    for sh in shapes:
        link_oval(sh, ent, False)
    return shapes


def stack_above(ent, items, cols=3):
    """items: (text, key, partial, multi, width). Returns oval shapes."""
    ecx, ecy, ew, eh = ent
    top = ecy - eh / 2
    shapes = []
    rows = [items[i : i + cols] for i in range(0, len(items), cols)]
    # de baixo para cima, a fileira mais próxima da entidade primeiro na leitura
    row_h = 42
    block_h = len(rows) * row_h
    y0 = top - 28 - (len(rows) - 1) * row_h
    for r, row in enumerate(rows):
        total_w = sum(it[4] for it in row) + 14 * (len(row) - 1)
        x = ecx - total_w / 2
        cy = y0 + r * row_h
        for text, key, partial, multi, w in row:
            cx = x + w / 2
            shapes.append(oval(cx, cy, w, 28, text, key, partial, multi))
            x += w + 14
    for sh in shapes:
        link_oval(sh, ent, False)
    return shapes


def build():
    parts.clear()
    boxes.clear()
    add(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">'
    )
    add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    add(
        f'<text x="36" y="28" fill="#000000" font-family="{FONT}" font-size="14" '
        f'font-weight="700">Esquema conceitual — notação de Chen / Elmasri-Navathe</text>'
    )

    # Entidades. Coordenadas são o canto superior esquerdo.
    presidente = entity(70, 168, 150, 40, "PRESIDENTE")
    federacao = entity(470, 168, 150, 40, "FEDERAÇÃO")
    competicao = entity(900, 168, 160, 40, "COMPETIÇÃO", weak=True)
    arbitro = entity(200, 520, 140, 40, "ÁRBITRO")
    empresa = entity(470, 520, 140, 40, "EMPRESA")
    clube = entity(980, 520, 130, 40, "CLUBE")
    estadio = entity(70, 900, 140, 40, "ESTÁDIO")
    jogo = entity(520, 900, 120, 40, "JOGO")
    funcionario = entity(980, 860, 170, 40, "FUNCIONÁRIO")
    jogador = entity(1005, 1180, 130, 40, "JOGADOR")
    trofeu = entity(1500, 860, 130, 40, "TROFÉU")

    # Atributos
    stack_above(presidente, [
        ("id", True, False, False, 52),
        ("nome", False, False, False, 70),
    ], cols=2)
    stack_above(federacao, [
        ("id", True, False, False, 52),
        ("nome", False, False, False, 70),
    ], cols=2)
    stack_above(competicao, [
        ("id artificial", False, True, False, 108),
        ("nome", False, False, False, 70),
        ("temporada", False, False, False, 96),
    ], cols=2)
    attrs_column(arbitro, [
        ("código", True, False, False, 72),
        ("nome", False, False, False, 70),
        ("dt. nasc.", False, False, False, 86),
        ("nacionalidade", False, False, False, 112),
    ], "left")
    stack_above(empresa, [
        ("CNPJ", True, False, False, 64),
        ("nome", False, False, False, 70),
    ], cols=2)
    attrs_column(clube, [
        ("código", True, False, False, 72),
        ("nome", False, False, False, 70),
        ("mascote", False, False, False, 80),
        ("sede", False, False, False, 60),
    ], "right")
    attrs_column(jogo, [
        ("código", True, False, False, 72),
        ("placar", False, False, False, 68),
        ("data", False, False, False, 56),
        ("hora", False, False, False, 56),
        ("fase", False, False, False, 56),
    ], "left")
    attrs_column(funcionario, [
        ("id", True, False, False, 48),
        ("nome", False, False, False, 68),
        ("salário", False, False, False, 72),
        ("dt. nasc.", False, False, False, 86),
        ("nacionalidade", False, False, False, 112),
    ], "right")
    stack_above(trofeu, [
        ("nome", True, False, False, 70),
        ("valor", False, False, False, 64),
    ], cols=2)

    # endereço composto, abaixo do estádio
    end = oval(140, 1020, 96, 28, "endereço")
    link_oval(end, estadio, False)
    kids = []
    labels = [("país", 56), ("cidade", 68), ("CEP", 52), ("número", 72)]
    total = sum(w for _, w in labels) + 10 * 3
    x = 140 - total / 2
    for text, w in labels:
        kids.append(oval(x + w / 2, 1072, w, 26, text))
        x += w + 10
    for sh in kids:
        link_oval(sh, end, False)

    # Relacionamentos
    preside = diamond(345, 188, 120, 64, "preside")
    connect(presidente, preside, "(1,1)")
    connect(federacao, preside, "(1,1)")

    realiza = diamond(760, 188, 130, 70, "realiza", identifying=True)
    connect(federacao, realiza, "(0,n)")
    connect(competicao, realiza, "(1,1)")

    garante = diamond(1360, 188, 150, 72, "garante vaga")
    line(1060, 176, 1285, 170)
    line(1060, 200, 1285, 206)
    card(1120, 158, "(0,n) menor")
    card(1120, 218, "(0,n) maior")

    faz = diamond(270, 400, 130, 64, "faz parte")
    connect(federacao, faz, "(0,n)")
    connect(arbitro, faz, "(0,n)")

    pat_c = diamond(700, 400, 130, 64, "patrocina")
    connect(competicao, pat_c, "(0,n)")
    connect(empresa, pat_c, "(0,n)")
    for sh in (
        oval(600, 318, 58, 26, "valor"),
        oval(710, 300, 112, 26, "dt. contrato"),
        oval(830, 318, 78, 26, "duração"),
    ):
        link_oval(sh, pat_c, True)

    pat_k = diamond(800, 540, 130, 58, "patrocina")
    connect(empresa, pat_k, "(0,n)")
    connect(clube, pat_k, "(0,n)")
    for sh in (
        oval(690, 470, 58, 26, "valor"),
        oval(800, 452, 112, 26, "dt. contrato"),
        oval(920, 470, 78, 26, "duração"),
    ):
        link_oval(sh, pat_k, True)

    ligado = diamond(1065, 700, 110, 54, "ligado")
    connect(clube, ligado, "(0,n)")
    connect(funcionario, ligado, "(0,n)")
    for sh in (
        oval(1188, 668, 92, 26, "temporada"),
        oval(1196, 704, 72, 26, "função"),
    ):
        link_oval(sh, ligado, True)

    participa = diamond(1140, 400, 130, 64, "participa")
    connect(competicao, participa, "(0,n)")
    connect(clube, participa, "(0,n)")
    col = oval(1288, 400, 90, 26, "colocação")
    link_oval(col, participa, True)

    recebe = diamond(1360, 760, 110, 58, "recebe")
    connect(participa, recebe, "(0,1)")
    connect(trofeu, recebe, "(0,1)")

    # especialização parcial
    fx, fy, fw, fh = funcionario
    jx, jy, jw, jh = jogador
    line(fx, fy + fh / 2, fx, 1120)
    add('<circle cx="1065" cy="1120" r="13" fill="#ffffff" stroke="#000000" stroke-width="1.15"/>')
    line(1065, 1133, jx, jy - jh / 2)
    card(1084, 1124, "parcial")

    joga = diamond(760, 1080, 100, 52, "joga")
    connect(jogador, joga, "(0,n)")
    connect(jogo, joga, "(0,n)")
    for sh in (
        oval(680, 1160, 56, 26, "gols"),
        oval(750, 1178, 72, 26, "assist."),
        oval(830, 1160, 76, 26, "posição"),
    ):
        link_oval(sh, joga, True)
    cartao = oval(900, 1168, 72, 30, "cartão", multi=True)
    link_oval(cartao, joga, True)
    cor = oval(860, 1220, 48, 24, "cor")
    minuto = oval(930, 1220, 68, 24, "minuto")
    link_oval(cor, cartao, False)
    link_oval(minuto, cartao, False)

    mandante = diamond(780, 900, 120, 52, "mandante")
    visitante = diamond(900, 980, 120, 52, "visitante")
    connect(jogo, mandante, "(1,1)")
    connect(clube, mandante, "(0,n)")
    connect(jogo, visitante, "(1,1)")
    connect(clube, visitante, "(0,n)")

    pertence = diamond(620, 760, 120, 52, "pertence")
    connect(jogo, pertence, "(1,1)")
    connect(competicao, pertence, "(1,n)")

    tem = diamond(300, 760, 100, 64, "tem")
    connect(arbitro, tem, "(0,n)")
    connect(estadio, tem, "(0,n)")
    connect(jogo, tem, "(1,n)")
    funcao = oval(300, 700, 70, 26, "função")
    link_oval(funcao, tem, True)

    add(
        f'<text x="36" y="{H-28}" fill="#000000" font-family="{FONT}" font-size="11">'
        "(mín, máx) ao lado da entidade. Retângulo duplo e losango duplo: entidade fraca e relacionamento identificador. "
        "Elipse dupla: multivalorado. Sublinhado tracejado: chave parcial. Círculo: especialização parcial."
        "</text>"
    )
    add("</svg>")
    return "\n".join(parts)


def main():
    svg = build()
    path = ROOT / "diagrama-conceitual.svg"
    path.write_text(svg, encoding="utf-8")
    # sobreposição grosseira (caixas-limite)
    hits = 0
    for i, a in enumerate(boxes):
        for b in boxes[i + 1 :]:
            ax, ay, aw, ah, an = a
            bx, by, bw, bh, bn = b
            if ax + aw > bx + 4 and bx + bw > ax + 4 and ay + ah > by + 4 and by + bh > ay + 4:
                hits += 1
                if hits <= 25:
                    print(f"overlap {an!r} / {bn!r}")
    print(path, "overlaps", hits)


if __name__ == "__main__":
    main()
