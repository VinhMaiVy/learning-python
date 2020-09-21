#!/bin/python3

"""

hackerhappy
hackerrank
9

Yes

aba
aba
7

Yes

y
yu
2

No

abcd
abcdert
10

No

"""

def appendAndDelete(s, t, k):
    result = 'No'
    ls = len(s)
    lt = len(t)    
    L = ls+lt
    
    for i in range(min(ls,lt)):
        if s[i] != t[i]:
            break
    
    if (L <= k+i*2) and (L%2 == k%2) or (L < k):    
        result = 'Yes'     
        
    return result

if __name__ == '__main__':
    
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result + '\n')
    
    
"""
#include <bits/stdc++.h>
using namespace std;
#define L (s.size() + t.size())

int main(){
    string s, t;
    int k, i;
    cin >> s >> t >> k;
    for(i = 0; s[i] == t[i]; i++);
    cout << (L <= k + i*2 && L%2 == k%2 || L < k ? "Yes" : "No");
    return 0;
}
"""
