#include<stdio.h>
#include<stdlib.h>
int top=-1;int num=8,stack[8]; 
void reversal(int a[],int s){
    for(int i=0;i<s;i++){
        stack[i]=a[i];
        top++;
    }
    for(int i=top;i>=0;i--){
        printf("%d \n",stack[i]);
    }
}
void main(){
    int s,a[100];
    printf("ENTER THE SIZE OF THE STACK:");
    scanf("%d",&s);
    printf("ENTER ELEMENTS TO STACK:");
    for(int i=0;i<s;i++){
        scanf("%d",&a[i]);
    }
    printf("REVERSE IS:\n");
    reversal(a,s);
}