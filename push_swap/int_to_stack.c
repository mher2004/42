/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   int_to_stack.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/15 19:33:10 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:20 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	switch_ints(int *a, int *b)
{
	int	tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

int	*sort(int *nums, int size)
{
	int	*sorted_nums;
	int	i;
	int	j;

	sorted_nums = (int *)malloc(size * sizeof(int));
	i = 0;
	while (i < size)
	{
		sorted_nums[i] = nums[i];
		i++;
	}
	i = 0;
	j = 0;
	while (i < size)
	{
		j = i + 1;
		while (j < size)
		{
			if (sorted_nums[i] > sorted_nums[j])
				switch_ints(&sorted_nums[i], &sorted_nums[j]);
			j++;
		}
		i++;
	}
	return (sorted_nums);
}

int	get_index(int *numbers, int num)
{
	int	i;

	i = 0;
	while (numbers[i] != num)
		i++;
	return (i);
}

void	int_to_stack(int *nums, int size, t_stack **a)
{
	int		i;
	int		*sorted;
	t_stack	*node;

	i = 0;
	sorted = sort(nums, size);
	while (i < size)
	{
		node = (t_stack *)malloc(sizeof(t_stack));
		if (!node)
			return ;
		node->next = node;
		node->prev = node;
		node->num = nums[size - i - 1];
		node->index = get_index(sorted, node->num);
		p_helper(node, a);
		i++;
	}
	free(sorted);
}
