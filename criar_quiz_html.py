from forms_defaults import DRIVE_FOLDER_NAME, build_choice_question, create_quiz_form

QUIZ_QUESTIONS = [
    {
        "title": "O que significa a sigla HTML?",
        "options": [
            "HyperText Markup Language",
            "High Tech Modern Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language",
        ],
        "correct": "HyperText Markup Language",
        "points": 5,
        "when_wrong": "HTML significa HyperText Markup Language (Linguagem de Marcação de Hipertexto).",
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
        "title": "Para que serve a declaração <!DOCTYPE html>?",
        "options": [
            "Informar ao navegador que o documento segue o padrão HTML5",
            "Marcar o início do conteúdo visível da página",
            "Definir o título exibido na aba do navegador",
            "Importar folhas de estilo CSS",
        ],
        "correct": "Informar ao navegador que o documento segue o padrão HTML5",
        "points": 5,
        "when_wrong": "<!DOCTYPE html> indica que o documento segue o padrão HTML5.",
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
        "title": "Qual atributo da tag <a> define o endereço do link?",
        "options": ["href", "src", "alt", "target"],
        "correct": "href",
        "points": 5,
        "when_wrong": "O atributo href define o endereço do hiperlink.",
    },
    {
        "title": "O que o atributo target=\"_blank\" faz em um link?",
        "options": [
            "Abre o link em uma nova aba",
            "Abre o link na mesma aba",
            "Define o endereço do link",
            "Adiciona uma imagem ao link",
        ],
        "correct": "Abre o link em uma nova aba",
        "points": 5,
        "when_wrong": "target=\"_blank\" faz o link abrir em uma nova aba do navegador.",
    },
    {
        "title": "Qual atributo da tag <img> define o caminho da imagem?",
        "options": ["src", "alt", "width", "href"],
        "correct": "src",
        "points": 5,
        "when_wrong": "O atributo src define o caminho (source) da imagem.",
    },
    {
        "title": "Para que serve o atributo alt em uma tag <img>?",
        "options": [
            "Descrição da imagem para acessibilidade e SEO",
            "Definir a largura da imagem",
            "Definir o endereço do link da imagem",
            "Abrir a imagem em nova aba",
        ],
        "correct": "Descrição da imagem para acessibilidade e SEO",
        "points": 5,
        "when_wrong": "O alt fornece uma descrição textual importante para acessibilidade e SEO.",
    },
    {
        "title": "Qual tag de título é a mais importante na hierarquia?",
        "options": ["<h1>", "<h2>", "<h6>", "<p>"],
        "correct": "<h1>",
        "points": 5,
        "when_wrong": "<h1> é o título mais importante; <h2> a <h6> são níveis menores.",
    },
    {
        "title": "O HTML sozinho deixa o site funcional, mas não bonito. Qual tecnologia cuida da aparência?",
        "options": ["CSS", "JavaScript", "Python", "HTML5"],
        "correct": "CSS",
        "points": 5,
        "when_wrong": "O CSS é responsável pelos estilos visuais — cores, fontes e layout.",
    },
    {
        "title": "O que acontece quando o navegador abre uma página HTML?",
        "options": [
            "Ele lê o código HTML e monta a estrutura visual na tela",
            "Ele executa cálculos matemáticos do HTML",
            "Ele compila o HTML em JavaScript",
            "Ele ignora as tags e exibe apenas texto puro",
        ],
        "correct": "Ele lê o código HTML e monta a estrutura visual na tela",
        "points": 5,
        "when_wrong": "O navegador interpreta o HTML e renderiza a estrutura visual para o usuário.",
    },
]


def main():
    print("Criando o formulário...")
    form_service, form = create_quiz_form(
        "Quiz: HTML — Estrutura e Tags",
        "Quiz_HTML_UI_Design",
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
