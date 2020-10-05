#include <stdio.h>

int main(){
  int n;

  printf("Entrer un entier :\n");
  scanf("%d", &n);

  if(n == 1){
    printf("Un\n");
  }
  else if(n == 2){
    printf("Deux\n");
  }
  else{
    printf("Autre\n");
  }
}
