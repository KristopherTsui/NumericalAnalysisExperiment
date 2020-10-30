#include<iostream>
#include<cmath>
#define N 3

using namespace std;

/* function statement */
double determinant(double [][N]);
void lu_decomposition(double [][N]);

int main()
{
	double a[N][N] = {{1, 2, 2}, {4, 4, 2}, {4, 6, 4}};

	cout << "The determinant of matrix A is " << determinant(a) << endl;
	return 0;
}

/**
 * @brief: Calculte the determinant of matrix A by LU decomposition.
 * @param: A: double [][N], the matrix whose determinant is to be calculated.
 *
 * @Returns: det: double, the determinant of matrix A
 */
double determinant(double A[][N])
{
	lu_decomposition(A);
	double det = 1;

	for (int i = 0; i < N; i++)
		det *= A[i][i];

	return det;
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

