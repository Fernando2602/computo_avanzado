import numpy as np

def main():
    # SAMPLE DIMENTION INPUT
    # O = 3
    # P = 5

    # SAMPLE ARRAY
    # array = [[3,1,9,0,5,8,2,1,4,0],
    #         [4,4,4,1,7,6,6,0,1,4],
    #         [1,8,1,7,1,5,4,5,9,8],
    #         [9,9,8,8,4,8,7,5,1,9],
    #         [9,5,1,8,4,0,6,1,0,1],
    #         [4,2,3,7,3,1,4,9,5,9],
    #         [6,8,8,7,3,0,3,3,9,2],
    #         [5,6,5,5,8,4,4,0,0,2],
    #         [4,7,6,6,9,2,0,2,5,1],
    #         [2,5,6,0,6,8,0,5,2,0],]

    M = int(input('Introduce las filas de la matriz zona petrolera: '))
    N = int(input('Introduce las columnas de la matriz zona petrolera: '))
    O = int(input('Introduce las filas de la matriz de la plataforma: '))
    P = int(input('Introduce las columnas de la matriz de la plataforma: '))
    print('')

    array = []
    for m in range(M):
        row = []
        for n in range(N):
            row.append(int(input(f'Introduce el elemento {m}x{n} de la matriz petrolera: ')))
        array.append(row)
    np_array = np.array(array)

    sum = 0
    higer = 0
    coords = []
    order = None

    P, O = (P, O) if O > P else (O, P)
    for t in range(2 if O != P else 1):
        v_size, h_size = (P, O) if t else (O, P)

        for y in range(np_array.shape[0]-v_size+1):
            for x in range(np_array.shape[1]-h_size+1):
                for i in range(v_size):
                    for e in range(h_size):
                        sum += np_array[i+y][e+x]
                if sum > higer:
                    higer = sum
                    coords = [y,x]
                    if O == P:
                        order = 'I'
                    else:
                        order = ('H') if t else ('V')
                sum = 0
        # print(t)

    print(f'({coords[0]}, {coords[1]})')
    print(higer)
    print(order)

if __name__ == "__main__":
    main()