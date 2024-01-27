#include <stdio.h>

int main (void)
{
    double terms;        //variable for the number of terms the user will input
    double value = 0;    //value of Pi
    int c = 1;           //variable to change the operation in the sequence
    double i;            //variable for the denominator that will change in the sequence in for loop

    int number = 0;      //only for numbering in the left side
    int whole = 4;       //variable for the whole number 4 to not have a decimal


    printf("Enter the number of terms to be used: ");
    scanf("%lf", &terms);

    for (i = 1; i < (terms * 2); i += 2)   //for loop to continue the sequence for the value of Pi
    {
        value = value + c*(4/i);           //formula
        c = - c;                           //change in operation every next loop
        number = number + 1;               //add 1 to the numbering on the left side for every next term


        if (value < whole)                                 //if statement so that the whole number "4" will not have a decimal
        {
            printf("%i       %.5lf\n", number, value);    //for the decimal values to only have up to 5 decimal places, and print the numbering and Pi
        }
        else
        {
            printf("%i       %.0lf\n", number, value);    //for the whole number "4" to not have a decimal of .000.., and print the numbering and Pi
        }
    }
     printf("\n\n\nHappy Teacher's Day Sir. Jermaine :)\n");
}
