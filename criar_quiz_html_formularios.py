from forms_defaults import DRIVE_FOLDER_NAME, build_choice_question, create_quiz_form

QUIZ_QUESTIONS = [
    {
        "title": "Qual tag HTML envolve todos os campos de um formulário?",
        "options": ["<form>", "<input>", "<fieldset>", "<section>"],
        "correct": "<form>",
        "points": 5,
        "when_wrong": "A tag <form> é o container principal de um formulário.",
    },
    {
        "title": "Qual código monta corretamente um formulário que envia dados para enviar.php via POST?",
        "options": [
            '<form action="enviar.php" method="post">',
            '<form src="enviar.php" method="get">',
            '<form href="enviar.php" type="post">',
            '<input action="enviar.php" method="post">',
        ],
        "correct": '<form action="enviar.php" method="post">',
        "points": 5,
        "when_wrong": "Use action para o destino e method=\"post\" para enviar os dados.",
    },
    {
        "title": "Qual atributo do <form> define para onde os dados serão enviados?",
        "options": ["action", "method", "name", "type"],
        "correct": "action",
        "points": 5,
        "when_wrong": "O atributo action indica o endereço que receberá os dados do formulário.",
    },
    {
        "title": "Qual tag é usada para descrever o que cada campo do formulário representa?",
        "options": ["<label>", "<span>", "<p>", "<title>"],
        "correct": "<label>",
        "points": 5,
        "when_wrong": "A tag <label> associa um texto descritivo ao campo do formulário.",
    },
    {
        "title": "Qual código cria um campo de nome obrigatório?",
        "options": [
            '<input type="text" name="nome" required>',
            '<input type="text" name="nome" optional>',
            '<text name="nome" required>',
            '<input type="nome" required>',
        ],
        "correct": '<input type="text" name="nome" required>',
        "points": 5,
        "when_wrong": "Use type=\"text\" com name e o atributo required para tornar o campo obrigatório.",
    },
    {
        "title": "Qual type de <input> é usado para e-mail e valida o formato automaticamente?",
        "options": ["email", "text", "url", "password"],
        "correct": "email",
        "points": 5,
        "when_wrong": "O type=\"email\" valida se o valor digitado tem formato de e-mail.",
    },
    {
        "title": "Qual type de <input> oculta os caracteres digitados, ideal para senhas?",
        "options": ["password", "text", "hidden", "secret"],
        "correct": "password",
        "points": 5,
        "when_wrong": "O type=\"password\" esconde os caracteres enquanto o usuário digita.",
    },
    {
        "title": "Qual type de <input> aceita apenas números?",
        "options": ["number", "text", "decimal", "numeric"],
        "correct": "number",
        "points": 5,
        "when_wrong": "O type=\"number\" restringe a entrada a valores numéricos.",
    },
    {
        "title": "Qual type de <input> exibe um seletor de data?",
        "options": ["date", "datetime", "calendar", "time"],
        "correct": "date",
        "points": 5,
        "when_wrong": "O type=\"date\" cria um campo com seletor de data.",
    },
    {
        "title": "Qual type de <input> permite selecionar apenas uma opção entre várias?",
        "options": ["radio", "checkbox", "select", "option"],
        "correct": "radio",
        "points": 5,
        "when_wrong": "Botões radio permitem seleção única entre opções com o mesmo name.",
    },
    {
        "title": "Qual type de <input> permite marcar várias opções ao mesmo tempo?",
        "options": ["checkbox", "radio", "select", "text"],
        "correct": "checkbox",
        "points": 5,
        "when_wrong": "Checkboxes permitem seleção múltipla, como em listas de interesses.",
    },
    {
        "title": "Qual type de <input> é usado para enviar arquivos?",
        "options": ["file", "upload", "image", "attach"],
        "correct": "file",
        "points": 5,
        "when_wrong": "O type=\"file\" permite que o usuário selecione um arquivo do computador.",
    },
    {
        "title": "Qual código monta corretamente um campo de gênero com opções Masculino e Feminino (seleção única)?",
        "options": [
            '<input type="radio" name="genero" value="masculino"> Masculino<br><input type="radio" name="genero" value="feminino"> Feminino',
            '<input type="checkbox" name="genero" value="masculino"> Masculino<br><input type="checkbox" name="genero" value="feminino"> Feminino',
            '<select type="radio" name="genero"><option>Masculino</option></select>',
            '<input type="text" name="genero" value="masculino"> Masculino',
        ],
        "correct": '<input type="radio" name="genero" value="masculino"> Masculino<br><input type="radio" name="genero" value="feminino"> Feminino',
        "points": 5,
        "when_wrong": "Use type=\"radio\" com o mesmo name e values diferentes para seleção única.",
    },
    {
        "title": "Qual código monta corretamente uma caixa de seleção com as opções HTML, CSS e JavaScript?",
        "options": [
            '<select name="linguagem"><option value="html">HTML</option><option value="css">CSS</option><option value="javascript">JavaScript</option></select>',
            '<input type="select" name="linguagem" value="HTML,CSS,JavaScript">',
            '<dropdown name="linguagem"><item>HTML</item></dropdown>',
            '<option name="linguagem"><select>HTML</select></option>',
        ],
        "correct": '<select name="linguagem"><option value="html">HTML</option><option value="css">CSS</option><option value="javascript">JavaScript</option></select>',
        "points": 5,
        "when_wrong": "Use <select> com <option> para criar listas suspensas.",
    },
    {
        "title": "Qual tag é usada para criar cada opção dentro de um <select>?",
        "options": ["<option>", "<item>", "<choice>", "<li>"],
        "correct": "<option>",
        "points": 5,
        "when_wrong": "Cada item da lista suspensa é definido com a tag <option>.",
    },
    {
        "title": "Qual tag é ideal para textos longos, como mensagens?",
        "options": ["<textarea>", "<input>", "<p>", "<text>"],
        "correct": "<textarea>",
        "points": 5,
        "when_wrong": "A tag <textarea> cria uma área de texto com várias linhas.",
    },
    {
        "title": "Qual código monta corretamente uma área de texto com 5 linhas e 40 colunas?",
        "options": [
            '<textarea name="mensagem" rows="5" cols="40"></textarea>',
            '<textarea name="mensagem" height="5" width="40"></textarea>',
            '<input type="textarea" rows="5" cols="40">',
            '<text name="mensagem" rows="5" cols="40"></text>',
        ],
        "correct": '<textarea name="mensagem" rows="5" cols="40"></textarea>',
        "points": 5,
        "when_wrong": "Use rows para altura e cols para largura na tag <textarea>.",
    },
    {
        "title": "Qual código cria o botão que envia o formulário?",
        "options": [
            '<input type="submit" value="Enviar">',
            '<button type="send">Enviar</button>',
            '<input type="button" value="Enviar">',
            '<submit>Enviar</submit>',
        ],
        "correct": '<input type="submit" value="Enviar">',
        "points": 5,
        "when_wrong": "O type=\"submit\" envia os dados do formulário ao ser clicado.",
    },
    {
        "title": "Qual type de <button> limpa todos os campos preenchidos no formulário?",
        "options": ["reset", "button", "clear", "submit"],
        "correct": "reset",
        "points": 5,
        "when_wrong": "O type=\"reset\" restaura os campos do formulário aos valores iniciais.",
    },
    {
        "title": "Qual código monta corretamente o formulário de contato com nome, e-mail, assunto e mensagem?",
        "options": [
            '<form action="enviar.php" method="post"><h2>Formulário de Contato</h2><label>Nome:</label><input type="text" name="nome" required><label>Email:</label><input type="email" name="email" required><label>Assunto:</label><select name="assunto"><option value="duvida">Dúvida</option><option value="sugestao">Sugestão</option><option value="outro">Outro</option></select><label>Mensagem:</label><textarea name="mensagem" rows="4" cols="50"></textarea><input type="submit" value="Enviar"></form>',
            '<form><input type="text"><input type="submit"></form>',
            '<div><h2>Formulário de Contato</h2><p>Nome</p><p>Email</p></div>',
            '<form action="enviar.php"><input type="text" name="nome"><button>Enviar</button>',
        ],
        "correct": '<form action="enviar.php" method="post"><h2>Formulário de Contato</h2><label>Nome:</label><input type="text" name="nome" required><label>Email:</label><input type="email" name="email" required><label>Assunto:</label><select name="assunto"><option value="duvida">Dúvida</option><option value="sugestao">Sugestão</option><option value="outro">Outro</option></select><label>Mensagem:</label><textarea name="mensagem" rows="4" cols="50"></textarea><input type="submit" value="Enviar"></form>',
        "points": 5,
        "when_wrong": "O formulário completo combina <form>, <label>, <input>, <select>, <textarea> e submit.",
    },
]


def main():
    print("Criando o formulário...")
    form_service, form = create_quiz_form(
        "Quiz: HTML — Formulários e Campos",
        "Quiz_HTML_Formularios",
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
