#include<stdio.h>
void main(){
    int n,at[10],bt[10],wt[10],tat[10],temp[10],t1,t2;
    float avgwt=0;
    float avgtat=0;
    printf("ENTER THE NUMBER OF PROCESSES:");
    scanf("%d",&n);
    printf("ENTER ARRIVAL TIME OF PROCESSES:");
    for(int i=0;i<n;i++){
        scanf("%d",&at[i]);
        }
        printf("ENTER BURST TIME OF PROCESSES:");
        for(int i=0;i<n;i++){
        scanf("%d",&bt[i]);
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n-i+1;j++){
                if(at[j]>at[j+1])
                {
                    t1=at[j];
                    at[j]=at[j+1];
                    at[j+1]=t1;
                    t2=bt[j];
                    bt[j]=bt[j+1];
                    bt[j+1]=t2;
                }
            }
        temp[0]=0;
        printf("PROCESS ARRIVAL TIME BURST TIME WAITING TIME TURNAROUND TIME\n:");
         for(int i=0;i<n;i++){
             wt[i]=0;
             tat[i]=0;
             temp[i+1]=temp[i]+bt[i];
             wt[i]=temp[i]-at[i];
             tat[i]=wt[i]+bt[i];
             avgwt=avgwt+wt[i];
             avgtat=avgtat+tat[i];
             printf("%d %d %d %d %d\n",i+1,at[i],bt[i],wt[i],tat[i]);
    }
    avgwt=avgwt/n;
    avgtat=avgtat/n;
    printf("AVERAGE WAITING TIME IS %f:\n",avgwt);
    printf("AVERAGE TURN AROUND TME TIME IS %f:\n",avgtat);
}
}
