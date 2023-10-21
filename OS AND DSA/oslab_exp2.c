//SJF
#include<stdio.h>
int main(){
    int bt[10],process[10], wt[10],tat[10],n,total=0,pos,temp;
    float avg_wt,avg_tat;
    printf("Enter no of processes:");
    scanf("%d",&n);
    printf("Enter Burst time:");
    for(int i=0;i<n;i++){
    printf("p%d:",i+1);
    scanf("%d",&bt[i]);
    process[i]=i+1;
    }
    for(int i=0;i<n;i++){
        
        for(int j=0;j<n-i-1;j++){
            if(bt[j]>bt[j+1]){
               temp=bt[j];
               bt[j]=bt[j+1];
               bt[j+1]=temp;
               temp=process[j];
               process[j]=temp;
                
            }
        }
        }
    wt[0]=0;
     for(int i=1;i<n;i++){
         wt[i]=0;
         for(int j=0;j<i;j++){
             wt[i]=wt[i]+bt[i];
             }
             total=total+wt[i];
     }
     avg_wt=(float)total/n;
     total=0;

printf("Process Burst time Waiting time Turn around time\n");
 for(int i=0;i<n;i++){
     tat[i]=bt[i]+wt[i];
     total+=tat[i];
     printf("p%d   %d   %d   %d\n",process[i],bt[i],wt[i],tat[i]);
     }
     avg_tat=(float)total/n;
     printf("Average waiting time: %f\n",avg_wt);
     printf("Average turn around time: %f\n",avg_tat);
}
     