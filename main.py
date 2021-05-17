"""
Quin Burrell
Alex McCarty
"""

def demand_volume(X, Y, Z):



def source2trans_cap(X, Y, Z):



def trans2dest_cap(X, Y, Z):



def trans_nodes(X, Y, Z):



def binary_vars(X, Y, Z):



def demand_flow(X, Y, Z):



def bound_vars(X, Y, Z):



def binaries(X, Y, Z):



def create_lp(X, Y, Z, N):
    filename = '{}{}{}.lp'.format(X, Y, Z)
    file = open(filename, 'w')
    content = '''Minimize r
    Subject to
    Demand volume: \n{}
    Source to tranfer node capacity: \n{}
    Transit to destination node capacity: \n{}
    Transit nodes: \n{}
    Binary variables: \n{}
    Demand flow: \n{}
    Bounds: \n{}
    0 <= r
    Binaries: \n{}
    End'''.format(demand_volume(X, Y, Z), source2tras_cap(X, Y, Z),
    trans2dest_cap(X, Y, Z), trans_nodes(X, Y, Z), binary_vars(X, Y, Z),
    demand_flow(X, Y, Z), bound_vars(X, Y, Z), binaries(X, Y, Z))

    file.write(content)
    file.close



def begin():
    X = int(input('The amount of source nodes:'))
    Y = int(input('The amount of transit nodes:'))
    Z = int(input('The amount of destination nodes:'))
    N = 3
    create_lp(X, Y, Z, N)


begin()