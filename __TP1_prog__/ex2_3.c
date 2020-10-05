#include <stdio.h>

int main(){
  int n;

  printf("Entrer un nombre entier :");
  scanf("%d", &n);

  if(n < 0){
    printf("négatif\n");
  }
  else if(n >= 0 && n <= 100){
    printf("entre 0 et 100\n");
  }
  else if(n > 100){
    printf("supérieur à 100\n");
  }
}
