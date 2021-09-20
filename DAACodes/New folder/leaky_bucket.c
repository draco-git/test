#include <stdio.h>
int main(){
    int n, bucketSize, packetSize, outgoing, store = 0;
    printf("Enter the number of packets to be sent: ");
    scanf("%d", &n);
    printf("Enter the bucket size: ");
    scanf("%d", &bucketSize);
    printf("Enter the outgoing rate: ");
    scanf("%d", &outgoing);
    while (n--){
        printf("\nEnter the size of the incoming packet: ");
        scanf("%d", &packetSize);
        if (packetSize <= bucketSize - store){
            store += packetSize;
        }
        else{
            printf("Data lost from the packet: %d\n", packetSize - bucketSize + store);
            store = bucketSize;
            printf("Bucket full\n");
        }
        printf("Packets bucket can hold is %d out of %d\n", bucketSize - store, bucketSize);
        store -= outgoing;
        if (store < 0)
            store = 0;
        printf("After outgoing Packets bucket can hold is %d out of %d\n", bucketSize - store, bucketSize);

    }
    return 0;
}
