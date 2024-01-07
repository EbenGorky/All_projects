#returns only function name
def get_function_name():
    l = list()
    with open(r'functions_project.py','r') as fp:
        rld = fp.readlines()
        for i in rld:
            if i[0:3] in 'def':
                try:
                    l.append((i[4:i.index('__')],i[4:-2]))
                except ValueError:
                    l.append((i[4:i.index('(')],i[4:-2]))
    return l

def get_graph_function_name():
    with open('graph_function.py','r') as fp:
        l = list()
        for i in fp.readlines():
            if i[:3] in 'def':
                l.append((i[4:i.index('(')],i[4:-2]))
    return l


import functions_project as fp

def run_and_return_function_formula_var(fun):
    vl = []
    rou = '('
    c = 1
    vl = fun[fun.index('(')+1:fun.index(')')].split(',')
    #fun = fun.replace(fun[fun.index('('):],rou)
    for i in range(len(vl)):
        rou += str(i+1)+','
    rou = rou[:-1:]
    rou += ')'
    fun = fun.replace(fun[fun.index('('):fun.index(')')+1],rou)
    fv = eval('fp.'+fun)
    try:
        return(fv[2][fv[2].index(':')+1:],tuple(vl))
    except:
        return(fv[2],tuple(vl))

def add_for(fn,fo,v):
    with open('functions_project.py','a') as fp:
        try:
            fn = fn.replace(' ','_')
        except AttributeError:
            pass
        lhs,rhs = tuple(fo.split('='))
        v = v.replace(' ',',')
        fun = f"\ndef {fn}__{lhs}({v}):\n\treturn ('{lhs}=',{rhs},':{fo}')\n"
        fp.write(fun)