/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fill_nums.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/12 19:06:56 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/12 20:17:57 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

char **filling_container(char **argv, int start, int argc)
{
    int		obj_count;
	int		i;
	char	**container;

    obj_count = 0;
	i = start;
	while (i < argc)
		obj_count += count_words(argv[i++], ' ');
	container = (char **)malloc(sizeof(char *) * (obj_count + 1));
	if (!container)
		return (NULL);
	container[0] = NULL;
	i = start;
	while (i < argc)
		if (filler(container, ft_split(argv[i++], ' ')))
			return (free_container(container), NULL);
    return (container);
}

void char_to_int(char **container, int *numbers)
{
    int i;

    i = 0;
    if (!container || !numbers)
        return ;
    while(container[i])
    {
        numbers[i] = ft_atoi(container[i]);
        i++;
    }
}

int *filling_nums(char **argv, int start, int argc, int *count)
{
	int		i;
	char	**container;
    int     *numbers;

	*count = 0;
	i = start;
	while (i < argc)
		*count += count_words(argv[i++], ' ');
    container = filling_container(argv, start, argc);
	if(!container)
        return (NULL);
	numbers = (int *)malloc(*count * sizeof(int));
    if (!numbers)
        return(free_container(container), NULL);
    char_to_int(container, numbers);
	free_container(container);
	return (numbers);
}

int get_start(char **argv, int argc)
{
    if (argc == 2)
        return (1);
    if (argc == 3 && !mode_check(argv[1]))
        return (1);
    else if(argc == 3 && mode_check(argv[1]))
        return (2);
    else if(mode_check(argv[1]) && mode_check(argv[2]))
        return (4);
    else if(mode_check(argv[1]) || mode_check(argv[2]))
        return (3);
    return (1);
}