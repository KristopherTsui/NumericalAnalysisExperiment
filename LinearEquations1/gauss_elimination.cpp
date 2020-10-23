#include<iostream>
#include<cmath>
#define N 3 

using namespace std;

/* function statement */
void gauss_method(double [][N+1], double []);
int verify_solution(double [][N+1], double []);

int main()
{
	// augmented matrix
	double a[N][N+1] = {0.101, 2.304, 3.555, 1.183,
						-1.347, 3.712, 4.623, 2.137,
						-2.835, 1.072, 5.643, 3.035}; 
	// backup the augmented matrix to verify the solution
	double b[N][N+1] = {0.101, 2.304, 3.555, 1.183,
						-1.347, 3.712, 4.623, 2.137,
						-2.835, 1.072, 5.643, 3.035}; 
	// solution vector
	double x[N]; 

	// solve the equations
	gauss_method(a, x);

	// verify the solution
	int mark = verify_solution(b, x);
	if(mark)
		cout << "The vector is the solution of the original equations" << endl;
	else
		cout << "The vector is not the solution of the original equations" << endl;

	return 0;
}

/**
 * @brief Solve linear equations by Gaussian method
 * @param A: double [][N+1], the augmented matrix
 * @param x: double, the solution vector
 */
void gauss_method(double A[][N+1], double x[])
{
	double m;         // 中间变量
	int i, j, k;

	// 消元过程
	for (k = 0; k < N - 1; k++)
	{
		if (A[k][k] == 0)
		{
			cout << "求解失败!";
			break;
		}

		for (i = k+1; i < N; i++)
		{
			m = A[i][k] / A[k][k];
			A[i][k] = 0;
			for (j = k+1; j <= N; j++)
				A[i][j] = A[i][j] - A[k][j] * m;
		}
	}

	// 回代过程
	x[N-1] = A[N-1][N] / A[N-1][N-1];
	for (k = N-2; k >= 0; k--)
	{
		for (j = k+1; j < N; j++)
		{
			A[k][N] = A[k][N] - A[k][j] * x[j];
		}
		x[k] = A[k][N] / A[k][k];
	}

	// 输出结果
	cout.precision(9);
	for (k = 0; k < N; k++)
		cout << x[k] << endl;

}

/**
 * @brief Verify whether the vector is the solution of the linear equations
 * @param A: double [][N+1], the augmented matrix of the linear equations
 * @param x: double [], the vector to be verified.
 *
 * @Returns mark: int, if mark=1, the vector is the solution of the equations
 */
int verify_solution(double A[][N+1], double x[])
{
	int mark = 1;
	for (int i = 0; i < N; i++)
	{
		double s = 0;
		for (int j = 0; j < N; j++)
		{
			s += A[i][j] * x[j];
		}
		if(fabs(s - A[i][N]) > 1e-9)
		{
			mark = 0;
			break;
		}
	}

	return mark;
}

