/*
@   @
@   @
@@@@@
@   @
@@@@@
*/

#include <stdio.h>

void print_row(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("@");
    }
}
void print_space(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}
void print_line_124(int n)
{
    for (int i = 0; i < n; i++)
    {
        print_row(n);
        for (int j = 0; j < 3; j++)
            print_space(n);
        print_row(n);

        printf("\n");
    }
}
void print_line_35(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 5; j++)
            print_row(n);

        printf("\n");
    }
}

int main()
{
    int n;
    scanf("%d", &n);

    print_line_124(n);
    print_line_124(n);
    print_line_35(n);
    print_line_124(n);
    print_line_35(n);

    return 0;
}