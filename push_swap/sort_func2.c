/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_func2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 18:23:45 by mher              #+#    #+#             */
/*   Updated: 2026/02/26 16:03:36 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra(t_stack **a, t_func_count *count)
{
	if (!(*a) || (*a) == (*a)->next)
		return ;
	*a = (*a)->next;
	count->ra++;
	write(1, "ra\n", 3);
}

void	rb(t_stack **b, t_func_count *count)
{
	if (!(*b) || (*b) == (*b)->next)
		return ;
	*b = (*b)->next;
	count->rb++;
	write(1, "rb\n", 3);
}

void	rr(t_stack **a, t_stack **b, t_func_count *count)
{
	if (!(*a) || (*a) == (*a)->next)
		return ;
	if (!(*b) || (*b) == (*b)->next)
		return ;
	*a = (*a)->next;
	*b = (*b)->next;
	count->rr++;
	write(1, "rr\n", 3);
}

void	rra(t_stack **a, t_func_count *count)
{
	if (!(*a) || (*a) == (*a)->next)
		return ;
	*a = (*a)->prev;
	count->rra++;
	write(1, "rra\n", 4);
}

void	rrb(t_stack **b, t_func_count *count)
{
	if (!(*b) || (*b) == (*b)->next)
		return ;
	*b = (*b)->prev;
	count->rrb++;
	write(1, "rrb\n", 4);
}
