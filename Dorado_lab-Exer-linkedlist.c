#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data; //value to store
    struct node *next; //pointer to the next node
} node;

/* Function Prototypes */
node* createNode(int data);
void printList(node* linked_list);
node* insertAtEnd(node* linked_list, int value);
node* insertAtFront(node* linked_list, int value);
node* deleteAtEnd(node* linked_list);
node* deleteAtFront(node* linked_list);
int viewFront(node* linked_list); //returns the value at the front
int viewEnd(node* linked_list); //returns the value at the end
int lengthList(node* linked_list);
void attemptingSplit(node* source, node** aList, node** bList);

int main(void)
{
    //create an empty list
    node* linked_list = NULL;
    node* a_list = NULL;
    node* b_list = NULL;
    int i;

    for(i = 1; i <= 5; i++)
    {
        linked_list = insertAtEnd(linked_list, i);
    }

    int list_size = lengthList(linked_list);
    printf("The size of the list is %i\n\n", list_size);

    printf("Original list: \n");
    printList(linked_list);

    attemptingSplit(linked_list, &a_list, &b_list);

    printf("a_list: \n");
    printList(a_list); // 1 -> 3 -> 5 -> NULL

    printf("b_list: \n");
    printList(b_list); // 2 -> 4 -> NULL

    return 0;
}

node* createNode(int data)
{
    //create a node with value specified by the argument data and return it
    node* new_node = malloc(sizeof(node));
    //add the contents
    new_node->data = data;
    //(*new_node).next = NULL;
    new_node->next = NULL;

    return new_node;
}

node* insertAtFront(node* linked_list, int value)
{
    //create a node
    node* new_node = createNode(value);
    //if the list is empty
    if(linked_list == NULL)
    {
        //set linked_list = new_node
        linked_list = new_node;
    }
    //if the list is not empty
    else
    {
        new_node->next = linked_list;
        linked_list = new_node;
    }
    return linked_list;
}


node* insertAtEnd(node* linked_list, int value)
{
    //create a node
    node* new_node = createNode(value);
    //if the list is empty
    if(linked_list == NULL)
    {
        //set linked_list = new_node
        linked_list = new_node;
    }
    //if the list is not empty
    else
    {
        node* counter = linked_list;
        //traverse/move towards the end of the list.
        while(counter->next != NULL)
        {
            counter = counter->next;
        }
        //assuming that the counter now contains the last element of the list
        counter->next = new_node;
    }

    return linked_list;
}

//Implementation using Pass-by-Reference
//void deleteAtEnd(node **linked_list);
//function call deleteAtEnd(&linked_list);

node* deleteAtEnd(node* linked_list)
{
    //if the list is empty
    if(linked_list == NULL)
    {
        printf("Empty list! No elements to delete\n");

    }
    //if the list is not empty
    else
    {
        node* counter = linked_list;
        //we traverse the list until we reach the second to the last element of the list.
        while(counter->next->next != NULL)
        {
            counter = counter->next;
        }

        node* formerEnd = counter->next;
        counter->next = NULL;
        free(formerEnd);
    }
    //return the modified list
    return linked_list;
}

node* deleteAtFront(node* linked_list)
{
    //if the list is empty
    if(linked_list == NULL)
    {
        printf("Empty list! No elements to delete\n");

    }
    //if the list is not empty
    else
    {
        //set counter as the start of the list
        node* counter = linked_list;
        //set the linked_list be the same as counter->next
        linked_list = counter->next;
        //set the counter->next as NULL
        counter->next = NULL;
        //free the counter
        free(counter);
    }

    //return the modified list
    return linked_list;
}


void printList(node* linked_list)
{
    //if the list is empty
    if(linked_list == NULL)
    {
        printf("Empty list!\n");
    }
    //if the list is not empty
    else
    {
        node* counter = linked_list;
        while(counter != NULL)
        {
            printf("%i ", counter->data); //prints out the value of the current node
            counter = counter->next; //update the node

            printf("-> ");

        }
        printf("NULL");
        printf("\n\n");
    }
}

int lengthList(node* linked_list)
{
    /*Returns the size of the linked list.*/
    int count = 0;
    node* counter = linked_list;

    //traverse the linked list
    while(counter != NULL)
    {
        //increment the count by 1
        count++;
        //we update the counter = counter->next
        counter = counter->next;
    }

    return count;

}

int viewFront(node* linked_list)
{
    //if the list is empty
    if(linked_list == NULL)
    {
        return -1; //indicates that the list is empty.
    }
    //if the list is not empty
    else
    {
        node* counter = linked_list;
        return counter->data;
    }
}

int viewEnd(node* linked_list)
{
    //if the list is empty
    if(linked_list == NULL)
    {
        return -1; //indicates that the list is empty.
    }
    else
    {
        //perform traversal
        node* counter = linked_list;
        while(counter->next !=NULL)
        {
            counter = counter->next;
        }

        return counter->data;
    }
}

// moves the node from the front of the source to the front of the destination
void move_node(node** destination, node** source)
{
    // if the list is empty
    if (*source == NULL)
    {
        return -1; //indicates that the list is empty.
    }
    else
    {
    node* new_node = *source;  // the front source node
    *source = (*source)->next;    // move forward the source pointer
    new_node->next = *destination;  // link the old destination off the new node
    *destination = new_node;        // move destination to the new node
    }
}

void attemptingSplit(node* source, node** aList, node** bList)
{
    node x; // use a another pointer
    node* aLast = &x;  // points to the last node in a
    x.next = NULL;   //set to null

    node y;
    node* bLast = &y;  // points to the last node in b
    y.next = NULL;

    node* current = source;

    while (current != NULL)  // check until it becomes null
    {
        move_node(&(aLast->next), &current);   // add at aLast
        aLast = aLast->next;                  // move forward the aLast
        if (current != NULL)
        {
            move_node(&(bLast->next), &current);
            bLast = bLast->next;
        }
    }
    *aList = x.next;   // aList
    *bList = y.next;   // bList
}
