#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
/*
	int i;
	for(i=0 ; i<10 ; i +=1){
		printf("Hola %d \n", i);
	}
int j;	
for (j= 0; j< 5; j += 1){
	for (i=0 ; i<10; i += 1){
	printf("#");
}
printf("\n");
}
*/
int j;
	int i;	
for (j= 0; j< 5; j += 1){
	for (i=0 ; i<10; i += 1){
		if(j==0 || j == 4 || i ==0 || i==9)
	printf("#");
	else{
		printf(" ");
	}
}
printf("\n");
}

	return 0;
}

