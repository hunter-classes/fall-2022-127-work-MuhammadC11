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
    int largest = max(5, 10);
    std::cout << "the largest number is " << largest << "\n\n";
    return 0;
}