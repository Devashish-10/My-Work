#include<stdio.h>
int main()
{
	int n,a[10],b[10],ct[10],w[10],tat[10];
	int count=0,temp[10],check[10],i,j,t=0;
	int min=0,pos=0;
	printf("Enter no of processes-:");
	scanf("%d",&n);
	for(j=0;j<n;j++)
	{
		printf("Enter AT of process %d -:",j+1);
		scanf("%d",&a[j]);
		printf("Enter BT of process %d -:",j+1);
		scanf("%d",&b[j]);
	}
	for(j=0;j<n;j++){temp[j]=b[j];check[j]=0;} 
	while(count!=n)
	{
		count=0;
		for(j=0;j<n;j++) if(temp[j]!=0 && a[j]<=t){min=temp[j];pos=j;break;}
		if(j==n) {t++;continue;}
		for(j=0;j<n;j++)
		{
			if(temp[j]<min && a[j]<=t && temp[j]!=0)
			{
				min=temp[j]; pos=j;
			}
		}
		//if(c==n){t++; continue;}
		temp[pos]--;
		t++;
		printf("\nPos- %d | Temp- %d",pos,temp[pos]);
		if(check[pos]==0 && temp[pos]==0)
		{
			check[pos]=1;
			ct[pos]=t;
		}
		for (j=0;j<n;j++) if (temp[j]==0) count++;
	}
	for (j=0;j<n;j++)
	{
		tat[j]=ct[j]-a[j];
		w[j]=tat[j]-b[j];
	}
	printf("\n Pro.  |  AT   |   BT  |   CT   |  TAT  |    WT  \n");
	for(j=0;j<n;j++)
	{
		printf("%6d | %5d | %5d |%7d |%6d |%6d\n",j+1,a[j],b[j],ct[j],tat[j],w[j]);
	}
	return 0;
}
