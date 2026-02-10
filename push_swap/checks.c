/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checks.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 16:24:03 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/10 17:56:53 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int mode_check(char *mode)
{
    if (!ft_strcmp(mode, "--adaptive"))
        return (1);
    else if (!ft_strcmp(mode, "--simple"))
        return (2);
    else if (!ft_strcmp(mode, "--medium"))
        return (3);
    else if (!ft_strcmp(mode, "--complex"))
        return (4);
    else if (!ft_strcmp(mode, "--bench"))
        return (5);
    else
        return (0);
}

int check_duplicates(char **argv, int start, int argc)
{
    int pivot;

    while (start < argc)
    {
        pivot = start + 1;
        while (pivot < argc)
        {
            if (argv[start] == argv[pivot])
                return (1);
            pivot++;
        }
        if (not_number_checker(argv[start]) || not_int_checker(argv[start]))
        start++;
    }
}
int error_checker(char ** argv, int argc)
{
    if (argc <= 1)
        return (1);
    if (mode_check(argv[1]))
    {
        if (mode_check(argv[2]))
            return (check_nums(argv, 3, argc));
        return (check_nums(argv, 2, argc));
    }
    return (check_nums(argv, 1, argc));
}