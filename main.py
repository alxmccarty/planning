"""
Quin Burrell
Alex McCarty
"""


def demand_vols(X, Y, Z):
    """determines the demand volumes on each source to destination pair"""
    result = []
    for src in range(1, X+1):
        for dest in range(1, Z+1):
            LHS = []
            for trans in range(1, Z+1):
                LHS += ['X{}{}{}'.format(src, trans, dest)]
            result += ['{} = {}'.format(' + '.join(LHS), str(src + dest))]
    return '\n'.join(result)


def STcapps(X, Y, Z):
    """determines the link capacity constraints from source to transit nodes"""
    result = []
    for src in range(1, X+1):
        for trans in range(1, Y+1):
            LHS = []
            for dest in range(1, Z+1):
                LHS += ['X{}{}{}'.format(src, trans, dest)]
            result += ['{} - (C{}{} * r) <= 0'.format(' + '.join(LHS), src, trans)]
    return '\n'.join(result)


def TDcapps(X, Y, Z):
    """determines the link capacity constraints from transit to destination nodes"""
    result = []
    for trans in range(1, Y + 1):
        for dest in range(1, Z + 1):
            LHS = []
            for src in range(1, X + 1):
                LHS += ['X{}{}{}'.format(src, trans, dest)]
            result += ['{} - (D{}{} * r) <= 0'.format(' + '.join(LHS), trans, dest)]
    return '\n'.join(result)


def capps(X, Y, Z):
    """returns a string of all capacity constraints"""
    return '{}\n{}'.format(STcapps(X, Y, Z), TDcapps(X, Y, Z))


def bounds(X, Y, Z):
    """determines the bounds"""
    result = ['r >= 0']
    for src in range(1, X+1):
        for trans in range(1, Y+1):
            result += ['C{}{} >= 0'.format(src, trans)]
            for dest in range(1, Z+1):
                result += ['X{}{}{} >= 0'.format(src, trans, dest)]
                if src == 1:
                    result += ['D{}{} >= 0'.format(trans, dest)]
    return '\n'.join(result)


def create_lp(X, Y, Z):
    filename = '{}{}{}.lp'.format(X, Y, Z)
    file = open(filename, 'w')
    content = '''Minimize \nr\nSubject to\nDemand Volumes:\n{}\nCapacity Constraints:\n{}\nBounds: \n{}\nEnd'''\
        .format(demand_vols(X, Y, Z), capps(X, Y, Z), bounds(X, Y, Z))

    file.write(content)
    file.close


def begin():
    X = int(input('The amount of source nodes: '))
    Y = int(input('The amount of transit nodes: '))
    Z = int(input('The amount of destination nodes: '))
    create_lp(X, Y, Z)


begin()
