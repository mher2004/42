/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_helper1.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/20 21:03:08 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:28 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	get_max_ind(t_stack *stack)
{
	int		max;
	t_stack	*start;

	if (!stack)
		return (-1);
	max = stack->index;
	start = stack;
	stack = stack->next;
	while (start != stack)
	{
		if (stack->index > max)
			max = stack->index;
		stack = stack->next;
	}
	return (max);
}

int	get_back_dist(t_stack *stack, int index)
{
	int	i;

	i = 0;
	if (!stack)
		return (-1);
	while (stack->index != index)
	{
		i++;
		stack = stack->prev;
	}
	return (i);
}

int	get_front_dist(t_stack *stack, int index)
{
	int	i;

	i = 0;
	if (!stack)
		return (-1);
	while (stack->index != index)
	{
		i++;
		stack = stack->next;
	}
	return (i);
}

int	get_chunk_step(int max_index)
{
	if (max_index <= 20)
		return (max_index / 2);
	else if (max_index <= 100)
		return (16);
	else if (max_index <= 500)
		return (38);
	else
		return (max_index / 13);
}
