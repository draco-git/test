#include <stdio.h>
#include <stdbool.h>
#include <string.h>
int i,j,genlen,msglen;
char data[100], generator[30],temp[30],quotient[100],Remainder[30],key1[30];
bool CheckRemainder(){
    for (i=0;i<genlen-1;i++)
        if (Remainder[i] != '0'){
            return false;
        }
    return true;
}
void divide(){
    for (i=0;i<genlen;i++)
	    temp[i]=data[i];
	for (i=0;i<msglen;i++) {
		quotient[i]=temp[0];
		if(quotient[i]=='0')
		    for (j=0;j<genlen;j++)
		        generator[j]='0';
        else
		    for (j=0;j<genlen;j++){
                generator[j]=key1[j];
            }

		for (j=genlen-1;j>0;j--) {
			if(temp[j]==generator[j])
			 Remainder[j-1]='0'; else
			 Remainder[j-1]='1';
		}
		Remainder[genlen-1]=data[i+genlen];
		strcpy(temp,Remainder);
	}
	strcpy(Remainder,temp);
 }
 int main() {
	printf("Enter the stream of data bits (no spaces): ");
	gets(data);
	printf("Enter the generator: ");
	gets(generator);
	genlen=strlen(generator);
	msglen=strlen(data);
	strcpy(key1,generator);
	for (i=0;i<genlen-1;i++) {
		data[msglen+i]='0';
	}
	divide();
	printf("\nAt Sender side: ");
	printf("Quotient is ");
    puts(quotient);
	printf("Remainder is ");
    puts(Remainder);
	printf("\nThe encoded data sent is: ");
    for (i=0;i<genlen-1;i++)
        data[i+msglen] = Remainder[i];
    puts(data);


    printf("\nAt receiver side: \n");
    printf("Enter the received data: ");
    gets(data);
    divide();
    printf("Remainder is ");
    puts(Remainder);
    if (CheckRemainder()){
        printf("\nData is correct, No error found.\n");
    }
    else{
        printf("\nError detected in the data. \n");
    }
return 0;
}
