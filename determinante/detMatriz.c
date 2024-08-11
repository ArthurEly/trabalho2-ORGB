#include <stdio.h>

int determinante(int matriz[3][3]){

    int

    det = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
          matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
          matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]);

    return det;
}

int main(){

    int matriz[3][3] = {
        {5, 2, 3},
        {4, 10, 6},
        {7, 8, 9}
    };
    int det;

    det = determinante(matriz);

    return 0;
}