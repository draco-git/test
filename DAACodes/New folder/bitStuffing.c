#include <stdio.h>
#include <string.h>
int main() {
    int i, count = 0, k = 0;
    char flag [] = "01111110";
    char string[100], data[100];
    printf("Enter the message:");
    scanf("%s",string);

    printf("\nBit Stuffing: ");
    printf("\nOriginal data: %s", string);
    for(i=0; i<strlen(string); i++){
        if (string[i] == '1'){
            count++;
        }
        else{
            count = 0;
        }
        data[k++] = string[i];
        if (count == 5){
            data[k++] = '0';
            count = 0;
        }
    }
    strcat(flag, data);
    strcpy(data, flag);
    strcat(data, "01111110");
    printf("\nBit stuffed data: ");
    puts(data);
    printf("\nDe-stuffing: ");
    printf("\nDe-stuffed data: ");
    count = 0;
    for (i=8; i < strlen(data)-8; i++){
        if (data[i] == '1'){
            printf("%c", data[i]);
            count++;
        }
        else{
            printf("%c", data[i]);
            count = 0;
        }
        if (count == 5 && data[i+1] == '0'){
            i++;
            count = 0;
        }
    }

    return 0;
}
