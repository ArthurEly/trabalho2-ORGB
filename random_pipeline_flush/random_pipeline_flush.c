#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <math.h>

float calcule(float n)
{
    float result = 0;
    for (int i = 0; i < 5; i++)
    {
        result += i * n;
    }
    return result / n;
}

void sleep_ms(int ms)
{
    struct timespec ts;
    ts.tv_sec = 0;
    ts.tv_nsec = ms * 1000000;
    nanosleep(&ts, NULL);
}

int main()
{
    srand(time(NULL)); // Seed the random number generator

    int i;
    volatile int result = 0; // Volatile to prevent optimization

    for (i = 0; i < 1000; i++)
    {
        sleep_ms(1);
        srand(42);
        int random_value = rand() % 100;
        
        // Introduce more unpredictable branches
        if (random_value < 25)
        {
            result += 1;
            float temporary = calcule((rand() % 5) + 1);
        }
        else if (random_value < 50)
        {
            result -= 1;
            float temporary = calcule((float)((rand() % 5) + 1));
        }
        else if (random_value < 75)
        {
            result *= 2;
            float temporary = calcule((float)((rand() % 5) + 1));
        }
        else
        {
            result /= 2;
            float temporary = calcule((float)((rand() % 5) + 1));
        }
    }

    printf("Result: %d\n", result);
    return 0;
}
