#include <stdio.h>

int main (){
  int n, i;

  printf("Entrer un nombre entier :");
  scanf("%d", &n);

  for(i = 0; i < n; i += 1){
    printf("*\n");
  }
}
