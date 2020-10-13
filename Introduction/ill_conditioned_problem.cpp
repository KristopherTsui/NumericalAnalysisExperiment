#include<iostream>

using namespace std;

/* function statements */
void solve_binary_linear_equations(double [][2], double [], double []);
double determinant(double [2][2]);
void print_solution(double [][2], double [], double, int);

int main()
{
	// initial value
	double a[2] = {0.99, 0.991};
	double A1[2][2] = {{1, a[0]}, {a[0], 1}};
	double A2[2][2] = {{1, a[1]}, {a[1], 1}};
	double A3[2][2] = {{1, a[0]}, {a[0], 4}};
	double A4[2][2] = {{1, a[1]}, {a[1], 4}};
	double b[2] = {1, 0};

	// output
	print_solution(A1, b, a[0], 0);
	print_solution(A2, b, a[1], 0);
	print_solution(A3, b, a[0], 1);
	print_solution(A4, b, a[1], 1);

	return 0;
}

/**
 * @brief Solve binary linear equations by Cramer rule 
 * @param A: double[][], the coefficient matrix
 * @param b: double[], the matrix b
 */
void solve_binary_linear_equations(double A[][2], double b[], double x[])
{
	// swap the first or second column with b
	double D1[][2] = {{b[0], A[0][1]}, {b[1], A[1][1]}};
	double D2[][2] = {{A[0][0], b[0]}, {A[1][0], b[1]}};

	// calculate the determinant of A, D1 and D2
	double D = determinant(A);
	double det_D1 = determinant(D1);
	double det_D2 = determinant(D2);

	// calculate the solution by Cramer rule
	x[0] = det_D1 / D;
	x[1] = det_D2 / D;
}

/**
 * @brief Calculate the two order determinant
 * @param A: double[][], the matrix
 *
 * @Returns double, the determinant of the matrix A
 */
double determinant(double A[2][2])
{
	return A[0][0] * A[1][1] - A[0][1] * A[1][0];
}


/**
 * @brief Print the solution of the first or second equations with some a
 * @param A: double[][], the coefficient matrix
 * @param b: double[], the matrix b
 * @param a: double, the value of the parameter in the cofficient matrix
 * @param flag: int, if flag = 0, the output is the solution of the first equations;
 * 					 if flag = 1, the output is the solution of the second equations.
 */
void print_solution(double A[][2], double b[], double a, int flag)
{
	// define the solution variable
	double x[2];

	// solve the equations
	solve_binary_linear_equations(A, b, x);

	// output
	if (flag == 0)
	{
		cout << "The solution of the first euqations with a = " << a; 
		cout << " is x1 = " << x[0] << " and x2 = " << x[1] << endl;
	}
	else
	{
		cout << "The solution of the second euqations with a = " << a; 
		cout << " is x1 = " << x[0] << " and x2 = " << x[1] << endl;
	}
}

