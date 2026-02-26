/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_func1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 18:23:45 by mher              #+#    #+#             */
/*   Updated: 2026/02/26 16:03:35 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sa(t_stack **a, t_func_count *count, int c)
{
	t_stack	*first;
	t_stack	*second;
	t_stack	*last;

	if (!*a || *a == (*a)->next)
		return ;
	if (c)
	{
		count->sa++;
		write(1, "sa\n", 3);
	}
	first = *a;
	second = first->next;
	last = first->prev;
	if (second->next != first)
	{
		last->next = second;
		second->prev = last;
		first->next = second->next;
		second->next->prev = first;
		second->next = first;
		first->prev = second;
	}
	*a = second;
}

void	sb(t_stack **b, t_func_count *count, int c)
{
	t_stack	*first;
	t_stack	*second;
	t_stack	*last;

	if (!*b || *b == (*b)->next)
		return ;
	if (c)
	{
		count->sb++;
		write(1, "sb\n", 3);
	}
	first = *b;
	second = first->next;
	last = first->prev;
	if (second->next != first)
	{
		last->next = second;
		second->prev = last;
		first->next = second->next;
		second->next->prev = first;
		second->next = first;
		first->prev = second;
	}
	*b = second;
}

void	ss(t_stack **a, t_stack **b, t_func_count *count)
{
	count->ss++;
	write(1, "ss\n", 3);
	sa(a, count, 1);
	sb(b, count, 1);
}

void	pa(t_stack **a, t_stack **b, t_func_count *count)
{
	t_stack	*node;

	if (!*b)
		return ;
	node = *b;
	count->pa++;
	write(1, "pa\n", 3);
	if ((*b)->next == *b)
		*b = NULL;
	else
	{
		(*b)->next->prev = (*b)->prev;
		(*b)->prev->next = (*b)->next;
		*b = (*b)->next;
	}
	p_helper(node, a);
}

void	pb(t_stack **a, t_stack **b, t_func_count *count)
{
	t_stack	*node;

	if (!*a)
		return ;
	node = *a;
	count->pb++;
	write(1, "pb\n", 3);
	if ((*a)->next == *a)
		*a = NULL;
	else
	{
		(*a)->next->prev = (*a)->prev;
		(*a)->prev->next = (*a)->next;
		*a = (*a)->next;
	}
	p_helper(node, b);
}
