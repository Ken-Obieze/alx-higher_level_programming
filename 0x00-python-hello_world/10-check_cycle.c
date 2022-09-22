#include "lists.h"

/**
 * check_cycle - checks sigly linked list for cycle
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *check;

	if (list == NULL)
		return (0);

	check = list->next;
	while (check)
	{
		if (check == list)
			return (1);
		check = check->next;
	}
	return (0);
}
