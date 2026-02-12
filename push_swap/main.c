/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 20:21:42 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/12 20:34:12 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include <stdio.h>
#include <limits.h>

int	main(int argc, char **argv)
{
	// int mode;
	// int bench;
	int *nums;
	// int i = 0;
	int count;
	
	if (error_checker(argv, argc))
		return (write(1, "Error\n", 6), 0);
	
	nums = filling_nums(argv, get_start(argv, argc), argc, &count);
	printf("%d",nums[0]);
	free(nums);

	// mode = mode_check(argv[1]);
	// run_sort(argv, mode);
}