#include<iostream>
#include<cmath>
#define N 4 

using namespace std;

/* function statement */
void successive_over_relaxation(double A[][N], double b[], double omega, double tol=1e-9, int Max_iter=500);

int main()
{
	double a[N][N] = {{-4, 1, 1, 1}, {1, -4, 1, 1}, {1, 1, -4, 1}, {1, 1, 1, -4}};
	double b[N] = {1, 1, 1, 1};
	double omega = 1.3;

	/* SOR method */
	successive_over_relaxation(a, b, omega);

	return 0;
}

/**
 * @brief Solve linear equations by Successive over relaxation method.
 * @param A: double [][N], cofficients matrix
 * @param b: double [], constant vector
 * @param omega: double, successive over relaxation
 * @param tol: double, iteration accuracy
 * @param Max_iter: int, maximum, iteration number
 */
void successive_over_relaxation(double A[][N], double b[], double omega, double tol, int Max_iter)
{
	double x0[N] = {1, 1, 1}; // initial vector
	double x[N];              // solution vector
	double current_e;
	int k = 0;                // initialize interation number

	do {
		current_e = 0;
		/* update iteration vector */
		for (int i=0; i<N; i++)
		{
			double sum = 0;
			for (int j=0; j<i; j++)
				sum += A[i][j] * x[j];
				
			for (int j=i+1; j<N; j++)
				sum += A[i][j] * x0[j];
				
			x[i] = (1 - omega) * x0[i] + omega * (b[i] - sum) / A[i][i]; 
		}

		k++;                  // update iteration number
		/* calculate error */
		for (int i=0; i<N; i++)
			if (fabs(x[i] - x0[i]) > current_e)
				current_e = fabs(x[i] - x0[i]);

		/* update initial vector */
		for (int i=0; i<N; i++)
			x0[i] = x[i];
	}while(current_e > tol && k < Max_iter);

	// output
	cout << "The solutin vector of the linear equations is " << endl;
	for (int i=0; i<N; i++)
		cout << x[i] << ' ';
	cout << endl << "The iteration number is " << k << endl;
	
}
