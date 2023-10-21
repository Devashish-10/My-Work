#include<stdio.h>
void Bitstuffing(int n,int a[]){
    int b[30];
    int i=0,j=0,k;
    while(i<n){
        if(a[i]==1){
            int c=1;
            b[j]=a[i];
            for(k=i+1;a[k]==1&& k<n && c<5;k++){
                j++;
                b[j]=a[k];
                c++;
                if(c==5){
                    j++;
                    b[j]=0;
                }
                i=k;
            }

        }
        else{
            b[j]=a[i];
        }
        i++;
        j++;
    }
    for(i=0;i<j;i++){
        printf("%d",b[i]);
    }
}
void main(){
    int n=6;
    int a[]={1,1,1,1,1,1};
    Bitstuffing(n,a);
}