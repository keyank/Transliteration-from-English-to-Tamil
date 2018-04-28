#include<stdio.h>

int main()
{
	char Left[12][50];
	char Right[12][50];

	char consonants[18][50];
	for (int i = 0; i< 12; i++)
	{
		scanf("%s", Left[i]);
		scanf("%s", Right[i]);

	}

	for (int i = 0; i< 18; i++)
	{
		scanf("%s", consonants[i]);

	} 
	int count  = 0;
	for (int i = 0; i< 18; i++)
	{
		for(int j = 0; j< 12; j++)
		{
			count++;
			printf("%s%s\t%s%s\n", consonants[i], Left[j] , consonants[i], Right[j] );
		}
	}


}

