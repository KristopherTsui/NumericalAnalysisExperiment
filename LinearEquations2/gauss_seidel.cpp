#include<iostream>
#include<cmath>
#define N 3

using namespace std;

/* function statement */
void gauss_seidel(double A[][N], double b[], double x0[], double tol=1e-9, int Max_iter=500);

int main()
{
	double a[N][N] = {{5, 2, 1}, {2, 8, -3}, {1, -3, -6}};
	double b[N] = {8, 21, 1};
	/* experiment 2
	double a[N][N] = {{-4, 1, 1, 1}, {1, -4, 1, 1}, {1, 1, -4, 1}, {1, 1, 1, -4}};
	double b[N] = {1, 1, 1, 1};
	*/
	/* thinking 4
	double a[N][N] = {{1, -3, -6}, {2, 8, -3}, {5, 2, 1}};
	double b[N] = {1, 21, 8}; 
	*/
	double x[N];

	// Gauss Seidel iteration method
	gauss_seidel(a, b, x, 1e-5);

	return 0;
}

/**
 * @brief Solve linear equations by Gauss Seidel iteration method.
 * @param A: double [][N], cofficients matrix
 * @param b: double [], constant vector
 * @param x: double [], initial vector
 * @param tol: double, iteration accuracy
 * @param Max_iter: int, maximum iteration number
 */
void gauss_seidel(double A[][N], double b[], double x[], double tol, int Max_iter)
{
	double current_e;
	int k = 0;
	double x0[N] = {1, 1, 1};
	do {
		current_e = 0;

		/* update iteration vector */
		for (int i=0; i < N; i++)
		{
			double sum = 0;
			for (int j = 0; j < i; j++)
				sum += A[i][j] * x[j];
				
			for (int j=i+1; j < N; j++) 
				sum += A[i][j] * x0[j];

			x[i] = (b[i] - sum) / A[i][i];
		}

		k++;
		/* calculate the error */
		for (int i=0; i < N; i++)
			if (fabs(x[i] - x0[i]) >= current_e)
				current_e = fabs(x[i] - x0[i]);

		/* update initial vector */
		for (int i = 0; i < N; i++)
			x0[i] = x[i];
	}while(current_e > tol && k < Max_iter);

	// output
	cout << "The solution vector is " << endl;
	for (int i = 0; i < N; i++)
		cout << x[i] << ' ';
	cout << endl << "The iteration number is " << k << endl;
}
 
