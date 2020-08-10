#include <stdio.h>

main()
{

	int x, y=0;
	x=y++;
	printf("\n valor de x= %d, valor de y=%d",x,y);
	
	y=3;
	x=++y;
	printf("\n %d \n %d",y,x);
}

