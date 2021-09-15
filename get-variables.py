import ast, keyword, builtins, csv

def is_keyword(name):
    return name in keyword.kwlist

def is_builtin(name):
    return name in builtins.__dict__

varslst = []
with open("training-data/test-input-finer.csv", 'r+') as csvfile:
    csv_reader = csv.reader(csvfile)
    with open("training-data/test-input-finer-mod.csv", 'w') as result:
        wtr = csv.writer(result)
        libs = ['re', 'datetime', 'Counter', 'itertools', 'time', 'cmpfun', 'itemgetter', 'OrderedDict', 'heapq', 'struct', 'ast', 'random', 'collections', 'base64']
        for row in csv_reader:
            nodelst = []
            code =  row[1]
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if (node.__class__.__name__ == "Name") and (not is_builtin(node.id)) and (not isinstance(node.ctx, ast.Store)) and (not is_keyword(node)):
                    nodelst.append(node.id)
            nodelst = [x for x in nodelst if x not in libs]
            varslst = list(set(nodelst))
            wtr.writerow((row[0], row[1], row[2], row[3], row[4], varslst))