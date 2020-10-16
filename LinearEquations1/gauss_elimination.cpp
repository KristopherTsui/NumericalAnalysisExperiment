#include<iostream>
#include<cmath>

#define N 3 

using namespace std;

int main()
{
	double a[N][N+1] = {0.101, 2.304, 3.555, 1.183,
						-1.347, 3.712, 4.623, 2.137,
						-2.835, 1.072, 5.643, 3.035}; // 增广矩阵
	double x[N];                                       // 存储解向量
	double m;                                          // 中间变量
	int i, j, k;

	// 消元过程
	for (k = 0; k < N - 1; k++)
	{
		// k < N - 1 ?
		if (a[k][k] == 0)
		{
			cout << "求解失败!";
			break;
		}

		for (i = k+1; i < N; i++)
		{
			m = a[i][k] / a[k][k];
			a[i][k] = 0;
			for (j = k+1; j <= N; j++)
				// j<=N?
				a[i][j] = a[i][j] - a[k][j] * m;
		}
	}

	// 回代过程
	x[N-1] = a[N-1][N] / a[N-1][N-1];
	for (k = N-2; k >= 0; k--)
	{
		for (j = k+1; j < N; j++)
		{
			a[k][N] = a[k][N] - a[k][j] * x[j];
		}
		x[k] = a[k][N] / a[k][k];
	}

	// 输出结果
	for (k = 0; k < N; k++)
		cout << x[k] << endl;

	// 验证所得到的解向量是否是原方程的解
	int mark = 1;
	for (i = 0; i < N; i++)
	{
		double s = 0;
		for (j = 0; j < N; j++)
			s += a[i][j] * x[j];
		if(fabs(s - a[i][N]) >= 1e-9)
		{
			mark = 0;
			break;
		}
	}
	if(mark)
		cout << "The vector is the solution of the original equations" << endl;
	else
		cout << "The vector is not the solution of the original equations" << endl;

	return 0;
}

