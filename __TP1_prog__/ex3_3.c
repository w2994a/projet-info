#include <stdio.h>

int main(){
  int i, n, m;

  printf("Entrer un nombre entier : ");
  scanf("%d", &n);

  for(i = 1; i <= n; i += 1){
    m = i * i;
    printf("%d ", m);
  }
}
