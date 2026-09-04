#define N 11
int ARRAY[N]= {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21};
void main (void)
{
	int total = sum_array(ARRAY);
	printf ("The total is: %d", total);
}
int sum_array(int ARRAY[N])
{
	int total=0;
	for (int i=0; i<N; i++ )
	{
		total+=ARRAY[i];
	}
	return total; // total == 121
}
