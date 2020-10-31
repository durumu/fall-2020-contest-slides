#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int n;
	cin >> n;
	int mx = -1;
	int mn = 1e7;
	int r;
	for (int i=0;i<n;i++)
	{
		cin >> r;
		mx = max(mx,r);
		mn = min(mn,r);
	}
	double ans = (double)mx/mn;
	printf("%.7f\n",ans);
	printf("2 %d %d\n",mn,mx);
	return 0;
}
	