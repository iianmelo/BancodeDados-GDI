#!/usr/bin/env python3
"""Gera o Mermaid do esquema e as figuras de resultado.

As figuras de resultado reproduzem a saída obtida no SQL*Plus contra
Oracle AI Database 26ai Free Release 23.26.3.0.0 (imagem
gvenzl/oracle-free:23-slim-faststart), depois de SQL/create.sql,
SQL/povoamento.sql e SQL/Consultas.sql.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONT = "Inter"
MONO = "JetBrains Mono"

NAVY = "#1e3a5f"
GREEN = "#1f6b4a"
INK = "#243140"
MUTED = "#5c6b7a"
LINE = "#8b97a3"
PAPER = "#f6f3ec"
CARD = "#ffffff"
GOLD = "#8a6232"



TABLES = [
    ("FEDERACAO", "inst", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "ID_FED", "INT"),
    ]),
    ("PRESIDENTE_DA_FEDERACAO", "inst", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "ID", "INT"),
        ("FK", "ID_FED", "INT"),
    ]),
    ("ARBITRO", "inst", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "CODIGO", "INT"),
        ("", "DT_NASCIMENTO", "DATE"),
        ("", "NACIONALIDADE", "VARCHAR(30)"),
    ]),
    ("FAZ_PARTE", "inst", [
        ("PK FK", "CODIGO_ARBITRO", "INT"),
        ("PK FK", "ID_FED", "INT"),
    ]),
    ("COMPETICAO", "inst", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "ID_ARTIFICIAL", "INT"),
        ("PK FK", "ID_FED", "INT"),
        ("", "TEMPORADA", "INT"),
    ]),
    ("GARANTE_VAGA", "inst", [
        ("PK FK", "ID_ARTIFICIAL_MAIOR", "INT"),
        ("PK FK", "ID_FED_MAIOR", "INT"),
        ("PK FK", "ID_ARTIFICIAL_MENOR", "INT"),
        ("PK FK", "ID_FED_MENOR", "INT"),
    ]),
    ("ESTADIO", "partida", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "COD_ESTADIO", "INT"),
        ("", "CAPACIDADE", "INT"),
        ("", "END_PAIS", "VARCHAR(30)"),
        ("", "END_CIDADE", "VARCHAR(30)"),
        ("", "END_CEP", "INT"),
        ("", "END_NUMERO", "INT"),
    ]),
    ("JOGO", "partida", [
        ("PK", "CODIGO", "INT"),
        ("", "DATA_", "DATE"),
        ("", "FASE", "VARCHAR(30)"),
        ("FK", "ID_ARTIFICIAL", "INT"),
        ("FK", "ID_FED", "INT"),
        ("FK NN", "CODIGO_VISITANTE", "INT"),
        ("FK NN", "CODIGO_MANDANTE", "INT"),
    ]),
    ("TEM", "partida", [
        ("PK FK", "COD_ARBITRO", "INT"),
        ("PK FK", "COD_JOGO", "INT"),
        ("", "FUNCAO_ARBITRO", "VARCHAR(30)"),
        ("", "PLACAR", "VARCHAR(30)"),
        ("FK NN", "COD_ESTADIO", "INT"),
    ]),
    ("EMPRESA", "clube", [
        ("UQ", "NOME", "VARCHAR(30)"),
        ("PK", "CNPJ", "INT"),
    ]),
    ("CLUBE", "clube", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "CODIGO", "INT"),
        ("", "MASCOTE", "VARCHAR(30)"),
        ("", "SEDE", "VARCHAR(30)"),
    ]),
    ("TROFEU", "clube", [
        ("PK", "NOME", "VARCHAR(30)"),
        ("", "VALOR", "INT"),
    ]),
    ("PAT_CLUBE", "clube", [
        ("PK FK", "CODIGO_CLUBE", "INT"),
        ("PK FK", "CNPJ_EMPRESA", "INT"),
        ("PK", "DT_CONTRATO", "DATE"),
        ("", "VALOR", "INT"),
        ("", "DURACAO", "INT"),
    ]),
    ("PAT_COMP", "clube", [
        ("PK FK", "ID_COMP", "INT"),
        ("PK FK", "ID_FED", "INT"),
        ("PK FK", "CNPJ_EMPRESA", "INT"),
        ("PK", "DT_CONTRATO", "DATE"),
        ("", "VALOR", "INT"),
        ("", "DURACAO", "INT"),
    ]),
    ("PARTICIPA", "clube", [
        ("PK FK", "CODIGO", "INT"),
        ("PK FK", "ID_ARTIFICIAL", "INT"),
        ("PK FK", "ID_FED", "INT"),
        ("FK", "NOME_TROFEU", "VARCHAR(30)"),
        ("", "COLOCACAO", "VARCHAR(30)"),
    ]),
    ("FUNCIONARIO", "pessoa", [
        ("", "NOME", "VARCHAR(30)"),
        ("PK", "ID_FUNC", "INT"),
        ("", "SALARIO", "INT"),
        ("", "DT_NASCIMENTO", "DATE"),
        ("", "NACIONALIDADE", "VARCHAR(30)"),
    ]),
    ("JOGADOR", "pessoa", [
        ("PK FK", "ID_JOGADOR", "INT"),
    ]),
    ("LIGADO", "pessoa", [
        ("PK FK", "ID_FUNC", "INT"),
        ("PK FK", "CODIGO_CLUBE", "INT"),
        ("PK", "TEMPORADA", "INT"),
        ("PK", "FUNCAO", "VARCHAR(30)"),
    ]),
    ("JOGADOR_PARTICIPA", "pessoa", [
        ("PK FK", "ID_FUNC", "INT"),
        ("PK FK", "CODIGO_JOGO", "INT"),
        ("", "N_GOLS", "INT"),
        ("", "N_ASSIST", "INT"),
        ("", "POSICAO", "VARCHAR(30)"),
    ]),
    ("CARTOES", "pessoa", [
        ("PK FK", "ID_FUNC", "INT"),
        ("PK FK", "COD_JOGO", "INT"),
        ("PK", "COR", "VARCHAR(50)"),
        ("PK", "MINUTO", "TIMESTAMP"),
    ]),
]



def mermaid():
    lines = [
        "erDiagram",
        "    %% Gerado a partir de SQL/create.sql. Cardinalidade segue as FKs implementadas.",
    ]
    for name, _group, cols in TABLES:
        lines.append(f"    {name} {{")
        for flag, col, typ in cols:
            kind = "PK" if "PK" in flag else ("FK" if "FK" in flag else "")
            safe_type = typ.replace("(", "_").replace(")", "")
            mark = f" {kind}" if kind else ""
            lines.append(f"        {safe_type} {col}{mark}")
        lines.append("    }")
    rels = [
        ("FEDERACAO", "|o--o{", "PRESIDENTE_DA_FEDERACAO", "id_fed"),
        ("FEDERACAO", "||--o{", "COMPETICAO", "organiza"),
        ("FEDERACAO", "||--o{", "FAZ_PARTE", "quadro"),
        ("ARBITRO", "||--o{", "FAZ_PARTE", "filia"),
        ("COMPETICAO", "||--o{", "GARANTE_VAGA", "maior"),
        ("COMPETICAO", "||--o{", "GARANTE_VAGA", "menor"),
        ("COMPETICAO", "|o--o{", "JOGO", "pertence"),
        ("CLUBE", "||--o{", "JOGO", "mandante"),
        ("CLUBE", "||--o{", "JOGO", "visitante"),
        ("JOGO", "||--o{", "TEM", "apita"),
        ("ARBITRO", "||--o{", "TEM", "atua"),
        ("ESTADIO", "||--o{", "TEM", "sedia"),
        ("COMPETICAO", "||--o{", "PAT_COMP", "patrocinio"),
        ("EMPRESA", "||--o{", "PAT_COMP", "patrocina"),
        ("CLUBE", "||--o{", "PAT_CLUBE", "patrocinio"),
        ("EMPRESA", "||--o{", "PAT_CLUBE", "patrocina"),
        ("CLUBE", "||--o{", "PARTICIPA", "disputa"),
        ("COMPETICAO", "||--o{", "PARTICIPA", "disputa"),
        ("TROFEU", "|o--o{", "PARTICIPA", "trofeu"),
        ("FUNCIONARIO", "||--o{", "LIGADO", "vinculo"),
        ("CLUBE", "||--o{", "LIGADO", "vinculo"),
        ("FUNCIONARIO", "||--o|", "JOGADOR", "pode_ser"),
        ("FUNCIONARIO", "||--o{", "JOGADOR_PARTICIPA", "atua"),
        ("JOGO", "||--o{", "JOGADOR_PARTICIPA", "escalacao"),
        ("JOGADOR_PARTICIPA", "||--o{", "CARTOES", "cartao"),
    ]
    for a, card, b, label in rels:
        lines.append(f"    {a} {card} {b} : {label}")
    return "\n".join(lines) + "\n"


def font(size, bold=False):
    path = (
        "/usr/share/fonts/truetype/macos/Inter-SemiBold.ttf"
        if bold
        else "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"
    )
    return ImageFont.truetype(path, size)


def mono(size):
    for candidate in [
        "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    ]:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    found = list(Path("/usr/share/fonts").rglob("JetBrainsMono-Regular.ttf"))
    if found:
        return ImageFont.truetype(str(found[0]), size)
    return ImageFont.load_default()


def wrap_text(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def result_consultas():
    W, H = 1600, 1280
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    title = font(36, True)
    sub = font(18)
    head = font(20, True)
    body = mono(18)
    small = font(15)
    d.rectangle((0, 0, W, 118), fill=NAVY)
    d.text((48, 28), "Consultas executadas no Oracle", font=title, fill="white")
    d.text((48, 74), "SQL*Plus  ·  Oracle AI Database 26ai Free Release 23.26.3.0.0  ·  carga de SQL/povoamento.sql", font=sub, fill="#d5e2f0")

    panels = [
        (48, 150, 760, 430, "Junção interna — empresa e clube patrocinado", ["EMPRESA", "CLUBE"], [
            ["SPOTIFY", "SPORT CLUB DO RECIFE"],
            ["NIKE", "SPORT CLUB DO RECIFE"],
            ["EMIRATES", "SANTA CRUZ"],
            ["EA", "SANTA CRUZ"],
        ], "4 linhas. O SELECT projeta E.NOME, C.NOME."),
        (800, 150, 1552, 500, "GROUP BY / HAVING — média salarial acima de 1000", ["CLUBE", "MEDIA_SALARIO"], [
            ["SPORT CLUB DO RECIFE", "275000"],
            ["CHELSEA", "116666.66"],
            ["BARCELONA", "500000"],
            ["REAL MADRID", "150000"],
            ["PSG", "800000"],
            ["SANTOS", "100000"],
        ], "TRUNC(AVG(SALARIO), 2). Sem ORDER BY; ordem desta execução."),
        (48, 540, 760, 900, "Semijoin (EXISTS) — funcionários que entraram em jogo", ["NOME"], [
            ["Neymar"], ["Messi"], ["Romarinho"], ["Ze Roberto"], ["Caíque França"],
        ], "5 linhas, via JOGADOR_PARTICIPA."),
        (800, 540, 1552, 860, "UNION — empresas que patrocinam clube ou competição", ["NOME"], [
            ["SPOTIFY"], ["NIKE"], ["EMIRATES"], ["EA"],
        ], "EMIRATES aparece nos dois ramos e sai uma vez."),
        (48, 930, 760, 1180, "Subconsulta de linha — mesmo ano e nacionalidade do id 1", ["NOME"], [
            ["Ze da Silva"], ["Francisco da Limpeza"],
        ], "Ano 1999 e nacionalidade BRASILEIRO, inclusive o próprio."),
        (800, 930, 1552, 1180, "Anti-join e subconsulta escalar", ["CONSULTA", "RESULTADO"], [
            ["Federações sem presidente", "0 linhas"],
            ["Clube da EMIRATES", "código 1"],
            ["Fora de PAT_COMP", "35 de 36"],
        ], "As 11 federações da carga têm presidente. Só a EMIRATES patrocina competição."),
    ]
    for x0, y0, x1, y1, title_txt, headers, rows, note in panels:
        d.rounded_rectangle((x0, y0, x1, y1), radius=16, fill=CARD, outline="#e1dbd0", width=2)
        d.text((x0 + 22, y0 + 16), title_txt, font=head, fill=NAVY)
        y = y0 + 58
        col_w = (x1 - x0 - 44) / len(headers)
        for i, h in enumerate(headers):
            d.text((x0 + 22 + i * col_w, y), h, font=small, fill=GOLD)
        y += 28
        d.line((x0 + 22, y, x1 - 22, y), fill="#eadfce", width=1)
        y += 10
        for row in rows:
            for i, cell in enumerate(row):
                d.text((x0 + 22 + i * col_w, y), cell, font=body, fill=INK)
            y += 30
        note_font = font(14)
        note_lines = wrap_text(d, note, note_font, x1 - x0 - 44)
        ny = y1 - 16 - 18 * len(note_lines)
        for line in note_lines:
            d.text((x0 + 22, ny), line, font=note_font, fill=MUTED)
            ny += 18
    d.text((48, 1224), "Fonte: execução de SQL/Consultas.sql nesta carga. Não há ORDER BY nas consultas originais.", font=small, fill=MUTED)
    return img


def result_plsql():
    W, H = 1400, 1040
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 118), fill=GREEN)
    d.text((48, 28), "PL/SQL executado no Oracle", font=font(36, True), fill="white")
    d.text((48, 74), "Gatilhos, procedure e funções de SQL/Consultas.sql  ·  DBMS_OUTPUT", font=font(18), fill="#e5f6ee")
    cards = [
        ("Gatilho MudancaDeNome", "BEFORE UPDATE OF NOME ON FUNCIONARIO", "UPDATE FUNCIONARIO SET NOME = 'Ze da Silva Junior' WHERE ID_FUNC = 1;", "NOVO NOME: Ze da Silva Junior", "O nome foi restaurado em seguida e a sessão deu ROLLBACK. A carga permanece como no povoamento."),
        ("Procedure AtualizarNomeEstadio", "Chamada já presente no script", "AtualizarNomeEstadio(0019, 'NEOQUIMICA ARENA');", "Nome do estádio atualizado com sucesso.", "O estádio 19 já se chamava NEOQUIMICA ARENA. SQL%ROWCOUNT acusou a linha."),
        ("Função CalcularSomaSalarios", "SUM(SALARIO) de FUNCIONARIO", "v_soma_total_salarios := CalcularSomaSalarios;", "Soma total dos salários de todos os funcionários: 4431700", "16 funcionários. O script não declara moeda."),
        ("Função S_CLUBES", "COUNT de CLUBE cujo nome começa com S", "qtd := S_CLUBES;", "Quantidade de clubes que comecam com S: 5", "SPORT, SANTA CRUZ, SAO PAULO FC, SANTOS e SEVILLA."),
    ]
    y = 150
    for title, subtitle, call, output, note in cards:
        d.rounded_rectangle((48, y, 1352, y + 188), radius=16, fill=CARD, outline="#e1dbd0", width=2)
        d.text((72, y + 14), title, font=font(22, True), fill=NAVY)
        d.text((72, y + 44), subtitle, font=font(15), fill=MUTED)
        d.text((72, y + 70), call, font=mono(16), fill=INK)
        d.rounded_rectangle((72, y + 100, 1320, y + 136), radius=8, fill="#eef6f1")
        d.text((86, y + 106), output, font=mono(16), fill=GREEN)
        d.text((72, y + 150), note, font=font(15), fill=MUTED)
        y += 200
    d.text(
        (48, 980),
        "Nenhum objeto em USER_ERRORS depois da compilação. Não há CURSOR explícito; a procedure usa o cursor implícito SQL%ROWCOUNT.",
        font=font(15),
        fill=MUTED,
    )
    return img



def main():
    (ROOT / "esquema-logico.mmd").write_text(mermaid(), encoding="utf-8")
    result_consultas().save(ROOT / "resultados-consultas.png", optimize=True)
    result_plsql().save(ROOT / "resultados-plsql.png", optimize=True)
    print("pngs", (ROOT / "resultados-consultas.png").stat().st_size, (ROOT / "resultados-plsql.png").stat().st_size)


if __name__ == "__main__":
    main()
