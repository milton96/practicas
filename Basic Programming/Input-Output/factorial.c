#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    printf("%d", f(N));
    system("pause");
    return 0;
}

int f(x)
{
    if (x == 0)
    {
        return 1;
    }
    return x * f(x - 1);
}