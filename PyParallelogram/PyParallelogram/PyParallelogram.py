import math
a1,a2,a3,b1,b2,b3,c1,c2,c3 = 2,3,4,5,6,4,7,8,9
def read_input():
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = input("please input a1 a2 a3 b1 b2 b3 c1 c2 c3:\n").split() 

def vector_magnitude(g1,g2,g3):
    return math.sqrt(g1 * g1 + g2 * g2 + g3 * g3)

def cross_product(g1,g2,g3,h1,h2,h3):
    k1 = g2 * h3 - g3 * h2
    k2 = -(g1 * h3 - g3 * h1)
    k3 = (g1 * h2 - g2 * h1)
    return (k1,k2,k3)

def dot_product(g1,g2,g3,h1,h2,h3):
    return g1 * h1 + g2 * h2 + g3 * h3

def calc_vector_magnitude(a1,a2,a3):
    

def area_parallelogram(g1,g2,g3,h1,h2,h3):
    (k1,k2,k3) = cross_product(g1,g2,g3,h1,h2,h3)#?
    return vector_magnitude(k1,k2,k3)

def calc_volumn(a1,a2,a3,b1,b2,b3):

def print_output(a1,a2,a3,b1,b2,b3,c1,c2,c3,area,volumn):

if __name__ == "__main__":
    print('---Start---')
    #read_input()
    print(a1)
    print(c3)
    print('---End---')
