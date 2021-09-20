#include<stdio.h>
void merge(int a[],int low,int high){
	int mid = (low+high)/2,temp[10];
	int i = low;
	int j = mid+1;
	int k =  low;
	while(i<=mid && j<=high){
		if(a[i]<a[j]){
			temp[k++] = a[i++];
		}
		else{
			temp[k++] = a[j++];
		}
		while(i<=mid){
			temp[k++] = a[i++];
		}
		while(j<=high){
			temp[k++] = a[j++];
		}
		for(i=low;i<=high;i++){
			a[i] = temp[i];
		}
	}
}
void mergeSort(int a[],int low,int high){
	int mid;
	mid = (low+high)/2;
	if(low>=high){
		return;
	}
	else{
		mergeSort(a,low,mid);
		mergeSort(a,mid+1,high);
		merge(a,low,high);
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
	mergeSort(a,0,n-1);
	printf("numbers after sorting\n");
	for(i=0;i<n;i++){
		printf("%d ",a[i]);
	}
}
