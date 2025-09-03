from FiboVisitor import FiboVisitor
from FiboParser import FiboParser

class EvalVisitor(FiboVisitor):

    def visitProg(self, ctx:FiboParser.ProgContext):
        # El programa solo tiene una expresión FIBO
        return self.visit(ctx.fiboExpr())

    def visitFiboExpr(self, ctx:FiboParser.FiboExprContext):
        # Captura el número dentro de los paréntesis
        n = int(ctx.INT().getText())
        return self.fibonacci(n)

    def fibonacci(self, n):
        """Genera la secuencia Fibonacci hasta n términos (versión iterativa eficiente)."""
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
