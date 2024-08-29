# https://www.renpy.org/doc/html/cds.html
python early:
    def parse_random(lexer):
        subblock_lexer = lexer.subblock_lexer()
        choices = []

        while subblock_lexer.advance():
            with subblock_lexer.catch_error():
                statement = subblock_lexer.renpy_statement()
                choices.append(statement)

        return choices

    def next_random(choices):
        return renpy.random.choice(choices)

    def lint_random(parsed_object):
        for i in parsed_object:
            check = renpy.check_text_tags(i.block[0].what)
            if check:
                renpy.error(check)

    renpy.register_statement(
        name="random",
        block=True,
        parse=parse_random,
        next=next_random,
        lint=lint_random,
    )
