#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <math.h>

int fibonacci(int n)
{
    int x;

    if (n == 1)
    {
        return (1);
    }

    if (n == 2)
    {
        return (1);
    }

    x = fibonacci(n - 1) + fibonacci(n - 2);
    return (x);
}

float bce(float n)
{
    // return (n * log(n) + (1 - n) * log(1 - n));
    return 1.0;
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

    for (i = 0; i < 100; i++)
    {
        sleep_ms(1);
        srand(clock());
        int random_value = rand() % 100;
        printf("Random value: %d\n", random_value);
        printf("Iteration: %d\n", i);
        // Introduce an unpredictable branch
        if (random_value % 2 == 0)
        {
            result += 1;
            int temporary = fibonacci((rand() % 10) + 1);
            printf("Fibonacci: %d\n", temporary);
        }
        else
        {
            result -= 1;
            float temporary = bce((float)((rand() % 12) + 1));
            printf("BCE: %f\n", temporary);
        }
    }

    printf("Result: %d\n", result);
    return 0;
}