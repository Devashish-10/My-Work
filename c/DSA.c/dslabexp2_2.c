#include<stdio.h>
#include<stdlib.h>
struct subject{
 char name[20];
 int code;
};
int main(){
int n;
printf("ENTER NO OF SUBJECT:");
scanf("%d",&n);
struct subject *ptr;
ptr=(struct subject *)malloc(n*sizeof(struct subject));
for(int i=0;i<n;i++){
 printf("ENTER SUBJECT NAME AND SUBJECT CODE ");
 scanf("%s %d",(ptr+i)->name,&(ptr+i)->code);
}
//PRINTING INFORMATION
for(int i=0;i<n;i++){
 printf("SUBJECT NAME:%s\nSUBJECT CODE:%d\n",(ptr+i)->name, (ptr+i)->code);
}
}