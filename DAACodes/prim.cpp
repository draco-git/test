#include<stdio.h>

int main(){
	int ne=1,n,c[10][10],traversed[10]={0};
	int minc=0,min,a,b,x,y,i,j;
	printf("enter no of vertices\n");
	scanf("%d",&n);
	printf("\n enter the matrix \n");
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			scanf("%d",&c[i][j]);
			if(c[i][j]==0){
				c[i][j]=999;
			}
		}
	}
	traversed[1] = 1;
	while(ne<n){
		min = 999;
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				if(c[i][j]<min){
					if(traversed[i]!=0){
						min = c[i][j];
						a=x=i;
						b=y=j;
					}
				}
			}
		}
		if(traversed[x]==0 || traversed[y]==0){
			printf("\n %d edge(%d,%d) is %d",ne++,a,b,min);
			minc = minc+min;
			traversed[b] =1;
		}
		c[a][b] = c[b][a] = 999;
	}
	printf("\n total cost is %d",minc);
	return 0;
	
}
