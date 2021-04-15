#include <iostream>
#include <vector>

int main(void)
{
    int n;
    std::cin >> n;
    for (int i = 2; i * i <= n; ++i)
        while (n % i == 0)
        {
            std::cout << i << " ";
            n /= i;
        };
    return 0;
};
