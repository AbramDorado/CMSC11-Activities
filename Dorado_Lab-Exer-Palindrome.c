#include <stdio.h>
#include <string.h>

int main()
{    //variable declaration
    char s[100];   //max character for the string
    int i;
    int n;
    int c=0;

    printf("Enter a string> ");
    scanf("%s", s);

    n = strlen(s);
    //for loop to calculate for the palindrome
    for(i=0; i<n; i++)
    {
        if (s[i] > 64 && s[i] < 91) //if statement to convert upper case to lower case and vice versa
            {
                s[i] = s[i] + 32; //the difference between uppercase and lowercase in ASCII table
            }

    	if(s[i] == s[n-i-1])  //comparing the value of string
    	c++;   //value will be compared to i
 	}

    //if statement to tell if ppalindrome or not
 	if(c==i)       // if c is equal to i then it is palindrome
 	    printf("string is palindrome");
    else
        printf("string is not palindrome");

    return 0;
}
