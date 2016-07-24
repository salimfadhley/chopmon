FUNCTION_REGISTRY = {}

def register(fn, group_name="all"):
    FUNCTION_REGISTRY.setdefault(group_name, set()).add(fn)


def get_functions(group_name):
    return FUNCTION_REGISTRY.setdefault(group_name, set())