
openingGroup = '('
closingGroup = ')'

openingIteration = '{'
closingIteration = '}'

openingOption = '['
closingOption = ']'

# |
alternative = '|'
# •
dot = '•'
# ?
question = '[]'
# *
star = '{}'

epsilon = 'ε'
hash = '#'


# Para incluir a los caracteres ( ) { } [ ]
def replace_reserved_words(r: str):
    return (r
            .replace('(', 'β')
            .replace(')', 'δ')
            .replace('{', 'ζ')
            .replace('}', 'η')
            .replace('[', 'θ')
            .replace(']', 'ω')
            .replace('|', 'φ')
            )


symbols = [replace_reserved_words(chr(i)) for i in range(1, 255)]
