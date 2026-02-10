/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checks.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 16:24:03 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/10 20:50:26 by mmkrtchy         ###   ########.fr       */
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

void free_container(char **container)
{
    int i;

    i = 0;
    while(container[i])
        free(container[i++]);
    free(container);
}

int filler(char **dest, char **src)
{
    int i;
    int j;

    i = 0;
    j = 0;
    if (!src)
        return (free_container(dest), 1);
    while (dest[i])
        i++;
    while (src[j])
        dest[i++] = src[i++];
    dest[i] = NULL;
    return (0);
}

int check_nums(char **argv, int start, int end)
{
    int obj_count;
    int i;
    char **container;
    
    obj_count = 0;
    i = start;
    while (i < end)
        obj_count += count_words(argv[i++], ' ');
    container = (char **)malloc(sizeof(char *) * obj_count + 1);
    if (!container)
        return (1);
    container[0] = NULL;
    i = 0;
    while (start < end)
        if (filler(container, ft_split(argv[start++], ' ')))
            return (1);
    if(check_duplicates(container) || check_long_num(container) || check_no_num(container))
        return (1);
    return (0);
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