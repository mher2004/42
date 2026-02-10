/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checks2.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 20:01:59 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/10 21:35:51 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int check_duplicates(char **container)
{
    int i;
    int j;

    i = 0;
    while (container[i])
    {
        j = i + 1;
        while (container[j])
        {
            if (!ft_strcmp(container[i], container[j]))
                return (1);
            j++;
        }
        i++;
    }
    return (0);
}

int check_no_num(char **container)
{
    int i;
    int j;

    i = 0;
    while (container[i])
    {
        j = 1;
        if (!ft_isdigit(container[i][0]) && container[i][0] != '+' && container[i][0] != '-')
                return (1);
        while (container[i][j])
            if (!ft_isdigit(container[i][j++]))
                return (1);
        i++;
    }
    return (0);
}

int check_long_num(char **container)
{
    int i;

    i = 0;
    while (container[i])
    {
        if ((container[i][0] == '+' || container[i][0] == '-') && ft_strlen(container[i]) > 11)
            return (1);
        else if (ft_strlen(container[i]) > 10)
            return (1);
        i++;
    }
    return (0);
}