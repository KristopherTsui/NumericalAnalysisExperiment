#include<iostream>
#include<cmath>

#define N 3 

using namespace std;

/* function statement */
void solve_linear_equations(double [][N+1]);
int select_principal_element(double [][N+1], int);
void swap_rows(double [][N+1], int, int);
void output(double [][N+1]);

int main()
{
	// Augmented matrix
	double a[N][N+1] = {0.101, 2.304, 3.555, 1.183,
						-1.347, 3.712, 4.623, 2.137,
						-2.835, 1.072, 5.643, 3.035};
	
	// solve linear equations
	cout << "The solution of the first equaitons is:" << endl;
	solve_linear_equations(a);

	/* the equations two, set N = 4
	double b[N][N+1] = {0.3*1e-15, 59.14, 3, 1, 59.17,
						5.291, -6.13, -1, 2, 46.78,
						11.2, 9, 5, 2, 1,
						1, 2, 1, 1, 2};
	cout << "The solution of the second equations is" << endl;
	solve_linear_equations(b);*/
	
	return 0;
}

/**
 * @brief Solve the linear equations by Gaussian elimination method
 * @param A: double [][], the augmented matrix
 */
void solve_linear_equations(double A[][N+1])
{
	for(int i = 0; i < N - 1; i++)
	{
		// select the column principal element's row
		int r = select_principal_element(A, i);

		// swap between the i-th row and r-th row
		swap_rows(A, i, r);

		// elimination
		for(int j = i + 1; j < N; j++)
		{
			double l = A[j][i] / A[i][i];
			for(int k = i; k < N + 1; k++)
				A[j][k] -= l * A[i][k];
		}
	}

	// solution vector
	double x[N];
	// back generation 
	x[N-1] = A[N-1][N] / A[N-1][N-1];
	for(int i = N - 2; i >= 0; i--)
	{
		for(int j = i + 1; j < N; j++)
			A[i][N] -= A[i][j] * x[j];

		x[i] = A[i][N] / A[i][i];
	}
	
	// output
	for(int i = 0; i < N; i++)
		cout << 'x' << i+1 << " = " <<  x[i] << endl;
}

/** 
 * @brief Select the absolute maximum element in the column
 * @param A: double [][], the Augmented matrix
 * @param c: int, the c-th column
 *
 * @Returns max: int, the row where the column principal element is at
 */
int select_principal_element(double A[][N+1], int c)
{
	// the absolute maximum element's row index in the c-th column
	int max = c;
	// iteration
	for (int r = c + 1; r < N; r++)
		max = fabs(A[r][c]) > fabs(A[max][c]) ? r : max;
	
	return max;
}

/**
 * @brief Swap the two rows in the matrix
 * @param A: double [][N+1], the Augmented matrix
 * @param r1: int, the index of the row to be swaped, r1 < r2
 * @param r2: int, another index of the row to be swaped, r1 < r2
 */
void swap_rows(double A[][N+1], int r1, int r2)
{
	for(int c = r1; c < N + 1; c++)
		swap(A[r1][c], A[r2][c]);
}

void output(double A[][N+1])
{
	for (int i=0; i < N; i++)
	{
		for (int j=0; j < N+1; j++)
			cout << A[i][j] << '\t';

		cout << endl;
	}
}

