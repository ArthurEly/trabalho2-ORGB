#include <stdio.h>

int main(){

    int primos[2000];
    int ind = 0, div = 2, primo = 1;
    

    for (int i = 3; i < 10000; i++){
        
        while (primo && div != i){
            if (i % div == 0)
                primo = 0;
            div++;
        }

        if (primo){
            primos[ind] = i;
            ind++;
        }
        div = 2;
        primo = 1;
    }

    // for (int i = 0; i < ind; i++)
    //     printf("%d ", primos[i]);

    return 0;
}
