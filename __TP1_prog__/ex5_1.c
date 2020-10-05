#include <stdio.h>

int main(){
  int i, n, m = 0;

  printf("Entrer un nombre entier positif : ");
  scanf("%d", &n);

  for(i = 1; i <= n; i += 1){
    m = m + (i * i * i);
  }
  printf("La somme des cubes des %d entiers naturels positfs est de : %d\n", n, m);
}
