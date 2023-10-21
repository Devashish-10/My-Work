#include<stdio.h>
void b_search(int high,int low,int a[20],int x){
    int mid;
    mid=(high+low)/2;
    if(a[mid]>x){
        high=a[mid];
        b_search(high,low,a,x);
    }
    else if(a[mid]<x){
        low=a[mid];
        b_search(high,low,a,x);
    }
    else{
        printf("ELEMENT FOUND AT:",(mid+1));
    }
}
void main(){
    int n,a[n],x;
    printf("ENTER ARRAY SIZE:");
    scanf("%d",&n);
    printf("ENTER ARRAY ELEMENTS:");
    for(int i=0;i<n;i++){
    scanf("%d",&a[i]);
    }
    printf("ENTER ELEMENT TO BE SEARCHED:");
    scanf("%d",&x);
    int high;
    high=a[n-1];
    int low;
    low=a[0];
    b_search(high,low,a,x);
}