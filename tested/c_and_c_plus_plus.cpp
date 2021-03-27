#include <iostream>
#include <vector>

int main(void)
{
    int mass[5] = {1, 2, 3, 4, 5};
    int mass2[5];
    int move = 2;
    int n = 5;
    std::cin >> move;
    
    
    move = move % n;
    for (int i = 0; i < n; ++i)
    {
        int new_i = (i + move + n) % n;
        mass2[new_i] = mass[i];
    };
    
    for (int i = 0; i < n; ++i)
        std::cout << mass2[i] << " ";
    
    return 0;
};
