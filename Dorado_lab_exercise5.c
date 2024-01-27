#include <stdio.h>

/************
1. Write a function that finds the index of the largest number in an array.
int findMax(int *anArray, int aSize)
*************/
int findMax(int *anArray, int aSize)
{
    int i;
    //Assume that the max element is located at index 0.
    int max_index = 0;
    //For each element in anArr[1,...,n-1], check if the anArr[i] is larger than the current max.
    for(i = 1; i < aSize; i++)
    {
        //if the current max is smaller than anArray[i]
        if(anArray[max_index] < anArray[i])
        {
            //update the index
            max_index = i;
        }
    }

    return max_index;
}

/**************
2. Write a function that swaps the two selected elements of an array.
void switchPlaces(int *anArray, int aSize, int aFirstEl, int aSecondEl)
***************/
void switchPlaces(int *anArray, int aSize, int aFirstEl, int aSecondEl)
{
    //given an array of size 5, the chosen element is index 0 and index(aSize - 1) or the last index
    int temp;
        // swap to first element/index 0 to a temp variable
        temp = anArray[aFirstEl];
        // swap second element/last index(aSize - 1) to first element/index 0
        anArray[aFirstEl] = anArray[aSize - aSecondEl];
        // swap temp variable to second element/last index
        anArray[aSize - aSecondEl] = temp;
}

/*************
3. Write a recursive function that sorts array into smallest to largest.
void sortArray(int *anArray, int aSize)
************/
void sortArray(int *anArray, int aSize)
{
    // recursive insertion sort
    // Base case asize if less than or equal to 1
    if (aSize <= 1)
        return;

    // call the function
    // Sort first n-1 elements
    sortArray(anArray, aSize-1);

    // Insert last element at its correct position in sorted array.
    int last = anArray[aSize-1];
    int i = aSize-2;

    // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
    while (i >= 0 && anArray[i] > last)
    {
        anArray[i+1] = anArray[i];
        i--;
    }
    anArray[i+1] = last;
}

/****
4. Write a boolean function that checks if all characters are unique (must be
case insensitive)
***/
int UniqueString(char* aString)
{
    char s[500];

    // If at any time we encounter 2 same characters, return false
    for (int i = 0; i < strlen(s) - 1; i++)
        {
        for (int j = i + 1; j < strlen(s); j++)
        {
            if (s[i] > 64 && s[i] < 91) //if statement to convert upper case to lower case and vice versa
            {
                s[i] = s[i] + 32; //the difference between uppercase and lowercase in ASCII table
            }
            if (aString[i] == aString[j]) // compare strings
            {
                return 0;
            }
        }
    }

    // If no duplicate characters encountered return true
    return 1;
}

/******
5. Write a function that searches for a value and returns the index of the number if it exists,
-1 if it does not exist.
*****/
int findInArray(int *anArray, int aSize, int Element)
{
    int i;
    // linear search to find the array
    for (i = 0; i < aSize; i++)
    {
        if (anArray[i] == Elements) //check if present
        {
            return i;
        }
    }
    return -1; // -1 if no. not exists in an array
}

/******
6. Write a function that takes a string as its argument and returns a new string with all doubled letters
in the string replaced by a single letter.

"Tressider" -> "Tresider"
"Tresidder" -> "Tresider"
"Bedridden" -> "Bedriden"
"Bookkeeper" -> "Bokeper"

*****/
char *removeDoubleLetters(char *in)
{
    int n;
    int index = 0; // Used as index in the modified string

    int i;
    for (i = 0; i < n; i++) // Traverse through all characters
    {
        // Check if in[i] is present before it
        int j;
        for (j = 0; j < i; j++)
            if (*in[i] == *in[j])
            break;

        // If not present, then add it to result.
        if (j == i)
            *in[index++] = *in[i];
   }
   return *in;
}





