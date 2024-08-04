#include <stdio.h>

int limit[] = {200, 100, 40, 20, 10, 4, 2, 1};

int cond(int argValue, int limitIndex) {
    return argValue <= limit[limitIndex];
}

int coinSum(int a, int b, int c, int d, int e, int f, int g, int h) {
    return a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200;
}

int main() {
    int a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;
    int sums = 0;

    while (1) {
        if (coinSum(a, b, c, d, e, f, g, h) == 200) {
            sums += 1;
        }
        a += 1;
        if (!cond(a, 0)) {
            b += 1;
            a = 0;
        }
        if (!cond(b, 1)) {
            c += 1;
            a = b = 0;
        }
        if (!cond(c, 2)) {
            d += 1;
            a = b = c = 0;
        }
        if (!cond(d, 3)) {
            e += 1;
            a = b = c = d = 0;
        }
        if (!cond(e, 4)) {
            f += 1;
            a = b = c = d = e = 0;
        }
        if (!cond(f, 5)) {
            g += 1;
            a = b = c = d = e = f = 0;
        }
        if (!cond(g, 6)) {
            h += 1;
            a = b = c = d = e = f = g = 0;
        }
        if (!cond(h, 7)) {
            break;
        }
    }

    printf("%d\n", sums);

    return 0;
}
