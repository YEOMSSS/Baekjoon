#include <stdio.h>

int main(void)
{
    int sh, sm, ss, eh, em, es;
    scanf("%d:%d:%d", &sh, &sm, &ss);
    scanf("%d:%d:%d", &eh, &em, &es);

    int rh, rm, rs;
    rs = es + 60 - ss;
    rm = em + 60 - sm;
    rh = eh + 24 - sh;

    if (rs >= 60)
        rs -= 60;
    else
        rm--;

    if (rm >= 60)
        rm -= 60;
    else
        rh--;

    if (rh >= 24)
        rh -= 24;

    if (rh == rm && rm == rs && rs == 0)
        rh = 24;

    printf("%02d:%02d:%02d", rh, rm, rs);
}