#include<iostream>
#include<cmath>

using namespace std;

/* function statement */
void sqrt_iteration_algorithm(double a, double x0, double tol=1e-5, int Max_iter=100);

int main()
{
	double a = 5;
	
	// various iteration initial value
	for (int x = 1; x <= 1000; x*=10)
		sqrt_iteration_algorithm(a, x);

	return 0;
}

/**
 * @brief Calculate the square root of a by iteration algorithm.
 * @param a: double, the value whose square root is to be calculated
 * @param x0: double, initial value of iteration
 * @param tol: double, iteration accuracy
 * @param Max_iter: int, maximum iteration number
 */
void sqrt_iteration_algorithm(double a, double x0, double tol, int Max_iter)
{
	// iteration number
	int k = 0;
	// initial
	double x = 0, y = x0;

	// iteration
	do {
		k++;
		x = y;
		y = (x + a / x) / 2;
	}while(fabs((y - x)/y) >= tol && k < Max_iter);

	cout << "The square root of " << a << " is " << y
		 << " with the initial value " << x0 
		 << " and the iteration number is " << k << '.'
		 << endl;
}

