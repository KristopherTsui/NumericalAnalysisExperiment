#include<iostream>
#include<cmath>

#define N 101

using namespace std;

/* function statement */
void method1(double []);
void method2(double []);
void print_arrays(double [], double [], int);

int main()
{
	// initial value
	double answer1[N], answer2[N];
	answer1[0] = log(6.0/5);
	answer2[100] = (606 + 505) / 505.0 / 606 / 2;

	// two methods	
	method1(answer1);
	method2(answer2);

	// output
	print_arrays(answer1, answer2, N);
	
	return 0;
}


/**
 * @brief Calculate I_n by method1 which disconverges
 * @param array double [], a array storing data
 *
 * @Returns None
 */
void method1(double array[])
{
	for(int i = 1; i < N; i++)
	{
		array[i] = 1.0/i - 5 * array[i-1];
	}
}

/**
 * @brief Calculate I_n by method2 which converges
 * @param array double [], a array storing data
 *
 * @Returns None
 */
void method2(double array[])
{
	for(int i = 100; i > 0; i--)
	{
		array[i-1] = (1.0/i - array[i]) / 5;
	}
}

/**
 * @brief print the data calculated by method 1 and method 2
 * @param array1 double[], the data from method 1
 * @param array2 double[], the data from method 2
 * @param N int, the number of the data
 *
 * @Returns None
 */
void print_arrays(double array1[], double array2[], int n)
{
	// set precision
	cout.precision(16);
	for(int i = 1; i < n; i++)
	{
		cout << i << '\t' << array1[i] << '\t' << array2[i] << endl;
	}
}

