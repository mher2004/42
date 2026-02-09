/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 15:42:27 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/01/30 15:57:28 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	isthere(char a, const char *s)
{
	int	i;

	i = 0;
	while (s[i])
	{
		if (s[i] == a)
			return (1);
		i++;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		start;
	int		end;
	char	*p;
	int		k;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	while (s1[start] && isthere(s1[start], set))
		start++;
	end = ft_strlen(s1);
	while (end > start && isthere(s1[end - 1], set))
		end--;
	p = (char *)malloc(sizeof(char) * (end - start + 1));
	if (!p)
		return (NULL);
	k = 0;
	while (start < end)
		p[k++] = s1[start++];
	p[k] = '\0';
	return (p);
}
