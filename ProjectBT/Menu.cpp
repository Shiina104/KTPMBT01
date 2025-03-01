#include <iostream>
using namespace std;

bool checkSNT(int x)
{
	for (int i = 2; i < sqrt(x)+1; i++)
	{
		if (x % i == 0)
			return false;
	}
	return true;
}

int main()
{
	int x, chon;
	do
	{
		cout << "Menu:\n"
			"1. Check SNT\n"
			"2. Kiem tra nam nhuan\n"
			"3. Thoat menu\n";
		cout << "Ban chon: ";
		cin >> chon;
		system("cls");

		if (chon != 3)
		{
			cout << "Nhap so x: ";
			cin >> x;
		}
		switch (chon)
		{
		case 1:
			if (checkSNT(x))
				cout << x << " la so nguyen to\n";
			else
				cout << x << " ko phai la so nguyen to\n";
			break;
		case 2:
			cout << "Chua lam\n";
			break;
		default:
			break;
		}
		system("pause");
		system("cls");
	} while (chon != 3);
	return 0;
}