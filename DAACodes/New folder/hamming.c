#include <stdio.h>
int main(){

    int data[20], received_data[20], i, c, c1, c2, c3;

    printf("Enter 4 data bits with spaces in between them: ");
    scanf("%d",&data[0]);
    scanf("%d",&data[1]);
    scanf("%d",&data[2]);
    scanf("%d",&data[4]);

    data[3] = data[0]^data[1]^data[2];
    data[5] = data[0]^data[1]^data[4];
    data[6] = data[0]^data[2]^data[4];

    printf("\nAt sender side: \nThe encoded signal is: ");
    for(i=0;i<7;i++){
        printf("%d",data[i]);
    }
    printf("\n\nAt Receiver side: ");
    printf("\nEnter the receiving data bits with spaces in between: ");
    for(i=0;i<7;i++){
        scanf("%d",&received_data[i]);
    }

    c1 = received_data[6] ^ received_data[4] ^ received_data[2] ^ received_data[0];
    c2 = received_data[5] ^ received_data[4] ^ received_data[1] ^ received_data[0];
    c3 = received_data[3] ^ received_data[2] ^ received_data[1] ^ received_data[0];
    c = 4*c3 + 2*c2 + c1;

    if(c == 0){
        printf("\nNo error detected in the received data.");
    }
    else{
        printf("\nError detected at position %d\n", 7-c+1);
        printf("Data received is: ");
        for(i=0;i<7;i++){
            printf("%d",received_data[i]);
        }
        printf("\nAfter correcting, the message is: ");
        if (received_data[7-c] == 0)
            received_data[7-c] = 1;
        else
            received_data[7-c] = 0;
        for(i=0;i<7;i++){
            printf("%d",received_data[i]);
        }
    }
    printf("\nThe message after decoding: ");
    printf("%d",data[0]);
    printf("%d",data[1]);
    printf("%d",data[2]);
    printf("%d",data[4]);

    return 0;
}


