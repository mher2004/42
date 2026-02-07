/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/04 01:51:10 by mher              #+#    #+#             */
/*   Updated: 2026/02/04 02:06:54 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	if (!str)
		return (0);
	while (str[i])
		i++;
	return (i);
}

int	is_there_new_line(char *buff)
{
	int	i;

	i = 0;
	if (!buff)
		return (0);
	while (buff[i])
		if (buff[i++] == '\n')
			return (1);
	return (0);
}
