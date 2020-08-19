#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int T;
    cin >> T;
    
    vector <string> S(T);
    
    for (int i=0;i<T;i++) {
        cin >> S[i];
    }
    
    for (int i=0;i<T;i++) {
        
        int l = S[i].length();
        
        for (int j=0;j<l;j=j+2) {
            cout << (char) S[i][j];
        }
        cout << " ";
        for (int k=1;k<l;k=k+2) {
            cout << (char) S[i][k];
        }
        cout << endl;
    }
    
    return 0;
    
}
