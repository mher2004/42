/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   head.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/08 17:14:42 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/05/08 17:38:05 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

typedef struct s_param
{
	int		number_of_coders;
	int		time_to_burnout;
	int		time_to_compile;
	int		time_to_debug;
	int		time_to_refactor;
	int		number_of_compiles_required;
	int		dongle_cooldown;
	char	scheduler[5];
}			t_param;

typedef struct s_coder
{
    int time;
}           t_coder;

int  is_valid_int(const char *str, int zero)
{
    int i;

    if (!str || !str[0] || strlen(str) > 10)
        return (0);
    i = 0;
    while (str[i])
    {
        if (str[i] < '0' || str[i] > '9')
            return (0);
        i++;
    }
    if (!zero && atoi(str) < 1)
        return (0);
    return (1);
}

int	parse_checker(int argc, char **argv)
{
	if (argc != 9)
		return (0);
	if (!is_valid_int(argv[1], 0))
		return (0);
	if (!is_valid_int(argv[2], 0))
		return (0);
	if (!is_valid_int(argv[3], 0))
		return (0);
	if (!is_valid_int(argv[4], 0))
		return (0);
	if (!is_valid_int(argv[5], 0))
		return (0);
	if (!is_valid_int(argv[6], 0))
		return (0);
	if (!is_valid_int(argv[7], 1))
		return (0);
	if (strcmp(argv[8], "fifo") && strcmp(argv[8], "edf"))
		return (0);
	return (1);
}

void	def_param(t_param *param, char **argv)
{
	param->number_of_coders = atoi(argv[1]);
	param->time_to_burnout = atoi(argv[2]);
	param->time_to_compile = atoi(argv[3]);
	param->time_to_debug = atoi(argv[4]);
	param->time_to_refactor = atoi(argv[5]);
	param->number_of_compiles_required = atoi(argv[6]);
	param->dongle_cooldown = atoi(argv[7]);
	if (!strcmp(argv[8], "fifo"))
	{
		param->scheduler[0] = 'f';
		param->scheduler[1] = 'i';
		param->scheduler[2] = 'f';
		param->scheduler[3] = 'o';
		param->scheduler[4] = 0;
	}
	else
	{
		param->scheduler[0] = 'e';
		param->scheduler[1] = 'd';
		param->scheduler[2] = 'f';
		param->scheduler[3] = 0;
	}
}
