#include<stdio.h>
void swap(int *p,int *q){
	int temp = *p;
	*p = *q;
	*q = temp;
}
int partition(int a[],int low,int high){
	int pivot = a[high],j;
	int i = low-1;
	for(j=low;j<=high;j++){
		if(a[j]<pivot){
			i++;
			swap(&a[i],&a[j]);
		}
	}
	swap(&a[i+1],&a[high]);
	return i+1;
}
void quickSort(int a[],int low,int high){
	if(low<high){
		int pi = partition(a,low,high);
		quickSort(a,low,pi-1);
		quickSort(a,pi+1,high);
	}
}
int main(){
	int i,n,a[10];
	printf("enter no of numbers\n");
	scanf("%d",&n);
	printf("enter the numbers\n");
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	quickSort(a,0,n-1);
	printf("numbers after sorting\n");
	for(i=0;i<n;i++){
		printf("%d ",a[i]);
	}
}
