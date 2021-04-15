#include <iostream>
#include <vector>

int main(void)
{
    int n;
    std::cin >> n;
    int mass[n];
    for (int i = 0; i < n; ++i)
        std::cin >> mass[i];
    
    for (int i = 0; i < n / 2; ++i)
    {
        int temp = mass[i];
        mass[i] = mass[n - 1 - i];
        mass[n - 1 - i] = temp;
    };
    
    for (int i = 0; i < n; ++i)
        std::cout << mass[i] << " ";
    return 0;
};
