"""
LP File Generator.
This program takes three numbers from the user (X, Y, Z), that indicate the amount of source, transit, and destination
nodes in a hypothetical network. It then formulates an LP file to be fed to the CPLEX algorithm for solving. The LP
file generated is in standard form and assumes that the flow between any destination and source is split over exactly
N paths. N here is permanently set as 2.
Authors:
Quin Burrell
Alex McCarty
"""


def demand_vols(X, Y, Z):
    """Determines the demand volumes on each source to destination pair."""
    result = []
    for src in range(1, X+1):
        for dest in range(1, Z+1):
            LHS = []
            for trans in range(1, Z+1):
                LHS += ['X{}{}{} U{}{}{}'.format(src, trans, dest, src, trans, dest)]
            result += ['{} = {}'.format(' + '.join(LHS), str(src + dest))]
    return '\n'.join(result)


def STcapps(X, Y, Z):
    """Determines the link capacity constraints from source to transit nodes."""
    result = []
    for src in range(1, X+1):
        for trans in range(1, Y+1):
            LHS = []
            for dest in range(1, Z+1):
                LHS += ['X{}{}{}'.format(src, trans, dest)]
            result += ['{} - C{}{} r <= 0'.format(' + '.join(LHS), src, trans)]
    return '\n'.join(result)


def TDcapps(X, Y, Z):
    """Determines the link capacity constraints from transit to destination nodes."""
    result = []
    for trans in range(1, Y + 1):
        for dest in range(1, Z + 1):
            LHS = []
            for src in range(1, X + 1):
                LHS += ['X{}{}{}'.format(src, trans, dest)]
            result += ['{} - D{}{} r <= 0'.format(' + '.join(LHS), trans, dest)]
    return '\n'.join(result)


def capps(X, Y, Z):
    """Returns a string of all capacity constraints."""
    return '{}\n{}'.format(STcapps(X, Y, Z), TDcapps(X, Y, Z))


def bounds(X, Y, Z):
    """Determines the bounds of the non integer variables. For efficiency's sake these are not alphabetically ordered."""
    result = ['r >= 0']
    for src in range(1, X+1):
        for trans in range(1, Y+1):
            result += ['C{}{} >= 0'.format(src, trans)]
            for dest in range(1, Z+1):
                result += ['X{}{}{} >= 0'.format(src, trans, dest)]
                if src == 1:
                    result += ['D{}{} >= 0'.format(trans, dest)]
    return '\n'.join(result)


def binary_constraints(X, Y, Z, N):
    """Determines the binary constraints."""
    result = []
    for src in range(1, X + 1):
        for dest in range(1, Z + 1):
            path = []
            for trans in range(1, Y + 1):
                path += ['U{}{}{}'.format(src, trans, dest)]
            result += [' + '.join(path) + ' = {}'.format(N)]
    return '\n'.join(result)


def binary_vars(X, Y, Z):
    """Determines the binary variables."""
    result = []
    for src in range(1, X+1):
        for trans in range(1, Y+1):
            for dest in range(1, Z+1):
                result += ['U{}{}{} '.format(src, trans, dest)]
    return '\n'.join(result)


def create_lp(X, Y, Z, N):
    """creates the LP file. It is automatically given the name XYZ.lp and writes the string content to it."""
    filename = '{}{}{}.lp'.format(X, Y, Z)
    file = open(filename, 'w')
    content = 'Minimize \nr\nSubject to\n' \
              'Demand Volumes:\n{}\n' \
              'Capacity Constraints:\n{}\n' \
              'Bounds:\n{}\n' \
              'Binary Constraints:\n{}\n'\
              'Integer:\n{}\nEnd' \
    .format(demand_vols(X, Y, Z), capps(X, Y, Z), bounds(X, Y, Z), binary_constraints(X, Y, Z, N), binary_vars(X, Y, Z))

    file.write(content)
    file.close()


def begin():
    """Takes input from the user to determine the values of X, Y, Z."""
    X = int(input('The amount of source nodes: '))
    Y = int(input('The amount of transit nodes: '))
    Z = int(input('The amount of destination nodes: '))
    N = 2
    create_lp(X, Y, Z, N)


begin()
