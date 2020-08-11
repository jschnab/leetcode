/* from the book "cracking the coding interview"
 * given an unsorted linked list, remove all duplicate nodes
 * (with or without a buffer) */

#include <stdio.h>
#include <stdlib.h>


#define MAXVAL 10000


typedef struct node {
    int val;
    struct node *next;
} Node;


/* we have a space complexity of O(1) at the expense of a time complexity
 * of O(n2) */
void remove_dup(Node *head) {
    Node *runner = (Node *) malloc(sizeof(Node));

    while (head != NULL) {
        runner = head;
        while (runner->next != NULL ) {
            if (runner->next->val == head->val)
                runner->next = runner->next->next;
            else
                runner = runner->next;
        }
        head = head->next;
    }
}


/* we use an array to store whether a given value was seen before
   we achieve O(n) time complexity at the expense of space complexity */
void remove_dup3(Node *head) {
    char seen[MAXVAL] = {0};
    Node *previous = (Node *) malloc(sizeof(Node));

    while (head != NULL) {
        if (seen[head->val]) {
            previous->next = head->next;
        }
        else {
            seen[head->val] = 1;
            previous = head;
        }
        head = head->next;
    }
}


Node *remove_dup2(Node *head) {
    /* we use an array to store whether a given value was seen before */
    char seen[MAXVAL] = {0};

    Node *first = (Node *) malloc(sizeof(Node));
    first->next = head;
    Node *current = head;

    while (current != NULL) {
        seen[current->val] = 1;
        if (current->next != NULL && seen[current->next->val])
            current->next = current->next->next;
        current = current->next;
    }

    return first->next;
}


int main(int argc, char *argv[]) {
    Node *head = (Node *) malloc(sizeof(Node));
    head->val = 6;
    head->next = (Node *) malloc(sizeof(Node));
    head->next->val = 2;
    head->next->next = (Node *) malloc(sizeof(Node));
    head->next->next->val = 3;
    head->next->next->next = (Node *) malloc(sizeof(Node));
    head->next->next->next->val = 3;
    remove_dup(head);
    while (head != NULL) {
        printf("%d%s", head->val, (head->next != NULL) ? " -> " : "\n");
        head = head->next;
    }

    Node *head2 = (Node *) malloc(sizeof(Node));
    head2->val = 3;
    head2->next = (Node *) malloc(sizeof(Node));
    head2->next->val = 1;
    head2->next->next = (Node *) malloc(sizeof(Node));
    head2->next->next->val = 1;
    head2->next->next->next = (Node *) malloc(sizeof(Node));
    head2->next->next->next->val = 2;
    remove_dup(head2);
    while (head2 != NULL) {
        printf("%d%s", head2->val, (head2->next != NULL) ? " -> " : "\n");
        head2 = head2->next;
    }

    Node *head3 = (Node *) malloc(sizeof(Node));
    head3->val = 4;
    head3->next = (Node *) malloc(sizeof(Node));
    head3->next->val = 4;
    head3->next->next = (Node *) malloc(sizeof(Node));
    head3->next->next->val = 0;
    head3->next->next->next = (Node *) malloc(sizeof(Node));
    head3->next->next->next->val = 2;
    remove_dup(head3);
    while (head3 != NULL) {
        printf("%d%s", head3->val, (head3->next != NULL) ? " -> " : "\n");
        head3 = head3->next;
    }

    return 0;
}
