import functools
import timeit

from AFN import AFN
from ExpressionTree import ExpressionTree


def timemeasure(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        return result
    return new_func

@timemeasure
def thompson_algorithm(r: str):
    """Crea un AFN a parir del arbol de una expresion regular"""

    # Se genera el arbol
    expression_tree = ExpressionTree(r)
    expression_tree.generate_tree()

    afn = AFN()
    afn.generate_AFN_from_re(expression_tree)

    print(afn)
    afn.graph_AFN()

    return afn
