#include "lists.h"
/**
 * check_cycle - function to check a cycle
 * @list: the linked list
 * Return: 0 if the list doesnt have a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
