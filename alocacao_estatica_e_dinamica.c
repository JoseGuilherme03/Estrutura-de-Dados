#include <stdio.h>
#include <stdlib.h>  //Contém NULL, calloc, malloc, free

int main() {
    puts("### VETOR ESTATICO ###");
    //alocacao de um vetor estático (memória stack)
    int vs[5] = {0, 10, 20, 30, 40};
    printf("&vs = %p, vs = %p\n", &vs, vs);

    for (int i=0; i < 5; i++) {
        printf("&vs[%d] = %p, vs[%d] = %d\n", i, &vs[i], i, vs[i]);
    }
    puts("\n");


    puts("### VETOR DINAMICO COM MALLOC ###");
    //alocacao de um vetor dinâmico usando malloc (memória Heap)
    int *vh_mal = (int *) malloc(5 * sizeof(int)); //todos elementos possuem lixo de memória.
    printf("&vh_mal = %p, vh_mal = %p\n", &vh_mal, vh_mal);

    for (int i=0; i < 5; i++) {
        printf("&vh_mal[%d] = %p, vh_mal[%d] = %d\n", i, &vh_mal[i], i, vh_mal[i]);
    }
    
    puts("\n");

    puts("### VETOR DINAMICO COM CALLOC ###");
    //alocacao de um vetor dinâmico usando calloc (memória Heap)
    int *vh_cal = (int *) calloc(5, sizeof(int)); //garante que todos elementos terão valor 0.
    printf("&vh_cal = %p, vh_cal = %p\n", &vh_cal, vh_cal);

    for (int i=0; i < 5; i++) {
        printf("&vh_cal[%d] = %p, vh_cal[%d] = %d\n", i, &vh_cal[i], i, vh_cal[i]);
    }


    return 0;

}

