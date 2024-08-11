#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_SIZE 1000 // Defina o tamanho do array para a análise

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Troca os elementos
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[ARRAY_SIZE];
    srand(time(0));

    // Preenche o array com valores aleatórios
    for (int i = 0; i < ARRAY_SIZE; i++) {
        arr[i] = rand() % 10000;
    }

    clock_t start = clock();
    
    bubbleSort(arr, ARRAY_SIZE);

    clock_t end = clock();
    
    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Bubble Sort took %f seconds to sort an array of size %d.\n", time_taken, ARRAY_SIZE);

    return 0;
}
