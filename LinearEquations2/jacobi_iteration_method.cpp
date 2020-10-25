#include<iostream>
#include<cmath>
#define N 3 // order of the linear euqations

using namespace std;

/* function statement */
void jacobi_iteration(double A[][N], double b[], double x[], double epsilon = 1e-9, int Max_iter = 5000);

int main()
{
	// cofficients matrix
	double a[N][N] = {{5, 2, 1}, {2, 8, -3}, {1, -3, -6}};
	// constant vector
	double b[N] = {8, 21, 1};
	// iteration accuracy
	double e = 1e-5;
	// solution vector
	double x[N];
	// Jacobi iteration method
	jacobi_iteration(a, b, x, e);
	
	return 0;
}

/**
 * @brief Solve linear equations by Jacobi iteration method.
 * @param A: double [][N], cofficients matrix
 * @param b: double [], constant vector
 * @param x: double [], solution vector
 * @param epsilon: double, iteration accuracy
 * @param Max_iter: int, defaut = 5000
 */
void jacobi_iteration(double A[][N], double b[], double x[], double epsilon, int Max_iter)
{
	int i, j, c_M = 0;
	double sum, current_e;
	double x0[N]= {1, 1, 1}; // initial iteration vector
	
	// Determine whether the accuracy requirements have not been met and the maximum number of iterations has not been reached
	do{
		current_e = 0;
		// update iteration vector
		for (i = 0; i < N; i++)
		{
			sum = 0;
			for (j = 0; j < N; j++)
				if (j != i)
					sum += A[i][j] * x0[j];
			x[i] = (b[i] - sum) / A[i][i];
		}

		c_M++; // iteration number +1
		// calculate error
		for (i = 0; i < N; i++)
			if (fabs(x[i] - x0[i]) > current_e)
				current_e = fabs(x[i] - x0[i]);

		// update initial vector
		for (i = 0; i < N; i++)
			x0[i] = x[i];
	}while(current_e > epsilon && c_M < Max_iter);

	// output the solution and the iteration number
	for (i = 0; i < N; i++)
		cout << x[i] << endl;
	cout << c_M << endl;
}

