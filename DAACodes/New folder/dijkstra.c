#include <stdio.h>
#define INF 9999
int main(){
    int cost[20][20], distance[20], visited[20];
    int n, min_node, vertex, edges, min_distance, i, j;

    printf("Enter the number of nodes in the computer network: ");
    scanf("%d", &n);
    printf("Enter the cost matrix for the network:\n");
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            scanf("%d", &cost[i][j]);
            if(cost[i][j] == 0){
                cost[i][j] = INF;
            }
        }
    }
    printf("Enter the source node: ");
    scanf("%d", &vertex);

    for(i=0; i<n; i++){
        distance[i] = cost[vertex][i];
        visited[i] = 0;
    }
    edges = n-2;
    while (edges--){
        min_distance = 99;
        for(i=0; i<n; i++){
            if (distance[i] < min_distance && !visited[i]){
                min_distance = distance[i];
                min_node = i;
            }
        }
        visited[min_node] = 1;
        for(i=0; i<n; i++){
            if (distance[min_node] + cost[min_node][i] < distance[i] && !visited[i]){
                distance[i] = distance[min_node] + cost[min_node][i];
            }
        }
    }

    printf("cost of travelling from \n");
    for(i=0; i<n; i++){
        if(i != vertex){
            printf("%d->%d is %d\n", vertex, i, distance[i]);
        }
    }
    return 0;
}
