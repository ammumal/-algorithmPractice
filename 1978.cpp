#include <iostream>
using namespace std;

int main() {

    int size, input = 0;

    cin >> size;

    //출력을 위해 count 선언
    int count = size;

    //size가 100 이상일 경우 종료
    if(size < 1 || size > 100) {
        cout << "error" << endl;
        return 0;
    }

    for(int i = 0; i < size; i++) {

        //input을 입력받는다
        cin >> input;

        //input이 1일경우 count 1 감소(1은 소수 아님)
        if(input == 1) {
            count --;
        }
        else {
            //input이 2 이상일 경우 input까지 for문
            for(int j = 2; j < input; j++) {
                //나누어 떨어지는 수가 있으면 count 1 감소
                if(input % j == 0) {
                    count --;
                    break;
                }
            }
        }
    }
    cout << count << endl;
    
    return 0;
}