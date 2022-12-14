// this is just something we include at the start of every program
#include <iostream>

int max(int a, int b)
{
    for (int i = 5; i > 0; i--)
    {
        std::cout << "program starts in " << i << "\n";
    }
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int main()
{
    int a = 5;
    int b = 10;
    int largest = max(a, b);
    std::cout << "the largest number between " << a << " and " << b << " is " << largest << "\n";
    return 0;
}