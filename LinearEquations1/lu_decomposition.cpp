#include<iostream>
#include<cmath>
#define N 3

using namespace std;

/* function statement */
void lu_decomposition(double [][N]);
void column_pivot_lu_decomposition(double [][N], double []);
void output1(double [][N]);
void output2(double [][N], double []);

int main()
{
	double a[N][N] = {{1, 2, 2}, {4, 4, 2}, {4, 6, 4}};
	double b[N][N] = {{1, 2, 2}, {4, 4, 2}, {4, 6, 4}};

	// LU decomposition
	lu_decomposition(a);
	// output
	cout << "The LU decomposition of matrix A is " << endl;
	output1(a);

	double p[N];
	// column pivot LU decomposition
	column_pivot_lu_decomposition(b, p);
	// output
	cout << "The column pivot LU decomposition of matrix A and the swap vector P are " << endl;
	output2(b, p);
	return 0;
}

/**
 * @brief: LU decomposition of matrix A.
 * @param: A: double [][N], the matrix to be decomposited
 */
void lu_decomposition(double A[][N])
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
}

/**
 * @brief: Column pivot LU decomposition of matrix A.
 * @param: A: double [][N], the matrix to be decomposited
 */
void column_pivot_lu_decomposition(double A[][N], double P[])
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
}

/**
 * @brief: Output the LU decomposition.
 * @param: A: double [][N], the LU decomposition matrix
 */
void output1(double A[][N])
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			cout << A[i][j] << '\t';

		cout << endl;
	}
}

/**
 * @brief: Output the LU decomposition and the swap vector.
 * @param A: double [][N], the LU decomposition matrix
 * @param P: double [], the swap vector
 */
void output2(double A[][N], double P[])
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			cout << A[i][j] << '\t';

		cout << endl;
	}

	for (int i = 0; i < N; i++)
		cout << P[i] << endl;
}

