using System;
using System.Collections.Generic;

public class Solution
{
    public int Solve(int n)
    {
        if (n == -1) return -1;
        
        var primes = new HashSet<int>();
        if ((n & 1) == 0) primes.Add(2);
        while ((n & 1) == 0) n >>= 1;
        for (var i = 3; i <= n; i += 2)
            if (IsPrime(i))
                if (n % i == 0)
                {
                    primes.Add(i);
                    while (n % i == 0)
                        n /= i;
                }

        var product = 1;
        foreach (int prime in primes)
            product *= prime;
        Console.WriteLine(product);
        return product;
    }

    private bool IsPrime(int n)
    {
        int limit = (int)Math.Sqrt((double) n);
        for (var i = 3; i < limit; i += 2)
            if (n % i == 0)
                return false;
        return true;
    }
}

public static class Q1
{
    private static void BHelper(Solution solution)
    {
        int[] lowest = new int[10];
        int i = 0;
        int n = 1;
        while (true)
        {
            if (i == 10) break;
            int sol = solution.Solve(n);
            if (solution.Solve(n) == 10)
                lowest[i++] = n;
            n++;
        }
        foreach (int num in lowest)
            Console.Write(num + " ");
        Console.WriteLine();
    }

    private static void CHelper(Solution solution)
    {
        var dict = new Dictionary<int, int>();
        for (int i = 2; i < 1000000; i += 2)
        {
            if (i % 3 != 0) continue;
            
            int sol = solution.Solve(i);
            if (dict.ContainsKey(sol)) dict[sol]++;
            else dict.Add(sol, 1);
        }

        KeyValuePair<int, int> frequent = new KeyValuePair<int, int>(-1, -1);
        foreach (var pair in dict)
        {
            if (pair.Value > frequent.Value)
            {
                frequent = pair;
            }
        }
        Console.WriteLine(frequent.Key);
    }
    
    public static void Main(string[] args)
    {
        var solution = new Solution();
        solution.Solve(int.Parse(Console.ReadLine() ?? "-1")); // 24/24
        // BHelper(solution);                                    // 2/2
        // CHelper(solution);                                    // 4/4
    }
}

// MARKS: 30/30
