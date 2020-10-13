#include<iostream>
#include<iomanip>
#define N 0.1234567890123456789

using namespace std;


int main()
{
	// section 1
	float ff = N;
	double df = N;
	cout.precision(20);
	cout << "The single precision floating point number ff is " << ff << endl;
	cout << "The double precision floating point number df is " << df << endl;

	// section 2
	float a1 = 1.000001;
	float a2 = 1.000000;
	float a3 = 0.0000001;
	// method 1
	float s1 = a1;
	for(int i = 0; i < 100; i++)
	{
		s1 += a3;
	}
	// method 2
	float s2 = 0;
	for(int i = 0; i < 100; i++)
	{
		s2 += a3;
	}
	// output
	cout.precision(10);
	cout << "The answer of adding 100 a3 to a1 by method1 is " << s1 << endl;
	cout << "The answer of adding 100 a3 to a1 by method2 is " << a1 + s2 << endl;

	cout << "a1/a3 + a2 = " << a1/a3 + a2 << endl;

	cout << "a1 - a2 = " << a1 - a2 << endl;
	return 0;
}
