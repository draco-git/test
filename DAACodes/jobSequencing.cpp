#include<stdio.h>
typedef struct Job{
	char id[5];
	int deadLine;
	int profit;
}job;
int minV(int x,int y){
	if(x<y){
		return x;
	}
	return y;
}
void jobSequencing(int n , job jobs[]){
	int maxProfit=0,i,k,dmax,filledSlots=0;
	int timeSlots[10];
	dmax = 0;
	for(i=0;i<n;i++){
		if(jobs[i].deadLine>dmax){
			dmax = jobs[i].deadLine;
		}
	}
	for(i=1;i<=dmax;i++){
		timeSlots[i]  = -1;
	}
	
	for(i=1;i<=n;i++){
		k = minV(dmax,jobs[i-1].deadLine);
		while(k>=1){
			if(timeSlots[k]==-1){
				timeSlots[k] = i-1;
				filledSlots++;
				break;
			}
			k--;
		}
		if(filledSlots == dmax){
			break;
		}
	}
	
	printf("\njob order\n");
	for(i=1;i<=dmax;i++){
		printf("%s",jobs[timeSlots[i]].id);
		maxProfit += jobs[timeSlots[i]].profit;
		if(i<dmax){
			printf("-->");
		}
	}
	printf("\nthe maxProfit is %d",maxProfit);
}
int main(){
	int i,j,n;
	job jobs[5] = {
	{"j1", 2,  60},
    {"j2", 1, 100},
    {"j3", 3,  20},
    {"j4", 2,  40},
    {"j5", 1,  20},
	};
	job temp;
	for(i=1;i<n;i++){
		for(j=0;j<n-i;j++){
			if(jobs[j+1].profit > jobs[j].profit){
				temp = jobs[j+1];
				jobs[j+1] = jobs[j];
				jobs[j] = temp;
			}
		}
	}
	n = 5;
	jobSequencing(n,jobs);
	return 0;
}
