#include <bits/stdc++.h>
#define FOR(i,j,k) for (int i = j; i < k; i++)
#define FORD(i,j,k) for (int i = j; i >= k; i--)
#define ll long long
//Make sure no overflow problems
#define pii pair<int, int>
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define VAR(i, n) __typeof(n) i = (n)
#define FOREACH(i, c) for (VAR(i,(c).begin()); i!=(c).end(); i++)
#define FORDEACH(i, c) for (VAR(i,(c).rbegin()), i != (c).rend(); i++)
#define REP(i, n) FOR(i, 0, n)
#define ld long double
#define INF 1000000009;
#define INFLL (ll)INF * (ll)INF;
#define EPS 10e-9;
using namespace std;
////////////////////////////////////////////////////////////////////////////////////////////////

string convert_to_roman(int n)
{
    vector<pair<string, int>> numerals = { 
        { "M", 1000 },
        { "CM", 900 },
        { "D", 500 },
        { "CD", 400 },
        { "C", 100 },
        { "XC", 90 },
        { "L", 50 },
        { "XL", 40 },
        { "X", 10 },
        { "IX", 9 },
        { "V", 5 },
        { "IV", 4 },
        { "I", 1 }
    };
    int numerals_idx = 0;
    string roman = "";

    while (n != 0)
    {
        if (n >= numerals[numerals_idx].second)
        {
            roman += numerals[numerals_idx].first;
            n -= numerals[numerals_idx].second;
        }
        else numerals_idx++;
    }
    return roman;
}

string look_and_say(string s)
{
    string applied = "";
    int current_count = 0;
    char current = s[0];
    FOREACH (c, s)
    {
        if (*c == current)
            current_count++;
        else
        {
            applied += convert_to_roman(current_count);
            applied += current;
            current = *c;
            current_count = 1;
        }
    }
    applied += convert_to_roman(current_count);
    applied += current;
    return applied;
}


void solve(string s, int n)
{
    string applied = s;
    FOR (i, 0, n)
        applied = look_and_say(applied);

    cout << count(applied.begin(), applied.end(), 'I') << " " << 
        count(applied.begin(), applied.end(), 'V') << endl;
}

void c_helper()
{
    set<string> distinct;
    FOR (i, 1, 4000)
        distinct.insert(look_and_say(convert_to_roman(i)));
    cout << distinct.size() << endl;
}

int main()
{
    // a
    string s;
    int n;
    cin >> s >> n;
    solve(s, n);                                              // 25/25
    // b
    // Answer can't be any number that is more than 10, 
    // as after that any look and say will start with I 
    // in the range 1-3999
    // So under ten only: I -> II, II -> III, X -> IX, V -> IV
    // Therefore 4 descriptions: II, III, IV, IX                 // 2/2
    // c
    // c_helper(); // ANS: 3919                                  // 4/4
}
