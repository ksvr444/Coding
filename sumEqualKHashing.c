#include<stdio.h>
#include<malloc.h>
int main()
{
  int b[10000000] = {0};
  int n, temp, sum, c = 0, i;
  printf("enter the length of array\n");
  scanf("%d", &n);
  int *a = (int*)malloc(n * sizeof(int));
  for(i = 0; i < n; i++)
  {
    scanf("%d", &a[i]);
  }
  printf("enter the sum\n");
  scanf("%d", &sum);
  for(i = 0; i < n; i++)
  {
    temp = sum - a[i];
    if(b[temp] == 1)
    {
      c++;
    }
    b[a[i]] = 1;
  }
  printf("the no of pairs are %d", c);
	return 0;
}
