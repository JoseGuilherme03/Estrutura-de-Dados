#include <stdio.h>
#include <stdio.h>

void soma_e_subtracao(int a, int b, int *soma, int *subtracao) {
    *soma = a + b;
    *subtracao = a - b;
}


int main() {
    int soma;
    int subtracao;
    int a = 20;
    int b = 10;

    soma_e_subtracao(a, b, &soma, &subtracao);

    printf("soma(%d + %d) = %d, subtracao(%d - %d) = %d\n", a, b, soma, a, b, subtracao);

    return 0;
}


