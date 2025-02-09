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

  int t,n;
  ll res,val,smolNeg,bigPos;
  cin >> t;
  bool flag = false;
  while(t--) {
    cin >> n;
    res = 0;
    rep(i,n) {
      cin >> val;
      if(n == 1) {
        res = val;
        break;
      }
      if(i == 0) {
        if(val > 0) {
          flag = true;
          bigPos = val;
        }
        else {
          flag = false;
          smolNeg = val;
        }
      }
      else {
        if(val > 0) {
          if(flag) {
            bigPos = max(bigPos,val);
          }
          else {
            res += smolNeg;
            bigPos = val;
            flag = true;
          }
          if(i == n-1) {
            res += bigPos;
          }
        } 
        else {
          if(!flag) {
            smolNeg = max(smolNeg,val);
          } 
          else {
            res += bigPos;
            smolNeg = val;
            flag = false; 
          }
          if(i == n-1) {
            res += smolNeg;
          }
        }
      }
    }
    cout << res << '\n';
  }
  ret;
}
