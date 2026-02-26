/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_mode_bench.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/26 16:00:51 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:02:55 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "push_swap.h"

int	get_total_ops(t_algo *algo)
{
	return (algo->count->sa + algo->count->sb + algo->count->ss
		+ algo->count->pa + algo->count->pb + algo->count->ra + algo->count->rb
		+ algo->count->rr + algo->count->rra + algo->count->rrb
		+ algo->count->rrr);
}

void	print_disorder(int d)
{
	putstr_stderr("[bench] disorder:  ");
	putnbr_stderr(d / 100);
	putstr_stderr(".");
	if (d % 100 < 10)
		putstr_stderr("0");
	putnbr_stderr(d % 100);
	putstr_stderr("%\n");
}

void	print_ops(t_algo *algo)
{
	putstr_stderr("[bench] sa: ");
	putnbr_stderr(algo->count->sa);
	putstr_stderr("  sb: ");
	putnbr_stderr(algo->count->sb);
	putstr_stderr("  ss: ");
	putnbr_stderr(algo->count->ss);
	putstr_stderr("  pa: ");
	putnbr_stderr(algo->count->pa);
	putstr_stderr("  pb: ");
	putnbr_stderr(algo->count->pb);
	putstr_stderr("\n");
	putstr_stderr("[bench] ra: ");
	putnbr_stderr(algo->count->ra);
	putstr_stderr("  rb: ");
	putnbr_stderr(algo->count->rb);
	putstr_stderr("  rr: ");
	putnbr_stderr(algo->count->rr);
	putstr_stderr("  rra: ");
	putnbr_stderr(algo->count->rra);
	putstr_stderr("  rrb: ");
	putnbr_stderr(algo->count->rrb);
	putstr_stderr("  rrr: ");
	putnbr_stderr(algo->count->rrr);
	putstr_stderr("\n");
}

char	*get_strategy_name(t_algo *algo)
{
	if (algo->mode == 2 || (algo->mode == 1 && algo->disorder < 2000))
	{
		if (algo->mode == 2)
			return ("Simple / O(n^2)");
		return ("Adaptive / O(n^2)");
	}
	else if (algo->mode == 3 || (algo->mode == 1 && algo->disorder < 5000))
	{
		if (algo->mode == 3)
			return ("Medium / O(n\xe2\x88\x9an)");
		return ("Adaptive / O(n\xe2\x88\x9an)");
	}
	else
	{
		if (algo->mode == 4)
			return ("Complex / O(n log n)");
		return ("Adaptive / O(n log n)");
	}
}

void	execute_strategy(t_algo *algo)
{
	char	*strat;

	strat = get_strategy_name(algo);
	if (algo->mode == 2 || (algo->mode == 1 && algo->disorder < 2000))
		selection_sort(&algo->a, &algo->b, algo->count);
	else if (algo->mode == 3 || (algo->mode == 1 && algo->disorder < 5000))
		chunk_sort(&algo->a, &algo->b, algo->count);
	else
		radix_sort(&algo->a, &algo->b, algo->count);
	if (algo->bench_flag == 1)
		print_bench(algo, strat);
}
