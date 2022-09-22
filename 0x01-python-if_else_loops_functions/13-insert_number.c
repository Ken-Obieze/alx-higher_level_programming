#include "lists.h"

/*
 * insert_node - inserts number into sorted linked list
 * @head: linked list
 * @number: data to insert in our list
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	int key = number;

	listint_t *temp;
	listint_t *newNode = malloc(sixeof(listint_t));

	newNode->n = number;
	newNode->next = NULL;

	if (head == NULL || key < head->)
	{
		newNode->next = head;
		head = newNode;
	}

	temp = head;
	while (temp->next != NULL && temp->next->n < key)
		temp = temp->next;
	newNode->next = temp->next;
	temp->next = newNode;
	return (head);
}
