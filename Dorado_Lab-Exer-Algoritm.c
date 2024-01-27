#include <stdio.h>

//the 4 sorting algorithm functions
void insertion_sort(int input_array[], int size);
void selection_sort(int input_array[], int size);
void bubble_sort(int input_array[], int size);
void merge_sort(int input_array[], int l, int r);

int main(void) //the main function program
{
    //insertion sort
    int i, n = 6;    //variables used, array size 6
    int arr[] = {8, 20, 5, 45, 3, 62};  //list of array
    printf("Insertion Sort\n");  //print the label of sorting algorithm
    print_before(arr, n);  //function call to the print for the list of array before sorted
    insertion_sort(arr, n); //function call to the specific sorting algorithm
    print_after(arr, n);   //function call to the print for the list of array after sorted

    //selection sort
    int a, b = 6;   //variables used, array size 6
    int arr2[] = {2, 19, 12, 8, 20, 4};  //each sorting alorithm has its own variable and array name
    printf("Selection Sort\n");
    print_before(arr2, b);
    selection_sort(arr2, b);
    print_after(arr2, b);

    //bubble sort
    int x, y = 6;
    int arr3[] = {66, 71, 40, 39, 1, 52};
    printf("Bubble Sort\n");
    print_before(arr3, y);
    bubble_sort(arr3, y);
    print_after(arr3, y);

    //merge sort
    int c, d = 6;
    int arr4[] = {22, 16, 35, 75, 29, 9};
    int size = sizeof(arr4) / sizeof(arr4[0]);
    printf("Merge Sort\n");
    print_before(arr4, d);
    merge_sort(arr4, 0, size - 1);
    print_after(arr4, d);
}

//function to print the array berore soting
void print_before(int arr[], int size)
{
    int i;
    printf("Before sorting: ");
    for(i = 0; i < size; i++)  //for loop was used
        printf("%i ", arr[i]);
    printf("\n");
}

//funtion to print the array after sorting
void print_after(int arr[], int size)
{
    int i;
    printf("After sorting: ");
    for(i = 0; i < size; i++)  //for loop was used
        printf("%i ", arr[i]);
    printf("\n\n");
}

//insertion sort function
void insertion_sort(int input_array[], int size)
{
    int i, j; //variable
    //for i from 1 to size-1
    for(i=1; i<=size-1; i++)
    {
        //Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        for(j=i; j>0; j--) //remove i'th element insert it into sorted side in order
            if(input_array[j - 1] > input_array[j]) //if statement to switch if coditions met
    	    {
            //swaping of the values
            int temp = input_array[j-1];  //assign input_array[j-1] to temp
            input_array[j-1] = input_array[j]; //assign input_array[j] to input_array[j-1]
            input_array[j] = temp; //assign temp to input_array[j]
    	    }
    }
}


//selection sort function
void selection_sort(int input_array[], int size)
{
    int i, j; //variable
    for(i = 0; i < size-1; i++) //One by one move boundary of unsorted subarraym
    {
        int smallest_index = i;
        for(j = i+1; j < size; j++) //finding the minimum element in the array
        {
            if(input_array[smallest_index] > input_array[j]) //if statement to switch if coditions met
            {
                smallest_index = j; //update the value of index
            }
            //swaping of the values
            int temp = input_array[smallest_index]; //assign input_array[smallest_index] to temp
            input_array[smallest_index] = input_array[i]; //assign input_array[i] to input_array[smallest_index]
            input_array[i] = temp; //assign temp to input_array[i]
        }
    }
}

//bubble sort function
void bubble_sort(int input_array[], int size)
{
    int i, j; //variable
    for (i = 0; i < size-1; i++) //loop to access each array
    {
        for (j = 0; j < size-i-1; j++) //loop to compare array
        {
            if (input_array[j] > input_array[j+1]) //if statement to switch if coditions met
           {
            //swaping of the values
            int temp = input_array[j]; //assign input_array[j] to temp
            input_array[j] = input_array[j+1]; //assign input_array[j] to input_array[j+i]
            input_array[j+1] = temp; //assign temp to input_array[j+1]
           }
        }
    }
}

//merge sort function
void merge(int input_array[], int p, int q, int r)
// Merges two subarrays of arr[]. First subarray is arr[l..m], Second subarray is arr[m+1..r]
{
    //variables
    int n1 = q - p + 1;
    int n2 = r - q;
    int L[n1], M[n2];

    for (int i = 0; i < n1; i++){ //Copy data to temp arrays L[] and R[]
        L[i] = input_array[p + i];
    }
    for (int j = 0; j < n2; j++){
        M[j] = input_array[q + 1 + j];
    }
    //Merge the temp arrays back into arr[l..r]
    int i, j, k;
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = p; // Initial index of merged subarray

    while (i < n1 && j < n2){
        if (L[i] <= M[j]){
        input_array[k] = L[i];
        i++;
        }
        else{
        input_array[k] = M[j];
        j++;
        }
        k++;
        }

    while (i < n1){ //Copy the remaining elements of L[]
        input_array[k] = L[i];
        i++;
        k++;
        }

    while (j < n2){ //opy the remaining elements of R[]
        input_array[k] = M[j];
        j++;
        k++;
        }
}

// a function to merge the sub arrays
void merge_sort(int input_array[], int l, int r) //l is for left index and r is right index of the sub-array of arr to be sorted
{
  if (l < r){  // Same as (l+r)/2, but avoids overflow for large l and h
    int m = l + (r - l) / 2;

    // Sorting the two parts
    merge_sort(input_array, l, m);
    merge_sort(input_array, m + 1, r);

    merge(input_array, l, m, r);
    }
}
