/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_algo.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/20 21:37:51 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:26 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	bring_to_topa(t_stack **stack, int front, int back, t_func_count *count)
{
	if (front >= back)
		while (back-- > 0)
			rra(stack, count);
	else if (back > front)
		while (front-- > 0)
			ra(stack, count);
}

void	bring_to_topb(t_stack **stack, int front, int back, t_func_count *count)
{
	if (front >= back)
		while (back-- > 0)
			rrb(stack, count);
	else if (back > front)
		while (front-- > 0)
			rb(stack, count);
}

void	fill_back(t_stack **a, t_stack **b, t_func_count *count)
{
	int	size;

	size = get_max_ind(*b);
	while (0 <= size)
	{
		bring_to_topb(b, get_front_dist(*b, size), get_back_dist(*b, size),
			count);
		pa(a, b, count);
		size--;
	}
}

void	chunk_sort(t_stack **a, t_stack **b, t_func_count *count)
{
	int		i;
	int		chnks;
	int		chnke;
	int		step;
	t_stack	*node;

	chnks = 0;
	step = get_chunk_step(get_max_ind(*a));
	chnke = step;
	i = 0;
	while (*a)
	{
		bring_to_topa(a, get_chunk_fdist(*a, chnks, chnke), get_chunk_bdist(*a,
				chnks, chnke), count);
		node = *a;
		pb(a, b, count);
		if (node->index < chnks + (chnke - chnks) / 2)
			rb(b, count);
		if (++i > chnke)
		{
			chnks += step;
			chnke += step;
		}
	}
	fill_back(a, b, count);
}
