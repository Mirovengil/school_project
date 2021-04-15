#include <iostream>
#include <vector>

void clear(int &length)
{
    length = 0;
};

void add(int *mass, int &length, int value)
{
    mass[length] = value;
    length += 1;
};

int get(int *mass, int length)
{
    if (length == 0)
        exit(1); //Аварийный выход из функции
    return mass[length - 1];
}; 

void del(int &length)
{
    length -= 1;
    if (length < 0)
        length = 0;
};

int main(void)
{
    int mass[100];
    int length;
    clear(length);
    add(mass, length, 1);
    add(mass, length, 2);
    add(mass, length, 3);
    for (int i = 0; i < 3; ++i)
    {
        std::cout << get(mass, length) << " ";
        del(length);
    };
    return 0;
};
