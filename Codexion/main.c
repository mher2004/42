/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/08 15:54:16 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/05/08 17:15:57 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "head.h"

int	main(int argc, char **argv)
{
	struct timeval	tv;
	t_param			param;

	if (!parse_checker(argc, argv))
	{
		printf("Error");
		return (1);
	}
	def_param(&param, argv);
}
