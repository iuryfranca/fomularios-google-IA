from forms_defaults import DRIVE_FOLDER_NAME, build_choice_question, create_quiz_form

QUIZ_QUESTIONS = [
    {
        "title": "Qual marcação HTML transforma 'Bem-vindo ao meu site' em título principal e 'Esta é a minha primeira página' em parágrafo?",
        "options": [
            "<h1>Bem-vindo ao meu site</h1><p>Esta é a minha primeira página</p>",
            "<p>Bem-vindo ao meu site</p><h1>Esta é a minha primeira página</h1>",
            "Bem-vindo ao meu site<p>Esta é a minha primeira página</p>",
            "<title>Bem-vindo ao meu site</title><p>Esta é a minha primeira página</p>",
        ],
        "correct": "<h1>Bem-vindo ao meu site</h1><p>Esta é a minha primeira página</p>",
        "points": 5,
        "when_wrong": "<h1> marca o título principal e <p> marca o parágrafo.",
    },
    {
        "title": "Qual é a principal função do HTML em um site?",
        "options": [
            "Organizar e estruturar o conteúdo exibido na tela",
            "Executar cálculos e lógica de programação",
            "Aplicar cores, fontes e estilos visuais",
            "Criar animações e interatividade avançada",
        ],
        "correct": "Organizar e estruturar o conteúdo exibido na tela",
        "points": 5,
        "when_wrong": "O HTML é o esqueleto do site — organiza textos, imagens, links, vídeos e listas.",
    },
    {
        "title": "O HTML é considerado uma linguagem de programação?",
        "options": [
            "Não, ele apenas organiza e marca o conteúdo",
            "Sim, como JavaScript e Python",
            "Sim, mas apenas dentro do navegador",
            "Sim, quando usado com CSS",
        ],
        "correct": "Não, ele apenas organiza e marca o conteúdo",
        "points": 5,
        "when_wrong": "HTML não é linguagem de programação — não executa cálculos nem lógica.",
    },
    {
        "title": "O que significa 'marcação' no contexto do HTML?",
        "options": [
            "Colocar etiquetas no conteúdo para indicar o que cada parte é",
            "Decorar o site com cores e imagens",
            "Conectar o site à internet",
            "Compilar o código em um executável",
        ],
        "correct": "Colocar etiquetas no conteúdo para indicar o que cada parte é",
        "points": 5,
        "when_wrong": "Marcação é usar tags como <h1> e <p> para o navegador entender a estrutura.",
    },
    {
        "title": "Qual tag indica um título principal na página?",
        "options": ["<h1>", "<p>", "<a>", "<img>"],
        "correct": "<h1>",
        "points": 5,
        "when_wrong": "A tag <h1> representa o título mais importante da página.",
    },
    {
        "title": "Qual tag é usada para criar um parágrafo de texto?",
        "options": ["<p>", "<h1>", "<ul>", "<li>"],
        "correct": "<p>",
        "points": 5,
        "when_wrong": "A tag <p> é usada para blocos de texto em parágrafos.",
    },
    {
        "title": "Qual é a estrutura básica de um elemento HTML?",
        "options": [
            "Tag de abertura, conteúdo e tag de fechamento",
            "Apenas a tag de abertura",
            "Conteúdo, tag de abertura e tag de fechamento",
            "Tag de fechamento, conteúdo e tag de abertura",
        ],
        "correct": "Tag de abertura, conteúdo e tag de fechamento",
        "points": 5,
        "when_wrong": "Exemplo: <p>Meu texto</p> — abertura, conteúdo e fechamento.",
    },
    {
        "title": "Qual é a estrutura básica correta de um documento HTML5?",
        "options": [
            "<!DOCTYPE html><html><head></head><body></body></html>",
            "<html><body><head></head></html>",
            "<!DOCTYPE html><body><head></head><html></html>",
            "<head><body><!DOCTYPE html><html></html>",
        ],
        "correct": "<!DOCTYPE html><html><head></head><body></body></html>",
        "points": 5,
        "when_wrong": "A ordem é: <!DOCTYPE html>, <html>, <head> e <body>.",
    },
    {
        "title": "Em qual parte do HTML ficam informações técnicas invisíveis ao usuário?",
        "options": ["<head>", "<body>", "<h1>", "<p>"],
        "correct": "<head>",
        "points": 5,
        "when_wrong": "O <head> contém título, meta tags e links para CSS — não é visível na página.",
    },
    {
        "title": "Onde deve ser colocado todo o conteúdo visível para o usuário?",
        "options": ["<body>", "<head>", "<html>", "<!DOCTYPE html>"],
        "correct": "<body>",
        "points": 5,
        "when_wrong": "O <body> é a parte visível onde ficam títulos, parágrafos, imagens e formulários.",
    },
    {
        "title": "Na analogia do boneco articulado, o que representa o HTML?",
        "options": [
            "O esqueleto (estrutura)",
            "As roupas e aparência (estilo)",
            "O movimento (funcionalidade)",
            "A conexão com a internet",
        ],
        "correct": "O esqueleto (estrutura)",
        "points": 5,
        "when_wrong": "HTML = esqueleto, CSS = roupas/aparência, JavaScript = movimento.",
    },
    {
        "title": "Qual tag cria uma lista com itens numerados?",
        "options": ["<ol>", "<ul>", "<li>", "<a>"],
        "correct": "<ol>",
        "points": 5,
        "when_wrong": "<ol> é lista ordenada (numerada); <ul> é lista não ordenada (com marcadores).",
    },
    {
        "title": "Qual tag cria uma lista com marcadores (não numerada)?",
        "options": ["<ul>", "<ol>", "<p>", "<h2>"],
        "correct": "<ul>",
        "points": 5,
        "when_wrong": "<ul> cria listas não ordenadas com marcadores.",
    },
    {
        "title": "Qual tag deve envolver cada item dentro de uma lista <ul> ou <ol>?",
        "options": ["<li>", "<ul>", "<ol>", "<p>"],
        "correct": "<li>",
        "points": 5,
        "when_wrong": "Cada item da lista é marcado com a tag <li>.",
    },
    {
        "title": "Qual atributo da tag <a> define o endereço do link?",
        "options": ["href", "src", "alt", "target"],
        "correct": "href",
        "points": 5,
        "when_wrong": "O atributo href define o endereço do hiperlink.",
    },
    {
        "title": "Qual código monta corretamente um link para o Google que abre em nova aba?",
        "options": [
            '<a href="https://www.google.com" target="_blank">Visitar o Google</a>',
            '<a src="https://www.google.com" target="_blank">Visitar o Google</a>',
            '<a href="https://www.google.com">Visitar o Google</a>',
            '<link href="https://www.google.com" target="_blank">Visitar o Google</link>',
        ],
        "correct": '<a href="https://www.google.com" target="_blank">Visitar o Google</a>',
        "points": 5,
        "when_wrong": "Use <a> com href para o endereço e target=\"_blank\" para abrir em nova aba.",
    },
    {
        "title": "Qual atributo da tag <img> define o caminho da imagem?",
        "options": ["src", "alt", "width", "href"],
        "correct": "src",
        "points": 5,
        "when_wrong": "O atributo src define o caminho (source) da imagem.",
    },
    {
        "title": "Qual código monta corretamente uma imagem com caminho, descrição e largura?",
        "options": [
            '<img src="bolo.jpg" alt="Foto de um bolo de chocolate" width="300">',
            '<img href="bolo.jpg" alt="Foto de um bolo de chocolate" width="300">',
            '<img src="bolo.jpg" width="300">',
            '<image src="bolo.jpg" alt="Foto de um bolo de chocolate" width="300">',
        ],
        "correct": '<img src="bolo.jpg" alt="Foto de um bolo de chocolate" width="300">',
        "points": 5,
        "when_wrong": "Use <img> com src, alt e width para montar a imagem corretamente.",
    },
    {
        "title": "Qual tag de título é a mais importante na hierarquia?",
        "options": ["<h1>", "<h2>", "<h6>", "<p>"],
        "correct": "<h1>",
        "points": 5,
        "when_wrong": "<h1> é o título mais importante; <h2> a <h6> são níveis menores.",
    },
    {
        "title": "Qual código monta corretamente uma página com título de receita, subtítulo e seções de ingredientes e preparo?",
        "options": [
            "<h1>Receitas de Bolo</h1><h2>Bolo de Chocolate</h2><h3>Ingredientes</h3><h3>Modo de Preparo</h3>",
            "<h3>Receitas de Bolo</h3><h1>Bolo de Chocolate</h1><p>Ingredientes</p><p>Modo de Preparo</p>",
            "<title>Receitas de Bolo</title><h1>Bolo de Chocolate</h1><ul>Ingredientes</ul>",
            "<h1>Receitas de Bolo</h1><p>Bolo de Chocolate</p><h1>Ingredientes</h1>",
        ],
        "correct": "<h1>Receitas de Bolo</h1><h2>Bolo de Chocolate</h2><h3>Ingredientes</h3><h3>Modo de Preparo</h3>",
        "points": 5,
        "when_wrong": "Use <h1> para o título principal, <h2> para subtítulo e <h3> para seções.",
    },
]


def main():
    print("Criando o formulário...")
    form_service, form = create_quiz_form(
        "Quiz: HTML — Tags e Montagem de Código",
        "Quiz_HTML_Tags_Montagem",
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
