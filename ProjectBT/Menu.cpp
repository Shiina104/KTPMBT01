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

bool checkNamNhuan(int nam)
{
	if (nam % 4 == 0 && nam % 100 != 0)
		return true;
	if (nam % 400 == 0)
		return true;
	return false;
}

int main()
{
	int x, chon;
	do
	{
		cout << "Menu dau tien:\n"
			"1. Check SNT\n"
			"2. Kiem tra nam nhuan\n"
			"3. Thoat menu\n";
		cout << "Ban chon: ";
		cin >> chon;
		system("cls");

		switch (chon)
		{
		case 1:
			cout << "Nhap so x: ";
			cin >> x;
			if (checkSNT(x))
				cout << x << " la so nguyen to\n";
			else
				cout << x << " ko phai la so nguyen to\n";
			break;
		case 2:
			cout << "Nhap nam: ";
			cin >> x;
			if (checkNamNhuan(x))
				cout << x << " la nam nhuan\n";
			else
				cout << x << " ko phai la nam nhuan\n";
			break;
		default:
			break;
		}
		system("pause");
		system("cls");
	} while (chon != 3);
	return 0;
}