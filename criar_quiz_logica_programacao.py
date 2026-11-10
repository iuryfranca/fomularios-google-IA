from forms_defaults import DRIVE_FOLDER_NAME, build_choice_question, create_quiz_form

QUIZ_QUESTIONS = [
    {
        "title": "Em termos simples, o que é lógica?",
        "options": [
            "A maneira como organizamos ideias para resolver um problema ou tomar uma decisão",
            "Um tipo de linguagem de programação",
            "Um programa que instala o computador",
            "Uma forma de desenhar sites",
        ],
        "correct": "A maneira como organizamos ideias para resolver um problema ou tomar uma decisão",
        "points": 5,
        "when_wrong": "Lógica é a maneira como organizamos ideias para resolver um problema ou tomar uma decisão.",
    },
    {
        "title": "No exemplo do guarda-chuva, o que é uma decisão lógica?",
        "options": [
            "Usar uma condição (está chovendo?) e tomar uma ação com base nela",
            "Levar o guarda-chuva todos os dias, chovendo ou não",
            "Pedir para o computador decidir sozinho",
            "Escrever um código em JavaScript",
        ],
        "correct": "Usar uma condição (está chovendo?) e tomar uma ação com base nela",
        "points": 5,
        "when_wrong": "Decisão lógica é usar uma condição e tomar uma ação com base nela, como levar o guarda-chuva se estiver chovendo.",
    },
    {
        "title": "O que é lógica de programação?",
        "options": [
            "O conjunto de regras e ideias usadas para criar instruções que o computador consiga entender",
            "Um aplicativo para celular",
            "O nome de uma linguagem de programação",
            "A parte visual de um site",
        ],
        "correct": "O conjunto de regras e ideias usadas para criar instruções que o computador consiga entender",
        "points": 5,
        "when_wrong": "Lógica de programação é o conjunto de regras e ideias para criar instruções que o computador entenda.",
    },
    {
        "title": "Por que os computadores precisam que tudo seja explicado passo a passo?",
        "options": [
            "Porque, diferente de nós, eles precisam de instruções claras, sem espaço para dúvidas",
            "Porque eles não ligam sozinhos",
            "Porque o JavaScript é difícil",
            "Porque o HTML não funciona sem isso",
        ],
        "correct": "Porque, diferente de nós, eles precisam de instruções claras, sem espaço para dúvidas",
        "points": 5,
        "when_wrong": "Os computadores precisam que tudo seja explicado de forma clara, passo a passo.",
    },
    {
        "title": "Por que precisamos aprender lógica antes de escrever código?",
        "options": [
            "Para organizar os passos da maneira certa e evitar erros",
            "Para instalar o JavaScript no computador",
            "Para criar imagens mais bonitas",
            "Para aprender inglês",
        ],
        "correct": "Para organizar os passos da maneira certa e evitar erros",
        "points": 5,
        "when_wrong": "A lógica ajuda a organizar os passos, planejar o código e evitar erros comuns.",
    },
    {
        "title": "No exemplo de preparar um lanche, o que acontece se os passos forem feitos fora de ordem?",
        "options": [
            "Pode dar errado, como acontece na programação",
            "O computador corrige sozinho",
            "Nada acontece",
            "O lanche fica pronto mais rápido",
        ],
        "correct": "Pode dar errado, como acontece na programação",
        "points": 5,
        "when_wrong": "Se os passos forem feitos fora de ordem, pode dar errado. O mesmo acontece na programação.",
    },
    {
        "title": "O que é pseudocódigo?",
        "options": [
            "Uma maneira de escrever os passos de um programa usando palavras comuns",
            "Uma linguagem usada só no Google",
            "Um tipo de erro no código",
            "Um aplicativo de celular",
        ],
        "correct": "Uma maneira de escrever os passos de um programa usando palavras comuns",
        "points": 5,
        "when_wrong": "Pseudocódigo é escrever os passos de um programa com palavras comuns, para planejar antes de codificar.",
    },
    {
        "title": "Qual é o pseudocódigo correto do exemplo da luz?",
        "options": [
            'Se a luz estiver acesa, mostrar "Luz acesa". Senão, mostrar "Luz apagada".',
            'Mostrar "Luz acesa" sempre',
            "Ligar a luz e depois desligar",
            "Escrever JavaScript para a lâmpada",
        ],
        "correct": 'Se a luz estiver acesa, mostrar "Luz acesa". Senão, mostrar "Luz apagada".',
        "points": 5,
        "when_wrong": 'O exemplo da apostila é: se a luz estiver acesa, mostrar "Luz acesa"; senão, mostrar "Luz apagada".',
    },
    {
        "title": "O que é uma linguagem de programação?",
        "options": [
            "Um conjunto de regras, símbolos e comandos que o computador consegue entender e executar",
            "Um idioma como português, inglês ou espanhol",
            "Um programa de desenho",
            "Um site da internet",
        ],
        "correct": "Um conjunto de regras, símbolos e comandos que o computador consegue entender e executar",
        "points": 5,
        "when_wrong": "Linguagem de programação é um conjunto de regras, símbolos e comandos que o computador entende e executa.",
    },
    {
        "title": "Quem criou o JavaScript e em que ano?",
        "options": [
            "Brendan Eich, em 1995, na empresa Netscape",
            "Bill Gates, em 1991, na Microsoft",
            "Steve Jobs, em 1972, na Apple",
            "Guido van Rossum, em 1991",
        ],
        "correct": "Brendan Eich, em 1995, na empresa Netscape",
        "points": 5,
        "when_wrong": "O JavaScript foi criado por Brendan Eich em 1995, enquanto trabalhava na Netscape.",
    },
    {
        "title": "Como eram as páginas da internet antes do JavaScript?",
        "options": [
            "Estáticas, com apenas texto e imagens",
            "Com jogos e animações",
            "Com menus interativos",
            "Com formulários que validavam sozinhos",
        ],
        "correct": "Estáticas, com apenas texto e imagens",
        "points": 5,
        "when_wrong": "Antes do JavaScript, as páginas eram estáticas, ou seja, apenas texto e imagens.",
    },
    {
        "title": "Com o JavaScript, o que passou a ser possível nas páginas da web?",
        "options": [
            "Exibir mensagens, criar menus, validar formulários e fazer animações",
            "Apenas escrever textos",
            "Apenas criar imagens",
            "Instalar o Windows",
        ],
        "correct": "Exibir mensagens, criar menus, validar formulários e fazer animações",
        "points": 5,
        "when_wrong": "Com o JavaScript ficou possível exibir mensagens, criar menus, validar formulários, animações e atualizar conteúdos.",
    },
    {
        "title": "Por que o JavaScript é importante, segundo a apostila?",
        "options": [
            "É universal, não precisa de instalação e é usado do início ao fim do site",
            "Só funciona no Google Chrome",
            "Precisa ser instalado no computador",
            "Serve apenas para jogos",
        ],
        "correct": "É universal, não precisa de instalação e é usado do início ao fim do site",
        "points": 5,
        "when_wrong": "O JavaScript funciona nos navegadores, não precisa de instalação e é usado do início ao fim do site.",
    },
    {
        "title": "Por que estamos aprendendo JavaScript nesta apostila?",
        "options": [
            "Porque é a linguagem da Web, fácil de começar e muito poderosa",
            "Porque é a única linguagem que existe",
            "Porque substitui o português",
            "Porque não precisa de lógica",
        ],
        "correct": "Porque é a linguagem da Web, fácil de começar e muito poderosa",
        "points": 5,
        "when_wrong": "Aprendemos JavaScript porque é a linguagem da Web, fácil de começar e muito poderosa.",
    },
    {
        "title": "Qual linguagem a apostila cita como simples e poderosa, criada em 1991?",
        "options": ["Python", "Java", "C", "SQL"],
        "correct": "Python",
        "points": 5,
        "when_wrong": "Python (1991) é conhecida por ser simples e poderosa.",
    },
    {
        "title": "Qual plataforma online a apostila indica para praticar pseudocódigo?",
        "options": [
            "Portugol Webstudio",
            "Google Chrome",
            "Microsoft Word",
            "Photoshop",
        ],
        "correct": "Portugol Webstudio",
        "points": 5,
        "when_wrong": "A apostila indica o Portugol Webstudio (https://portugol.dev/) para praticar algoritmos.",
    },
    {
        "title": "Qual é a estrutura básica de um pseudocódigo?",
        "options": [
            "início, declarar variáveis, ler dados, processar dados, mostrar resultado, fim",
            "HTML, CSS e JavaScript",
            "abrir, fechar e salvar",
            "título, parágrafo e imagem",
        ],
        "correct": "início, declarar variáveis, ler dados, processar dados, mostrar resultado, fim",
        "points": 5,
        "when_wrong": "Em geral o pseudocódigo começa em início, declara variáveis, lê e processa dados, mostra o resultado e termina em fim.",
    },
    {
        "title": "No Portugol, qual comando mostra uma mensagem na tela?",
        "options": ["escreva", "leia", "se", "para"],
        "correct": "escreva",
        "points": 5,
        "when_wrong": "O comando escreva mostra uma mensagem na tela, como em escreva(\"Bom dia, aluno!\").",
    },
    {
        "title": "No Portugol, qual comando lê um dado digitado pelo usuário?",
        "options": ["leia", "escreva", "senao", "limpa"],
        "correct": "leia",
        "points": 5,
        "when_wrong": "O comando leia recebe o que a pessoa digitou, como em leia(nome) ou leia(idade).",
    },
    {
        "title": "No exemplo da idade, o que o se / senao faz?",
        "options": [
            "Toma uma decisão: se a idade for menor que 18, mostra uma mensagem; senão, mostra outra",
            "Repete a tabuada várias vezes",
            "Lê o nome da pessoa",
            "Apaga a tela",
        ],
        "correct": "Toma uma decisão: se a idade for menor que 18, mostra uma mensagem; senão, mostra outra",
        "points": 5,
        "when_wrong": "se / senao é uma decisão: compara a idade e mostra a mensagem correspondente.",
    },
    {
        "title": "No exemplo da tabuada, qual estrutura é usada para repetir os cálculos?",
        "options": [
            "para (laço de repetição)",
            "se / senao",
            "escreva",
            "cadeia",
        ],
        "correct": "para (laço de repetição)",
        "points": 5,
        "when_wrong": "O comando para é um laço de repetição, usado para repetir os cálculos da tabuada.",
    },
]


def main():
    print("Criando o formulário...")
    form_service, form = create_quiz_form(
        "Quiz: Lógica de Programação e Linguagens",
        "Quiz_Logica_Programacao_Linguagens",
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
