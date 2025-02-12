#include <bits/stdc++.h>
using namespace std;
#define fast() { ios::sync_with_stdio(0);cin.tie(0);}
#define SETUP_IO \
  freopen("input.txt", "r", stdin); \
  freopen("output.txt", "w", stdout);
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define vi vector<int>
#define vll vector<long long>
#define pb push_back
#define ll long long 
#define ret return 0
#define sort(a) sort(a.begin(),a.end()); 

int main(){
  #ifdef LOCAL
  SETUP_IO
  #endif
  fast(); 
  int n,a,b;
  cin >> n;
  while(n--) {
    cin >> a >> b;
    if(a < b) cout << "NO" << '\n';
    else if(a == b) {
      cout << "YES\n";
      rep(i,a) {
        cout << "1 ";
      }
      cout << '\n';
    }
    else if (a%2 == 1){
      if(b%2 == 0) {
        cout << "NO" << '\n';
      }
      else {
        cout << "YES\n";
        rep(i,b-1) {
          cout << "1 ";
        } 
        cout << a-(b-1) << '\n';
      }
    }
    else {
      if((a/2) < b) {
        if(b % 2 == 1 ) {
          cout << "NO\n";
        }
        else {
          cout << "YES\n";
          rep(i,b-1) {
            cout << "1 ";
          }
          cout << a-(b-1) << '\n';
        }
      }
      else if(b == 1){
        cout << "YES\n" << a << '\n';
      }
      else {
        cout << "YES" << '\n';
        rep(i,b-1) {
          cout << "2 ";
        } 
        cout << a-(2*(b-1)) << '\n';
      }
    }
  }
  ret;
}
