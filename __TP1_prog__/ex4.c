#include <stdio.h>

int main(){
  int i, n, m, f = 0;

  printf("Entrer un nombre entier de tentative : ");
  scanf("%d", &n);

  for(i = 1; i <= n; i += 1){
    printf("Entrer un nombre entier : ");
    scanf("%d", &m);
    if(m == 6){
      f = 1;
    }
  }
  if(f == 1){
    printf("Le nombre 6 se trouvait parmis ces %d entiers.\n", n);
  }
  else{
    printf("Le nombre 6 ne se trouvait pas parmis ces %d entiers.\n", n);
  }
}
