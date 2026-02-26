/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 20:21:42 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:21 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	is_sorted(t_stack *a)
{
	t_stack	*tmp;

	if (!a)
		return (1);
	tmp = a;
	while (tmp->next != a)
	{
		if (tmp->index > tmp->next->index)
			return (0);
		tmp = tmp->next;
	}
	return (1);
}

void	free_stack(t_stack **stack)
{
	t_stack	*current;
	t_stack	*next_node;
	t_stack	*start;

	if (!stack || !*stack)
		return ;
	current = *stack;
	start = *stack;
	while (1)
	{
		next_node = current->next;
		free(current);
		current = next_node;
		if (current == start)
			break ;
	}
	*stack = NULL;
}

int	main(int argc, char **argv)
{
	int				*nums;
	int				count_nums;
	t_func_count	count;
	t_algo			algo;

	if (error_checker(argv, argc))
		return (write(1, "Error\n", 6), 0);
	nums = filling_nums(argv, get_start(argv, argc), argc, &count_nums);
	if (duplicate_checker(nums, count_nums))
		return (free(nums), write(1, "Error\n", 6), 0);
	algo.a = NULL;
	algo.b = NULL;
	int_to_stack(nums, count_nums, &algo.a);
	ft_bzero(&count, sizeof(t_func_count));
	if (is_sorted(algo.a))
		return (free(nums), free_stack(&algo.a), 0);
	algo.count = &count;
	algo.nums = nums;
	algo.size = count_nums;
	return (init_algo_params(&algo, argv), execute_strategy(&algo), free(nums),
		free_stack(&algo.a), free_stack(&algo.b), 0);
}
