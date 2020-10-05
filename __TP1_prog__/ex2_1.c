#include <stdio.h>

int main(){
  int n;

  printf("Entrer un nombre entier :\n");
  scanf("%d", &n);

  if(n == 42){
    printf("Gagné !!\n");
  }
  else{
    printf("perdu !!\n");
  }
}
