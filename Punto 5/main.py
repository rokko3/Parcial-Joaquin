import sys
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from EvalVisitor import EvalVisitor

def main(argv):
    if len(argv) < 2:
        print("No se agrego un archivo")
        return

    input_stream = FileStream(argv[1])
    lexer = gramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    result = visitor.visit(tree)

    print("Resultado:", ", ".join(map(str, result)))

if __name__ == '__main__':
    main(sys.argv)
