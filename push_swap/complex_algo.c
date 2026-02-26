/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_algo.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/25 00:05:10 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:16 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	max_bits(int size)
{
	int	bits;
	int	n;

	bits = 0;
	n = size - 1;
	while (n > 0)
	{
		bits++;
		n /= 2;
	}
	return (bits);
}

void	radix_sort(t_stack **a, t_stack **b, t_func_count *count)
{
	int	size;
	int	bits;
	int	bit;
	int	i;

	size = stack_size(*a);
	bits = max_bits(size);
	bit = 0;
	while (bit < bits)
	{
		i = 0;
		while (i < size)
		{
			if (((*a)->index >> bit) & 1)
				ra(a, count);
			else
				pb(a, b, count);
			i++;
		}
		while (*b)
			pa(a, b, count);
		bit++;
	}
}
