from forms_defaults import DRIVE_FOLDER_NAME, build_choice_question, create_quiz_form

QUIZ_QUESTIONS = [
    {
        "title": "O que significa a sigla CSS?",
        "options": [
            "Cascading Style Sheets (Folhas de Estilo em Cascata)",
            "Computer Style System (Sistema de Estilo do Computador)",
            "Creative Site Script (Script Criativo de Sites)",
            "Code Style Syntax (Sintaxe de Estilo do Código)",
        ],
        "correct": "Cascading Style Sheets (Folhas de Estilo em Cascata)",
        "points": 5,
        "when_wrong": "CSS significa Cascading Style Sheets, ou Folhas de Estilo em Cascata.",
    },
    {
        "title": "Qual é a função principal do CSS em um site?",
        "options": [
            "Definir cores, fontes, espaçamento e aparência dos elementos",
            "Organizar a estrutura de títulos, parágrafos e imagens",
            "Enviar dados de um formulário para o servidor",
            "Criar campos de texto, botões e listas suspensas",
        ],
        "correct": "Definir cores, fontes, espaçamento e aparência dos elementos",
        "points": 5,
        "when_wrong": "O CSS é a alma visual do site: cores, fontes, espaçamento e posição.",
    },
    {
        "title": "No HTML da Sonho Store, o CSS foi colocado de qual forma?",
        "options": [
            "CSS interno, dentro da tag <style> no <head>",
            "CSS externo, em um arquivo .css separado",
            "CSS inline, no atributo style de cada tag",
            "CSS automático, sem nenhum código escrito",
        ],
        "correct": "CSS interno, dentro da tag <style> no <head>",
        "points": 5,
        "when_wrong": "A loja usa CSS interno: as regras ficam dentro de <style> no <head>.",
    },
    {
        "title": "Qual código liga um arquivo CSS externo à página HTML?",
        "options": [
            '<link rel="stylesheet" href="estilo.css">',
            '<style src="estilo.css">',
            '<css href="estilo.css">',
            '<link rel="script" src="estilo.css">',
        ],
        "correct": '<link rel="stylesheet" href="estilo.css">',
        "points": 5,
        "when_wrong": "Use <link rel=\"stylesheet\" href=\"arquivo.css\"> para CSS externo.",
    },
    {
        "title": "Qual é a estrutura correta de uma regra CSS?",
        "options": [
            "seletor { propriedade: valor; }",
            "propriedade { seletor: valor; }",
            "seletor ( valor = propriedade )",
            "<seletor propriedade=\"valor\">",
        ],
        "correct": "seletor { propriedade: valor; }",
        "points": 5,
        "when_wrong": "A sintaxe é: seletor { propriedade: valor; }",
    },
    {
        "title": "Qual propriedade muda a cor do texto (da fonte)?",
        "options": ["color", "background-color", "font-family", "border"],
        "correct": "color",
        "points": 5,
        "when_wrong": "A propriedade color altera a cor do texto. background-color altera o fundo.",
    },
    {
        "title": "Qual propriedade muda a cor de fundo de um elemento?",
        "options": ["background-color", "color", "border-color", "font-color"],
        "correct": "background-color",
        "points": 5,
        "when_wrong": "Use background-color para o fundo e color para o texto.",
    },
    {
        "title": "No CSS da loja, o preço (.card-preco) fica verde. Qual declaração faz isso?",
        "options": [
            "color: #16a34a;",
            "background-color: #16a34a;",
            "border: #16a34a;",
            "font-family: #16a34a;",
        ],
        "correct": "color: #16a34a;",
        "points": 5,
        "when_wrong": "color: #16a34a; muda a cor do texto do preço para verde.",
    },
    {
        "title": "Qual atributo HTML aplica uma classe a um botão?",
        "options": [
            'class="botao"',
            'style="botao"',
            'classe="botao"',
            'css="botao"',
        ],
        "correct": 'class="botao"',
        "points": 5,
        "when_wrong": "No HTML o atributo correto é class=\"\", e não classe, style ou css.",
    },
    {
        "title": "Qual seletor CSS estiliza todos os elementos com class=\"card\"?",
        "options": [".card", "#card", "card", "*card"],
        "correct": ".card",
        "points": 5,
        "when_wrong": "O ponto (.) indica seletor de classe: .card.",
    },
    {
        "title": "Qual seletor CSS estiliza o campo com id=\"campoBusca\"?",
        "options": ["#campoBusca", ".campoBusca", "id=campoBusca", "campoBusca"],
        "correct": "#campoBusca",
        "points": 5,
        "when_wrong": "A cerquilha (#) indica seletor de ID: #campoBusca.",
    },
    {
        "title": "Qual seletor altera só os parágrafos <p> que estão dentro de um <article>?",
        "options": ["article p", "p article", "article.p", "article + p"],
        "correct": "article p",
        "points": 5,
        "when_wrong": "O seletor combinado article p pega <p> que estão dentro de <article>.",
    },
    {
        "title": "Qual propriedade cria espaço INTERNO, entre o conteúdo e a borda?",
        "options": ["padding", "margin", "border", "gap"],
        "correct": "padding",
        "points": 5,
        "when_wrong": "padding é o espaço interno. margin é o espaço externo.",
    },
    {
        "title": "Qual propriedade cria espaço EXTERNO, entre uma caixa e as outras?",
        "options": ["margin", "padding", "width", "line-height"],
        "correct": "margin",
        "points": 5,
        "when_wrong": "margin é o espaço externo entre as caixas.",
    },
    {
        "title": "No Box Model, qual é a ordem das camadas de DENTRO para FORA?",
        "options": [
            "conteúdo → padding → border → margin",
            "margin → border → padding → conteúdo",
            "border → conteúdo → padding → margin",
            "padding → conteúdo → margin → border",
        ],
        "correct": "conteúdo → padding → border → margin",
        "points": 5,
        "when_wrong": "De dentro para fora: conteúdo, padding, border e margin.",
    },
    {
        "title": "Qual propriedade define o contorno (a \"parede\") da caixa?",
        "options": ["border", "padding", "margin", "outline-text"],
        "correct": "border",
        "points": 5,
        "when_wrong": "border é o contorno da caixa. Exemplo: border: 2px solid black;",
    },
    {
        "title": "Qual propriedade arredonda os cantos, como na foto de perfil da loja?",
        "options": ["border-radius", "border", "padding", "text-align"],
        "correct": "border-radius",
        "points": 5,
        "when_wrong": "border-radius arredonda os cantos. 50% deixa a foto circular.",
    },
    {
        "title": "Qual propriedade define o tamanho da fonte?",
        "options": ["font-size", "font-weight", "font-style", "line-height"],
        "correct": "font-size",
        "points": 5,
        "when_wrong": "font-size define o tamanho do texto, por exemplo 16px.",
    },
    {
        "title": "Qual propriedade deixa o texto em negrito, como no preço da loja?",
        "options": ["font-weight", "font-style", "text-decoration", "font-family"],
        "correct": "font-weight",
        "points": 5,
        "when_wrong": "font-weight: bold; deixa o texto em negrito.",
    },
    {
        "title": "Qual propriedade escolhe a família da fonte, como \"Segoe UI\", Arial?",
        "options": ["font-family", "font-size", "font-weight", "text-align"],
        "correct": "font-family",
        "points": 5,
        "when_wrong": "font-family define a fonte. Sempre coloque um plano B, como sans-serif.",
    },
    {
        "title": "Qual propriedade alinha o texto à esquerda, ao centro ou à direita?",
        "options": ["text-align", "align-items", "justify-content", "font-style"],
        "correct": "text-align",
        "points": 5,
        "when_wrong": "text-align alinha o texto. Exemplo: text-align: center;",
    },
    {
        "title": "Qual formato de cor é hexadecimal, como o verde da loja?",
        "options": ["#16a34a", "rgb(22, 163, 74)", "green", "rgba(22, 163, 74, 1)"],
        "correct": "#16a34a",
        "points": 5,
        "when_wrong": "Hexadecimal começa com # e tem 6 dígitos, como #16a34a.",
    },
    {
        "title": "Qual código usa RGB para deixar o texto vermelho?",
        "options": [
            "color: rgb(255, 0, 0);",
            "color: #vermelho;",
            "color: rgba(red);",
            "font-color: rgb(255);",
        ],
        "correct": "color: rgb(255, 0, 0);",
        "points": 5,
        "when_wrong": "Em RGB, vermelho é rgb(255, 0, 0). Os valores vão de 0 a 255.",
    },
    {
        "title": "Qual valor de color em hexadecimal representa o branco?",
        "options": ["#ffffff", "#000000", "#ff0000", "#16a34a"],
        "correct": "#ffffff",
        "points": 5,
        "when_wrong": "#ffffff é branco e #000000 é preto.",
    },
    {
        "title": "Qual propriedade define se o elemento é bloco, linha, flex ou some da tela?",
        "options": ["display", "position", "float", "visibility-box"],
        "correct": "display",
        "points": 5,
        "when_wrong": "display controla como o elemento aparece: block, inline, flex, grid ou none.",
    },
    {
        "title": "A classe .escondido oculta produtos na busca. Qual declaração faz isso?",
        "options": [
            "display: none;",
            "display: block;",
            "display: flex;",
            "visibility: inline;",
        ],
        "correct": "display: none;",
        "points": 5,
        "when_wrong": "display: none; esconde o elemento. É o que .escondido faz na loja.",
    },
    {
        "title": "Qual valor de display deixa o elemento na mesma linha, mas permite width e height?",
        "options": ["inline-block", "inline", "block", "none"],
        "correct": "inline-block",
        "points": 5,
        "when_wrong": "inline-block fica na linha como inline, mas aceita largura e altura.",
    },
    {
        "title": "Qual código ativa o Flexbox no container, como no cabeçalho .topo?",
        "options": [
            "display: flex;",
            "display: grid;",
            "display: block;",
            "flex: display;",
        ],
        "correct": "display: flex;",
        "points": 5,
        "when_wrong": "Para usar Flexbox, o container precisa de display: flex;",
    },
    {
        "title": "Qual propriedade alinha os itens na HORIZONTAL no Flexbox?",
        "options": ["justify-content", "align-items", "flex-direction", "text-align"],
        "correct": "justify-content",
        "points": 5,
        "when_wrong": "justify-content alinha no eixo horizontal. align-items alinha no vertical.",
    },
    {
        "title": "No .topo da loja, logo e perfil ficam nas extremidades. Qual valor faz isso?",
        "options": ["space-between", "center", "flex-end", "stretch"],
        "correct": "space-between",
        "points": 5,
        "when_wrong": "justify-content: space-between; coloca espaço igual entre os itens.",
    },
    {
        "title": "Qual propriedade alinha os itens na VERTICAL no Flexbox?",
        "options": ["align-items", "justify-content", "text-align", "flex-direction"],
        "correct": "align-items",
        "points": 5,
        "when_wrong": "align-items alinha no eixo vertical. O padrão é stretch.",
    },
    {
        "title": "No body da loja, os blocos ficam um abaixo do outro. Qual declaração faz isso?",
        "options": [
            "flex-direction: column;",
            "flex-direction: row;",
            "justify-content: center;",
            "display: inline;",
        ],
        "correct": "flex-direction: column;",
        "points": 5,
        "when_wrong": "flex-direction: column; empilha os itens de cima para baixo.",
    },
    {
        "title": "Qual código ativa o Grid Layout no container, como na lista de produtos?",
        "options": [
            "display: grid;",
            "display: flex;",
            "display: table;",
            "grid: display;",
        ],
        "correct": "display: grid;",
        "points": 5,
        "when_wrong": "Para usar Grid, o container precisa de display: grid;",
    },
    {
        "title": "A lista de produtos (.lista) tem 4 colunas iguais. Qual código faz isso?",
        "options": [
            "grid-template-columns: 1fr 1fr 1fr 1fr;",
            "grid-template-rows: 1fr 1fr 1fr 1fr;",
            "flex-direction: row;",
            "columns: 4;",
        ],
        "correct": "grid-template-columns: 1fr 1fr 1fr 1fr;",
        "points": 5,
        "when_wrong": "Cada 1fr é uma coluna. 1fr 1fr 1fr 1fr cria 4 colunas iguais.",
    },
    {
        "title": "Qual propriedade cria o espaço entre os cards na grade da loja?",
        "options": ["gap", "padding", "margin", "border"],
        "correct": "gap",
        "points": 5,
        "when_wrong": "gap cria espaço entre os itens do Grid (e também do Flexbox).",
    },
    {
        "title": "Qual atalho cria 4 colunas iguais no Grid?",
        "options": [
            "repeat(4, 1fr)",
            "repeat(1fr, 4)",
            "columns: repeat(4)",
            "1fr x 4",
        ],
        "correct": "repeat(4, 1fr)",
        "points": 5,
        "when_wrong": "repeat(4, 1fr) é o atalho de 1fr 1fr 1fr 1fr.",
    },
]


def main():
    print("Criando o formulário...")
    form_service, form = create_quiz_form(
        "Quiz: CSS — Propriedades, Seletores e Layout",
        "Quiz_CSS_Propriedades_Seletores",
    )
    form_id = form["formId"]

    print(f"\nFormulário criado com sucesso!")
    print(f"Link para responder: {form['responderUri']}")
    print(f"Link para editar: https://docs.google.com/forms/d/{form_id}/edit")
    print(f'Formulário salvo na pasta "{DRIVE_FOLDER_NAME}".\n')

    requests = []
    for index, question in enumerate(QUIZ_QUESTIONS):
        question_with_index = {**question, "index": index}
        requests.append(build_choice_question(question_with_index))

    print("Adicionando perguntas...")
    form_service.forms().batchUpdate(formId=form_id, body={"requests": requests}).execute()
    print(f"Quiz criado com {len(QUIZ_QUESTIONS)} perguntas ({len(QUIZ_QUESTIONS) * 5} pontos no total).")


if __name__ == '__main__':
    main()
