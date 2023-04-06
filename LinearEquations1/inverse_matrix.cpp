#include<iostream>
#include<cmath>
#define N 3

using namespace std;

/* function statement */
void inverse_matrix(double [][N], double [][N]);
void lu_decomposition(double [][N], double [][N], double [][N]);
void output(double [][N]);


int main()
{
	double a[N][N] = {{1, 2, 2}, {4, 4, 2}, {4, 6, 4}};
	double inv_a[N][N];

	// calculate the inverse matrix of A
	inverse_matrix(a, inv_a);

	// output
	cout << "The inverse matrix of A is " << endl;
	output(inv_a);
	

	return 0;
}

/**
 * @brief Calculate the inverse matrix of A by LU decomposition
 * @param A: double [][N], the matrix whose inverse is to be calculated
 * @param inv_A: double [][N], inverse matrix of A
 */
void inverse_matrix(double A[][N], double inv_A[][N])
{
	double L[N][N] = {0, 0, 0,
					  0, 0, 0,
					  0, 0, 0};
	double U[N][N] = {0, 0, 0,
					  0, 0, 0,
					  0, 0, 0};
	double inv_U[N][N], inv_L[N][N];

	// LU decomposition
	lu_decomposition(A, L, U);

	// calculate the inverse matrix of L
	for (int i = 0; i < N; i++)
	{
		inv_L[i][i] = 1;
		for (int k = i+1; k < N; k++)
			for (int j = i; j < k; j++)
				inv_L[k][i] -= L[k][j] * inv_L[j][i];
	}

	// calculate the inverse matrix of U
	for (int i=0; i < N; i++)
	{
		inv_U[i][i] = 1 / U[i][i];
		for (int k=i-1; k >= 0; k--)
		{
			double s = 0;
			for (int j=k+1; j <= i; j++)
				s += U[k][j] * inv_U[j][i];

			inv_U[k][i] = -s / U[k][k];
		}
	}

	// calculate the inverse matrix of A
	for (int i=0; i < N; i++)
		for (int j=0; j < N; j++)
			for (int k=0; k < N; k++)
				inv_A[i][j] += inv_U[i][k] * inv_L[k][j];
}

/**
 * @brief: LU decomposition of matrix A.
 * @param: A: double [][N], the matrix to be decomposited
 * @param: L: double [][N], L matrix
 * @param: U: double [][N], U matrix
 */
void lu_decomposition(double A[][N], double L[][N], double U[][N])
{
	for (int k = 0; k < N-1; k++)
	{
		if(A[k][k] == 0)
		{
			cout << "The main element is zero!!!" << endl;
			break;
		}

		for(int i = k+1; i < N; i++)
		{
			A[i][k] = A[i][k] / A[k][k];

			// calculate the matrix U
			for(int j = k+1; j < N; j++)
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
 * @brief Output the matrix.
 * @param A: double[][N], the matrix to be printed
 */
void output(double A[][N])
{
	for (int i=0; i < N; i++)
	{
		for (int j=0; j < N; j++)
			cout << A[i][j] << '\t';
		cout << endl;
	}
}

