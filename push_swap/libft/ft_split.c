/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 14:22:07 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/10 19:41:48 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	count_words(char const *s, char c)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	if (!s)
		return (0);
	while (s[i])
	{
		if (s[i] != c)
		{
			count++;
			while (s[i] != c && s[i])
				i++;
		}
		else
			i++;
	}
	return (count);
}

char	*word(char const *text, char c, int *i)
{
	int		j;
	char	*w;

	j = 0;
	while (text[*i + j] && text[*i + j] != c)
		j++;
	w = (char *)malloc(sizeof(char) * (j + 1));
	if (!w)
		return (NULL);
	j = 0;
	while (text[*i] && text[*i] != c)
		w[j++] = text[(*i)++];
	w[j] = '\0';
	return (w);
}

void	f(char **text, int j)
{
	while (j >= 0)
		free(text[j--]);
	free(text);
}

char	**ft_split(char const *s, char c)
{
	char	**text;
	int		i;
	int		j;

	if (!s)
		return (NULL);
	text = (char **)malloc(sizeof(char *) * (count_words(s, c) + 1));
	if (!text)
		return (NULL);
	i = 0;
	j = 0;
	while (s[i])
	{
		if (s[i] != c)
		{
			text[j++] = word(s, c, &i);
			if (!text[j - 1])
				return (f(text, j - 1), NULL);
		}
		else
			i++;
	}
	text[j] = NULL;
	return (text);
}
/*
int main(){
char p[]="  adfghn qadsd          wqsdwsc qssqax      ";
char **aa;

aa = ft_split(p,' ');
printf("%s", aa[1]);
return (0);
}
*/
