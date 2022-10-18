import importlib.util

def check_module(module_name):
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {} not found'.format(module_name))
    else:
        print('Module: {} can be found!'.format(module_name))
        return module_spec


def import_module_from_spec(module_spec):
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    module_spec = check_module('fake_module')
    module_spec = check_module('collections')
    print('module_spec:', module_spec)
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))