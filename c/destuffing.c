#include<stdio.h>
void destuffing(int n,int a[]){
    int b[20];
    int i=0,j=0,k;
    int c=1;
    while(i<n){
        if(a[i]==1){
            b[j]=a[i];
            for(k=i+1;a[k]==1 && k<n && c<5;k++,c++){
                j++;
                b[j]=a[k];
            }
            c=1;
            i=k;
            }
        
        else{
            b[j]=a[i];
            i++;
        }
        j++;
    }
    for(i<0;i<j;i++){
        printf("%d",b[i]);
    }
}
void main(){
    int n=5;
    int a[]={1,0,1,0,1};
    destuffing(n,a);
}