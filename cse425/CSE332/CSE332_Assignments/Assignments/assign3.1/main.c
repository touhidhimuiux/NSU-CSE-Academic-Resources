#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int parameter(int x, int y, int z);
bool validity(int x, int y, int z);

void main(void)
{
    int a,b,c;
    scanf("%d %d %d", &a,&b,&c);
    bool valid = validity(a,b,c);
    if(valid)
        printf("%d", parameter(a,b,c));
    else
        printf("The input is invalid");
}
int parameter(int x,int y,int z)
{
    return x+y+z;
}
bool validity(int x,int y,int z)
{
    if(x+y>z && y+z>x && z+x>y)
        return true;

    else
        return false;
}
