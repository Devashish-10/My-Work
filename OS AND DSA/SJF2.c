#include<stdio.h>
void main(){
    int at[10],n,bt[10],tat[10],wt[10],process[10],pos,temp;
    printf("ENTER NO OF PROCESSES:");
    scanf("%d",&n);
        for(int i=0;i<=n;i++){
        printf("ENTER ARRIVAL TIME OF PROCESS ",i+1," :");
        scanf("%d",&at[i]);
        process[i]=i+1; 
        }
        for(int i=0;i<=n;i++){
            printf("ENTER BURST TIME OF PROCESS ",i+1," :");
            scanf("%d",&bt[i]);
        }
         for(int i=0;i<n;i++){
        pos=i;
        for(int j=0;j<n;j++){
            if(bt[i]<bt[pos]){
                pos=j;
            }
        }
        temp=bt[i];
        bt[i]=bt[pos];
        bt[pos]=temp;
        temp=process[i];
        process[i]=temp;
    }



}