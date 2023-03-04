#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

size_t count_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * is_palindrome - function checks if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a  palindrome and 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	int *nArr, i = 0, j = 0, len = 0;
	listint_t *temp;

	if (*head == NULL)
		return (1);
	temp = *head;
	len = count_listint(temp);
	nArr = (int *)malloc(sizeof(int) * len);
	if (nArr == NULL)
		return (0);
	temp = *head;
	while (temp != NULL)
	{
		nArr[j] = temp->n;
		j++;
		temp = temp->next;
	}
	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (nArr[i] != nArr[j])
			return (0);
	}
	return (1);
}
