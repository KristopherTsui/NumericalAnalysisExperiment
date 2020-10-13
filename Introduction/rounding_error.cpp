#include<iostream>

using namespace std;

/* function statement */
double f(double);
double forward_difference_quotient(double, double, double (*)(double));
double central_difference_quotient(double, double, double (*)(double));

int main()
{
	double x0 = 1;
	for(double h = 1; h >= 1e-15; h /= 10)
	{
		cout << "When h = " << h << endl;
		cout.precision(16);
		cout << "The forward difference quotient of f(x) at x=1 is "
			 << forward_difference_quotient(x0, h, f) << endl;
		cout << "The central difference quotient of f(x) at x=1 is "
			 << central_difference_quotient(x0, h, f) << endl;
	}

	return 0;
}


double f(double x)
{
	return x*x*x;
}

/**
 * @brief Calculate the forward difference quotient
 * @param x0 double, 
 * @param h double, the step length of the difference quotient
 * @param (*f)() function pointer, the function to solve
 *
 * @Returns double, the forward difference quotient of f at x0 with step h
 */
double forward_difference_quotient(double x0, double h, double (*f)(double x))
{
	return (f(x0 + h) - f(x0))/h;
}

/**
 * @brief Calculate the central difference quotient
 * @param x0 double, 
 * @param h double, the step length of the difference quotient
 * @param (*f)() function pointer, the function to solve
 *
 * @Returns double, the central difference quotient of f at x0 with step h
 */
double central_difference_quotient(double x0, double h, double (*f)(double x))
{
	return (f(x0 + h) - f(x0 - h)) / (2 * h);
}

