#include<iostream>
#include<cmath>
#define N 3

using namespace std;

/* function statement */
void column_pivot_lu_decomposition(double [][N], int [], double [][N], double [][N]);
void solve_by_lu(double [][N], double [][N], int [], double []);

int main()
{
	double A[N][N] = {0.101, 2.304, 3.555,
					  -1.347, 3.712, 4.623,
					  -2.835, 1.072, 5.643}; 
	double b[N] = {1.183, 2.137, 3.035};
	double L[N][N] = {0, 0, 0,
					  0, 0, 0,
					  0, 0, 0};
	double U[N][N] = {0, 0, 0,
					  0, 0, 0,
					  0, 0, 0};
	int P[N];
	column_pivot_lu_decomposition(A, P, L, U);
	solve_by_lu(L, U, P, b);

	return 0;
}

/**
 * @brief Column pivot LU decomposition of matrix A.
 * @param A: double [][N], the matrix to be decomposited
 * @prram P: int [], the swap vector
 * @param L: double [][N], L matrix
 * @param U: double [][N], U matrix
 */
void column_pivot_lu_decomposition(double A[][N], int P[], double L[][N], double U[][N])
{
	// initialize P
	for(int k = 0; k < N; k++)
		P[k] = k + 1;

	// begin
	for(int k = 0; k < N-1; k++)
	{
		int s;
		s = k;
		// select column pivot
		for (int i=k+1; i < N; i++)
			if(fabs(A[i][k]) > fabs(A[s][k]))
				s = i;

		if (s != k)
		{
			double m;
			// swap row
			for (int j = 0; j < N; j++)
				swap(A[k][j], A[s][j]);

			swap(P[s], P[k]);
		}

		if (A[k][k] == 0)
		{
			cout << "There exists zero pivot!!!" << endl;
			continue;
		}

		for (int i=k+1; i < N; i++)
		{
			A[i][k] = A[i][k] / A[k][k];

			// calculate matrix U
			for (int j=k+1; j < N; j++)
				A[i][j] = A[i][j] - A[i][k] * A[k][j];
		}
	}

	// calculate L
	for (int i = 0; i < N; i++)
	{
		for(int j = 0; j < i+1; j++)
		{
			if (i == j)
				L[i][j] = 1;
			else
				L[i][j] = A[i][j];
		}
	}

	// calculate U
	for (int i=0; i < N; i++)
		for (int j = i; j < N; j++)
			U[i][j] = A[i][j];
}

/**
 * @brief Solve linear equations by column pivot LU decomposition
 * @param L: double [][N], L of A's LU decomposition
 * @param U: double [][N], U of A's LU decomposition
 * @param P: int [], the swap vector
 * @param b: double [], constant vector
 */
void solve_by_lu(double L[][N], double U[][N], int P[], double b[])
{
	/* update b */
	double z[N];
	for (int i = 0; i < N; i++)
		z[i] = b[P[i] - 1];

	double y[N];
	double x[N];
	for (int i=0; i<N; i++)
	{
		double sum = 0;
		for (int j=0; j<i; j++)
			sum += L[i][j] * y[j];

		y[i] = (z[i] - sum) / L[i][i];
	}

	for (int i=N-1; i>=0; i--)
	{
		double sum = 0;
		for (int j=i+1; j<N; j++)
			sum += U[i][j] * x[j];

		x[i] = (y[i] - sum) / U[i][i];
	}

	cout << "The solution vector of the linear equaitons is " << endl;
	for (int i=0; i<N; i++)
		cout << x[i] << ' ';
	cout << endl;
}

