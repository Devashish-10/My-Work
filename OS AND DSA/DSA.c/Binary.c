#include<stdio.h>
#include<stdlib.h>
int c=0,beg,end,mid,temp;
void sort(int a[10],int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i;j++){
            if(a[j]>a[j+1]){
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;

            }
        }
    }
    printf("ELEMENTS AFTER SORTING:");
    for(int i=0;i<n;i++){
        printf("%d ",a[i]);
    }
}
void binary(int a[10],int n){
    int x;
    printf("\nENTER THE ELEMENT TO BE FOUND:");
    scanf("%d",&x);
    beg=0;
    end=n-1;
    for(int i=beg;i<end;i++){
    mid=(end+beg)/2;
    if(a[mid]>x){
        end=mid;
    }
    else if(a[mid]<x){
        beg=mid;
    }
    else{
        c+=1;
        break;
       }
}
    if(c==0){
         printf("ELEMENT DOES NOT EXIST ");
        }
    else{
         printf("ELEMENT FOUND AT :%d",mid+1);
        }

}
void main(){
    int n,a[10],x;
    printf("ENTER NO OF ELEMENTS IN ARRAY:");
    scanf("%d",&n);
    printf("ENTER AN ARRAY IN ASCENDING ORDER:");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
  
    sort(a,n);
    binary(a,n);
}
    
