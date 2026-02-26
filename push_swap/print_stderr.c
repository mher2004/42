/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_stderr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/23 15:50:47 by rmesropy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:31 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	putstr_stderr(char *s)
{
	int	i;

	i = 0;
	if (!s)
		return ;
	while (s[i])
		write(2, &s[i++], 1);
}

void	putnbr_stderr(long n)
{
	char	c;

	if (n < 0)
	{
		write(2, "-", 1);
		n = -n;
	}
	if (n >= 10)
		putnbr_stderr(n / 10);
	c = (n % 10) + '0';
	write(2, &c, 1);
}

void	init_algo_params(t_algo *algo, char **argv)
{
	int	m1;
	int	m2;

	algo->disorder = compute_disorder(algo->nums, algo->size);
	algo->mode = 1;
	algo->bench_flag = 0;
	m1 = 0;
	m2 = 0;
	if (argv[1])
		m1 = mode_check(argv[1]);
	if (argv[1] && argv[2])
		m2 = mode_check(argv[2]);
	if (m1 == 5)
		algo->bench_flag = 1;
	else if (m1 > 0)
		algo->mode = m1;
	if (m2 == 5)
		algo->bench_flag = 1;
	else if (m2 > 0)
		algo->mode = m2;
}

void	print_bench(t_algo *algo, char *strat)
{
	int	total;

	total = get_total_ops(algo);
	print_disorder(algo->disorder);
	print_strategy_total(strat, total);
	print_ops(algo);
}

void	print_strategy_total(char *strat, int total)
{
	putstr_stderr("[bench] strategy:  ");
	putstr_stderr(strat);
	putstr_stderr("\n");
	putstr_stderr("[bench] total_ops: ");
	putnbr_stderr(total);
	putstr_stderr("\n");
}
