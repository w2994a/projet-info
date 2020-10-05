#include <stdio.h>

int main(){
  int i, n ,m , o = 0;
  double p;

  printf("Entrer un nombre ce valeurs à calculer : ");
  scanf("%d", &n);

  for(i = 1; i <= n; i += 1){
    printf("Entrer une valeurs : ");
    scanf("%d", &m);
    o += m;
  }
  printf("La somme est de : %d\n", o);
  p = o / n;
  printf("la moyenne est de : %lf\n", p);
}
