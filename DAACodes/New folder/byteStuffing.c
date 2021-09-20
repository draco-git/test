#include <stdio.h>
#include <string.h>
int main(){
    int i;
    char string[100], data[100] = "", flag [] = "flag";
    printf("Enter the data (characters): ");
    gets(string);
    printf("\nStuffing the data: \n");
    int k = 0;
    for(i = 0; i<strlen(string); i++){
        if (string[i] == 'f' && string[i+1] == 'l' && string[i+2] == 'a' && string[i+3] == 'g'){
            data[k++] = 'e';
            data[k++] = 's';
            data[k++] = 'c';
            data[k++] = string[i];
        }
        else if (string[i] == 'e' && string[i+1] == 's' && string[i+2] == 'c'){
            data[k++] = 'e';
            data[k++] = 's';
            data[k++] = 'c';
            data[k++] = string[i];
        }
        else{
            data[k++] = string[i];
        }
    }
    strcat(flag, data);
    strcpy(data, flag);
    strcat(data, "flag");
    puts(data);

    printf("\nDe-stuffing the received data: \n");
    for(i=4; i<strlen(data)-4; i++){
        if (data[i] == 'e' && data[i+1] == 's' && data[i+2] == 'c'){
            i += 3;
        }
        printf("%c",data[i]);
    }
    return 0;
}
