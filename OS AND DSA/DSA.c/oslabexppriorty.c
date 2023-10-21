#include<stdio.h>
void main(){
    int priorty[10],bt[10],n,wt[10],tat[10],process[10],temp,pos;
    float awt,atat;
    printf("ENTER NUMBER OF PROCESSES:");
    scanf("%d",&n);
    printf("ENTER BURST TIME OF PROCESSES:");
    for(int i=0;i<n;i++){
    scanf("%d",&bt[i]);
    process[i]=i+1;
    }
    printf("ENTER PRIORTY OF PROCESSES:");
    for(int i=0;i<n;i++){
    scanf("%d",&priorty[i]);
    }
    for(int i=0;i<n;i++){
        pos=i;
        for(int j=i+1;j<n;j++){
           
            if(priorty[j]<priorty[pos]){
              pos=j;
              }
        }
        temp=priorty[i];
        priorty[i]=priorty[pos];
        priorty[pos]=temp;
        temp=bt[i];
        bt[i]=bt[pos];
        bt[pos]=temp;
    }
    wt[0]=0;
    printf("Process\tBurst Time\tPriority\tWaiting Time\t Turn Around Time\n");
    for(int i=0;i<n;i++){
        wt[i]=0;
        tat[i]=0;
        for(int j=0;j<i;j++){
            wt[i]=wt[i]+bt[j];
            }
            tat[i]=wt[i]+bt[i];
            awt+=wt[i];
            atat+=wt[i];
            printf("%d\t%d\t\t%d\t\t%d\t\t%d\n",i+1,bt[i],priorty[i],wt[i],tat[i]);
    }
    awt=awt/n;
    atat=atat/n;
    printf("Average Waiting time%f\n:",awt);
    printf("Average Turn Around Time%f\n:",atat);}




    




            