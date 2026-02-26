/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   disorder.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/15 21:21:09 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:17 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	compute_disorder(int *numbers, int size)
{
	int	i;
	int	j;
	int	mistakes;
	int	pairs;

	i = 0;
	j = 0;
	mistakes = 0;
	pairs = 0;
	if (size == 1)
		return (0);
	while (i < (size - 1))
	{
		j = i + 1;
		while (j < size)
		{
			pairs++;
			if (numbers[i] > numbers[j])
				mistakes++;
			j++;
		}
		i++;
	}
	return ((mistakes * 10000) / pairs);
}
