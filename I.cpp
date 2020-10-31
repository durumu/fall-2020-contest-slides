#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int n,m,d;
	cin >> n >> m >> d;
	vector<int> h(n),p(n),t(n),s(m), count(m);
	for (int i =0;i<n;i++) cin >> h[i];
	for (int i =0;i<n;i++) cin >> p[i];
	for (int i =0;i<n;i++) 
	{
		cin >> t[i];
		t[i] -= 1;
		count[t[i]] +=1;
	}
	for (int i =0;i<m;i++) cin >> s[i];

	// Preprocessing to put the array in order
	vector<pair<int,pair<int,int>>> b(n);
	for (int i =0;i<n;i++)
	{
		b[i] = make_pair(t[i],make_pair(h[i],p[i]));
	}
	sort(b.begin(),b.end());

	vector<pair<int,int>> a;
	vector<int> jump;
	
	a.push_back(make_pair(0,0));
	jump.push_back(0);
	
	int lastType = 0;
	int sumHappiness = 0;
	for (int i =0;i<n;i++)
	{
		int type = b[i].first;
		int happiness = b[i].second.first;
		int price = b[i].second.second;
		if (type != lastType)
		{
			a.push_back(make_pair(sumHappiness,s[lastType]));
			jump.push_back(count[lastType]+1);
			sumHappiness = 0;
			lastType = type;
		}
		a.push_back(make_pair(happiness,price));
		jump.push_back(1);
		sumHappiness += happiness;
	}
	a.push_back(make_pair(sumHappiness,s[lastType]));
	jump.push_back(count[lastType]+1);


	// DP
	vector<vector<int>> dp(a.size(),vector<int>(d+1));
	for (int i=0;i<a.size();i++)
	{
		for (int j=1;j<=d;j++) dp[i][j] = -1;
		dp[i][0] = 0;
	}
	int res = 0;

	for (int i =1;i<a.size();i++)
	{
		int k = i - jump[i];
		int happiness = a[i].first;
		int price = a[i].second;
				
		for (int j =0;j <= d;j++)
		{		
			dp[i][j] = dp[i-1][j];
			if (j-price>=0 && dp[k][j-price]!=-1)
			{
				dp[i][j] = max(dp[i][j],dp[k][j-price] + happiness);
			}
			res = max(res, dp[i][j]);
		}
	}
	cout << res << endl;
}