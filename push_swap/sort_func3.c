/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_func3.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 18:23:45 by mher              #+#    #+#             */
/*   Updated: 2026/02/26 16:03:37 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rrr(t_stack **a, t_stack **b, t_func_count *count)
{
	if (!(*a) || (*a) == (*a)->next)
		return ;
	if (!(*b) || (*b) == (*b)->next)
		return ;
	*a = (*a)->prev;
	*b = (*b)->prev;
	rrb(b, count);
	count->rrr++;
	write(1, "rrr\n", 4);
}

void	p_helper(t_stack *node, t_stack **push)
{
	t_stack	*old_node;

	if (!(*push))
	{
		*push = node;
		(*push)->next = node;
		(*push)->prev = node;
	}
	else
	{
		old_node = *push;
		old_node->prev->next = node;
		node->prev = old_node->prev;
		node->next = old_node;
		old_node->prev = node;
		*push = node;
	}
}
