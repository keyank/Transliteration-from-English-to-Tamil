#include<stdio.h>

int main()
{

	char S[100];
	printf("sed 's/a/ 1/g' $1 | ");

	int i = 2;
	for(i = 2; i< 26; i++)
	{
		printf("sed 's/%c/ %d/g' | " , 'a' + (i-1) , i);
	}

	printf("sed 's/%c/ %d/g' \n" , 'a' + (i-1) , i);

}