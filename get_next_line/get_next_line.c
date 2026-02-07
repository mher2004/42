/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 00:38:30 by mher              #+#    #+#             */
/*   Updated: 2026/02/04 03:35:25 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

void	*ft_memmove(char *dest, char *src, int n)
{
	int				i;
	unsigned char	*d;
	unsigned char	*s;

	d = (unsigned char *)dest;
	s = (unsigned char *)src;
	i = 0;
	if (!dest && !src)
		return (NULL);
	if (d < s)
	{
		while (i < n)
		{
			d[i] = s[i];
			++i;
		}
	}
	else
		while (n-- > 0)
			d[n] = s[n];
	return (dest);
}

char	*new_line(char **line)
{
	int		i;
	int		len;
	char	*p;
	char	*realloc_line;

	i = 0;
	len = ft_strlen(*line);
	while ((*line)[i] != '\n')
		++i;
	p = (char *)malloc(i + 2);
	ft_memmove(p, *line, i + 1);
	p[i + 1] = '\0';
	realloc_line = (char *)malloc(len - i);
	if (realloc_line)
	{
		ft_memmove(realloc_line, &(*line)[i + 1], len - i);
		realloc_line[len - i - 1] = '\0';
	}
	free(*line);
	*line = realloc_line;
	return (p);
}

int	read_more(char **line, int fd)
{
	int		i;
	int		readed_bytes;
	int		len;
	char	*buffer;
	char	*realloc_line;

	len = ft_strlen(*line);
	buffer = malloc(BUFFER_SIZE);
	if (!buffer)
		return (-1);
	readed_bytes = read(fd, buffer, BUFFER_SIZE);
	if (readed_bytes <= 0)
		return (free(buffer), readed_bytes);
	realloc_line = (char *)malloc(readed_bytes + len + 1);
	if (!realloc_line)
		return (free(buffer), -2);
	ft_memmove(realloc_line, *line, len);
	i = 0;
	while (i < readed_bytes)
	{
		realloc_line[len + i] = buffer[i];
		++i;
	}
	realloc_line[len + i] = '\0';
	return (free(buffer), free(*line), *line = realloc_line, readed_bytes);
}

char	*get_next_line(int fd)
{
	int			i;
	static char	*line = NULL;
	char		*tmp;

	while (1)
	{
		if (is_there_new_line(line))
			return (new_line(&line));
		i = read_more(&line, fd);
		if (i <= 0)
		{
			if (i == 0 && line && *line != '\0')
			{
				tmp = line;
				line = NULL;
				return (tmp);
			}
			free(line);
			line = NULL;
			return (NULL);
		}
	}
}

// int	main(void)
// {
// 	char	*fileName;
// 	int		fd;

// 	fileName = "a.out";
// 	fd = open(fileName, O_RDWR);
// 	// if (fd == -1)
// 	// {
// 	// 	printf("\nError Opening File!!\n");
// 	// 	exit(1);
// 	// }
// 	// else
// 	// 	printf("\nFile %s opened sucessfully!\n", fileName);
// 	printf("File Contents: %s\n", get_next_line(fd));
// 	printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	// printf("%s", get_next_line(fd));
// 	return (0);
// }
