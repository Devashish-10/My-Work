//FCFS
#include<stdio.h>
void waiting_time(int at[],int n ,int bt[],int wt[]){
    wt[0]=0;
    for (int i=1;i<n;i++){
     wt[i]=bt[i-1]+wt[i-1];
     }
     }
     void turn_around_time(int at[],int n ,int bt[],int wt[],int tat[]){
     for (int i=0;i<n;i++){
         tat[i]=bt[i]+wt[i];
     }
     }
    void avgtime(int at[],int n ,int bt[]){
    int wt[n],tat[n],t_wt=0,t_tat=0;
    waiting_time( at, n , bt, wt);
    turn_around_time(at,n ,bt,wt,tat);
    printf(" Process Arrival Time Burst time Waiting time Turn around time \n");
      for (int i=0;i<n;i++){
      t_wt=t_wt+wt[i];
      t_tat=t_tat+tat[i];
      printf("   %d",(i+1));
      printf("        %d",at[i]);
      printf("        %d ", bt[i]);
      printf("        %d ",wt[i]);
      printf("        %d\n",tat[i]);
     }
     int avg=(float)t_wt/(float)n;
     int t=(float)t_tat/(float)n;
     printf("Average waiting time =%d",avg);
     printf("\n");
     printf("Average turn around time=%d",t);
     }
     void main(){
         int at[]={1,5,7,9,11};
         int n=sizeof at/sizeof at[0];
         int bt[]={10,5,8,9,6};
         avgtime(at,n ,bt);
          }
