#include<stdio.h>

int main()
{
	int Left[456];
	int Right[456];

	for (int i = 0; i< 456; i++)
	{
		scanf("%d%d",&Left[i], &Right[i]);
		printf("if (num == %d):\n ", Left[i]);
		printf("\t return %d\n", Right[i] );
	}

}

