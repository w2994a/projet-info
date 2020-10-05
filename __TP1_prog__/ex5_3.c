#include <stdio.h>

int main(){
  int i, n, m = 1;

  printf("Entrer un nombre entier positif : ");
  scanf("%d", &n);

  for(i = 1; i <= n; i += 1){
    m = i * m;
    printf("%d! = %d\n", i, m);
  }

  printf("le factorielle de %d est de : %d\n", n, m);
}
