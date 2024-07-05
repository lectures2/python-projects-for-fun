#include <iostream>
#include <Windows.h>

// Game constants
const int MIN_NUMBER = 1;
const int MAX_NUMBER = 100;

// Function to generate a random number
int GenerateRandomNumber()
{
    return rand() % (MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER;
}

int main()
{
    // Generate random number
    srand(static_cast<unsigned>(time(0)));
    int targetNumber = GenerateRandomNumber();

    // Game loop
    int guess;
    do {
        std::cout << "Guess a number between " << MIN_NUMBER << " and " << MAX_NUMBER << ": ";
        std::cin >> guess;

        if (guess < targetNumber) {
            std::cout << "Too low. Try again!" << std::endl;
        }
        else if (guess > targetNumber) {
            std::cout << "Too high. Try again!" << std::endl;
        }
        else {
            std::cout << "Congratulations! You guessed the correct number." << std::endl;
        }

    } while (guess != targetNumber);

    // Wait for user input before closing the console window
    system("pause");

    return 0;
}
