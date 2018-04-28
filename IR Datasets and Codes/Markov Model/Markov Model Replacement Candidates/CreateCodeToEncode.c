#include<stdio.h>


int main()
{
	char S[100]; 
	scanf("%s", S);
	printf("sed 's/ %s/%d /g' $1 | ", S, 1);
	for (int i = 2; i<= 313; i++)
	{
		scanf("%s", S);
		printf("sed 's/%s/%d /g' | ", S, i);
	}


}


