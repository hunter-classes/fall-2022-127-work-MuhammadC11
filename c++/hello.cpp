// this is just something we include at the start of every program
#include <iostream>

// this is the main function
int main()
{
    std::cout << "Hello, world!" // this is how to print to the screen
              << "\n";           // this is how to print a new line
    for (int i = 0; i < 5; i++)
    {
        std::cout << i << "\n";
    }
    return 0;
}