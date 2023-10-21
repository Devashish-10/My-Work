#include<stdio.h>
#include<string.h>
union product{
 int quantity;
 char name[20];
 int price;
};
int main(){
 union product a;
 int n,p,q,amt=0;
 char arr[15];
 printf("ENTER NUMBER OF PRODUCTS :");
 scanf("%d",&n);
 for(int i=0;i<n;i++){
 printf("ENTER QUANTITY OF PURCHASED ITEM:");
 scanf("%d",&a.quantity);
 q=a.quantity;
 printf("ENTER PRODUCT NAME:");
 scanf("%s",&a.name);
 strcpy(arr,a.name);
 printf("ENTER PRICE OF PRODUCT:");
 scanf("%d",&a.price);
 p=a.price;
 printf("YOUR ORDER DETAILS ARE:");
 printf(" ITEM QUANTITY: %d\n ITEM NAME: %s\n ITEM PRICE: %d\n ",q,a,p);
 amt=amt+q*p;
 }
 printf("YOUR TOTAL BILL COSTS: %d",amt);
}

 
