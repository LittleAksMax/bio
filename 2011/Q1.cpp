#include <iostream>

void solve(char c1, char c2, int n)
{
    // tabulation
    int *dp = new int[n];
    dp[0] = c1 - 'A' + 1;
    dp[1] = c2 - 'A' + 1;
    for (int i = 2; i < n; i++) dp[i] = 0;
    for (int i = 2; i < n; i++)
    {
        dp[i] = (dp[i - 1] + dp[i - 2]);
        if (dp[i] > 26) dp[i] -= 26;
    }
    std::cout << (char)(dp[n - 1] + 'A' - 1) << std::endl;
}

void b_helper()
{
    for (int i = 0; i < 26; i++)
        if (('F' - 'A' + i) % 26 + 'A' == 'X')
            std::cout << (char)(i + 'A' - 1) << std::endl;
    for (int i = 0; i < 26; i++)
        if (('Q' - 'A' + i) % 26 + 'A' == 'H')
            std::cout << (char)(i + 'A' - 1) << std::endl;
}

void c_helper()
{
    // C C repeats for 85 and 86
    // for (int i = 1; i <= 100; i++)
    // {
    //     std::cout << i;
    //     solve('C', 'C', i);
    //     std::cout << std::endl;
    // }
    // 10^18 MOD 84 = 64
    // so the answer should be a solve for C C where n = 64
    solve('C', 'C', 64);
}

int main()
{
    // b_helper();         // R, Q 3/3
    // return 0;
    // c_helper();         // K 3/3
    // return 0;
    char c1, c2;
    int n;
    std::cin >> c1 >> c2 >> n;
    solve(c1, c2, n);   // 24/24
}