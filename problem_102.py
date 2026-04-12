FILENAME = 'problem_102.txt'

import math

def point_point_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def point_edge_distance(x, y, a, b, c, signed=False):
    if not signed:
        return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)
    return (a*x + b*y + c) / math.sqrt(a**2 + b**2)

def line_coefficients_given_points(x0, y0, x1, y1):
    if x1 == x0:
        return 1, 0, -x0
    
    m = (y1 - y0) / (x1 - x0)
    q = y0 - m*x0
    return -m, 1, -q

def vertex_edge_distance(vertex, edge1, edge2, signed=False):
    return point_edge_distance(*vertex, *line_coefficients_given_points(*edge1, *edge2), signed)

def isOriginInside(triang, to_print = False):
    coord1, coord2, coord3 = triang
    dist123, dist213, dist312 = vertex_edge_distance(coord1, coord2, coord3, True), vertex_edge_distance(coord2, coord1, coord3, True), vertex_edge_distance(coord3, coord1, coord2, True)
    dist012, dist013, dist023 = vertex_edge_distance([0,0], coord1, coord2, True), vertex_edge_distance([0,0], coord1, coord3, True), vertex_edge_distance([0,0], coord2, coord3, True)
    
    if dist012 * dist312 <= 0 or dist013 * dist213 <= 0 or dist023 * dist123 <= 0:
        return False
    return True

def main():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split(',')
            for j in range(len(lines[i])):
                lines[i][j] = int(lines[i][j].strip())
            
        triangles = [[[line[0], line[1]], [line[2], line[3]], [line[4], line[5]]] for line in lines]
                    
        counter = 0
        for triangle in triangles:
            if isOriginInside(triangle):
                counter += 1

        print(counter)

if __name__ == '__main__':
    main()
