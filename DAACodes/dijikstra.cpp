#include<stdio.h>

int main(){
	int vertices,c[10][10],i,j,startNode,prevNode,nextNode,k;
	int dist[10],visit[10],pre[10],count,minDist;
	printf("enter no of vertices\n");
	scanf("%d",&vertices);
	printf("enter the matrix\n");
	for(i=0;i<vertices;i++){
		for(j=0;j<vertices;j++){
			scanf("%d",&c[i][j]);
			if(c[i][j]==0){
				//initializing nodes as there is a infinite distance for loops
				c[i][j]=999;
			}
		}
	}
	printf("enter the start node\n");
	scanf("%d",&startNode);
	for(k=0;k<vertices;k++){ //init the distances from start node and visited nodes in visit array
		dist[k]=c[startNode][k];
		visit[k]=0;
		pre[k]=startNode;
	}
	printf("\n the dist array");
	for(i=0;i<vertices;i++){
		printf("%d ",dist[i]);
	}
	count=1;
	visit[startNode]=1;
	dist[startNode] =0;
	while(count<vertices){
		minDist = 999;
		for(k=0;k<vertices;k++){
			if(dist[k]<minDist && !visit[k]){
				minDist = dist[k];
				nextNode = k;
			}
		}
		visit[nextNode] = 1;
		for(k=0;k<vertices;k++){
			if(!visit[k]){
				if((minDist+c[nextNode][k])<dist[k]){
					dist[k] = minDist+c[nextNode][k];
					pre[k] = nextNode;
				}
			}
		}
		count++;
	}
	//for printing
	for(i=0;i<vertices;i++){
		if(i!=startNode){
			printf("\nthe distance of %d is %d",i,dist[i]);
			printf("\npath=%d",i);
			j=i;
			do{
				j=pre[j];
				printf("<--%d",j);
			}while(j!=startNode);
		}
	}
//	//test matrix
//	for(i=0;i<vertices;i++){
//		for(j=0;j<vertices;j++){
//			printf("%d\n",c[i][j]);
//		}
//	}
}
