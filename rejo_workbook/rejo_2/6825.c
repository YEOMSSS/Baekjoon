
#include <stdio.h>

int main(void)
{
    float weight, height;
    scanf("%f %f", &weight, &height);

    float result = weight / (height * height);
    if (result > 25)
    {
        puts("Overweight");
    }
    else if (result < 18.5)
    {
        puts("Underweight");
    }
    else // 18.5<=result<=25
    {
        puts("Normal weight");
    }

    return 0;
}