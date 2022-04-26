#include "lists.h"
/**
 * check_cycle - Checks if a single list has a cycle in it
 * @list: checker
 * Return: 0 if there is not a cycle and 1 if it is
 */

int check_cycle(listint_t *list)
{
	listint_t *_single = list;
	listint_t *_double = list;

	while (_single != NULL && _double != NULL)
	{
		_single = _single->next;
		_double = _double->next->next;
		if (_double == _single)
			return (1);
	}

	return (0);
}
