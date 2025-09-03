from gramaticaVisitor import FiboVisitor
from gramaticaParser import FiboParser

class EvalVisitor(FiboVisitor):

    def visitProg(self, ctx:FiboParser.ProgContext):

        return self.visit(ctx.fiboExpr())

    def visitFiboExpr(self, ctx:FiboParser.FiboExprContext):

        n = int(ctx.INT().getText())
        return self.fibonacci(n)

    def fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq
