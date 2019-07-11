#include<stdio.h>
#include<malloc.h>
struct Node
{
  int data;
  struct Node *left;
  struct Node *right;
};

struct Node* create()
{
  int x;
  scanf("%d", &x);
  if(x == -1)
  {
    return NULL;
  }
  struct Node *nn = (struct Node*)malloc(sizeof(struct Node));

  nn -> data = x;
  nn -> left = create();
  nn -> right = create();
  return nn;
}

void mirror(struct Node *temp)
{
  if(temp)
  {
    mirror(temp -> left);
    mirror(temp -> right);
    struct Node *n = temp -> left;
    temp -> left = temp -> right;
    temp -> right = n;
  }
}

void inorder(struct Node *root)
{
  if(root)
  {
    inorder(root -> left);
    printf("%d ", root -> data);
    inorder(root -> right);
  }
}

int main()
{
  struct Node *temp;
  temp = create();
  inorder(temp);
  mirror(temp);
  printf("inoeder after mirroring : ");
  inorder(temp);
  return 1;
}
