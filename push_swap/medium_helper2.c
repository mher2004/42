/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_helper2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/20 21:03:08 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:29 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	get_chunk_fdist(t_stack *stack, int start, int end)
{
	int	i;

	i = 0;
	if (!stack)
		return (-1);
	while (stack->index > end || stack->index < start)
	{
		i++;
		stack = stack->next;
	}
	return (i);
}

int	get_chunk_bdist(t_stack *stack, int start, int end)
{
	int	i;

	i = 0;
	if (!stack)
		return (-1);
	while (stack->index > end || stack->index < start)
	{
		i++;
		stack = stack->prev;
	}
	return (i);
}
