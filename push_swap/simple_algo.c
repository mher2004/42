/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_algo.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/18 13:11:32 by rmesropy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:34 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "push_swap.h"

int	stack_size(t_stack *a)
{
	int		size;
	t_stack	*start;

	if (!a)
		return (0);
	size = 0;
	start = a;
	while (1)
	{
		size++;
		a = a->next;
		if (a == start)
			break ;
	}
	return (size);
}

int	find_position(t_stack *a, int target_index)
{
	int		i;
	t_stack	*current;

	if (!a)
		return (-1);
	i = 0;
	current = a;
	while (1)
	{
		if (current->index == target_index)
			return (i);
		current = current->next;
		i++;
		if (current == a)
			break ;
	}
	return (-1);
}

int	find_min_index(t_stack *a)
{
	int		min;
	t_stack	*current;

	if (!a)
		return (-1);
	min = a->index;
	current = a->next;
	while (current != a)
	{
		if (current->index < min)
			min = current->index;
		current = current->next;
	}
	return (min);
}

void	bring_index_to_top(t_stack **a, int target_index, t_func_count *count)
{
	int	pos;
	int	size;

	if (!a || !(*a))
		return ;
	pos = find_position(*a, target_index);
	size = stack_size(*a);
	if (pos <= size / 2)
	{
		while ((*a)->index != target_index)
			ra(a, count);
	}
	else
	{
		while ((*a)->index != target_index)
			rra(a, count);
	}
}

void	selection_sort(t_stack **a, t_stack **b, t_func_count *count)
{
	while (*a)
	{
		bring_index_to_top(a, find_min_index(*a), count);
		pb(a, b, count);
	}
	while (*b)
		pa(a, b, count);
}
