class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token


def get_tokens(filename: str):
    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            tokens.append(words[3][:-1])


tokens = list()
get_tokens("test1.txt_output_no_whitespace.txt")
