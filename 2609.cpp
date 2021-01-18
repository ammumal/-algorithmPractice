#include <iostream>
using namespace std;

int main() {
    int a, b, c, d = 0;

    cin >> a >> b;

    // 공약수 구하기 (유클리드 호제법)
    while (b != 0){
        c = a % b;
        a = b;
        b = c;
    }

    cout << a << endl;


    // 공배수 구하기
    d = a * b;

    cout << d / a << endl;

    return 0;
}