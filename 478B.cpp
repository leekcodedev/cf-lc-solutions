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
  //return min possible and max possible friends made
  ll m,n;
  cin >> n >> m;
  ll maxInGroup = n - (m-1);
  ll minInGroup = n / m;
  int rem = n % m;
  auto largestPossible = (maxInGroup*(maxInGroup-1))/2;
  auto smallestPossible = (m-rem)*(minInGroup*(minInGroup-1)/2) + rem*((minInGroup)*(minInGroup+1)/2);
  cout << smallestPossible << " " << largestPossible;
  ret;
}
