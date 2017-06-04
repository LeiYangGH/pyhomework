import math
def read_input():
    #sample input:2 3 4 5 6 4 7 8 9
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = map(float,input("please input a1 a2 a3 b1 b2 b3 c1 c2 c3:\n").split())
    return (a1,a2,a3,b1,b2,b3,c1,c2,c3)

def vector_magnitude(g1,g2,g3):
    return math.sqrt(g1 * g1 + g2 * g2 + g3 * g3)

def cross_product(g1,g2,g3,h1,h2,h3):
    k1 = g2 * h3 - g3 * h2
    k2 = -(g1 * h3 - g3 * h1)
    k3 = (g1 * h2 - g2 * h1)
    return (k1,k2,k3)

def dot_product(g1,g2,g3,h1,h2,h3):
    return g1 * h1 + g2 * h2 + g3 * h3

def area_parallelogram(g1,g2,g3,h1,h2,h3):
    k1,k2,k3 = cross_product(g1,g2,g3,h1,h2,h3)#?
    return vector_magnitude(k1,k2,k3)

def volumn_parallelepiped(g1,g2,g3,h1,h2,h3,k1,k2,k3):
    k1,k2,k3 = cross_product(h1,h2,h3,k1,k2,k3)#?
    dot = dot_product(g1,g2,g3,k1,k2,k3)
    return abs(dot)

def print_output(a1,a2,a3,b1,b2,b3,c1,c2,c3,area,volumn):
    print('vector a=({0},{1},{2})'.format(a1,a2,a3))
    print('vector b=({0},{1},{2})'.format(b1,b2,b3))
    print('vector c=({0},{1},{2})'.format(c1,c2,c3))
    print('area = {0}'.format(c1,c2,c3))
    print('volumn = {0}'.format(c1,c2,c3))

if __name__ == "__main__":
    print('---Start---')
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = read_input()
    area = area_parallelogram(a1,a2,a3,b1,b2,b3)
    volumn = volumn_parallelepiped(a1,a2,a3,b1,b2,b3,c1,c2,c3)
    print_output(a1,a2,a3,b1,b2,b3,c1,c2,c3,area,volumn)
    print('---End---')
