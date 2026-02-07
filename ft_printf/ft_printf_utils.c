/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 19:26:32 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/07 00:12:03 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	numlen(long n, int base)
{
	int	i;

	i = 0;
	if (n <= 0)
		i++;
	while (n)
	{
		n /= base;
		i++;
	}
	return (i);
}

int	print_num(long nb, int base, const char *hex)
{
	int		len;
	char	*p;

	len = numlen(nb, base);
	p = (char *)malloc(sizeof(char) * (len + 1));
	if (!p)
		return (0);
	p[len] = '\0';
	if (nb == 0)
		p[0] = '0';
	if (nb < 0)
	{
		p[0] = '-';
		nb = -nb;
	}
	while (nb > 0)
	{
		p[--len] = hex[nb % base];
		nb /= base;
	}
	len = print_s(p);
	return (free(p), len);
}

int	print_s(char *text)
{
	int	i;

	i = 0;
	if (!text)
		return (write(1, "(null)", 6));
	while (text[i])
		write(1, &text[i++], 1);
	return (i);
}

int	print_x(unsigned int text, int x)
{
	if (!x)
		return (print_num((long)text, 16, "0123456789abcdef"));
	else
		return (print_num((long)text, 16, "0123456789ABCDEF"));
}

int	print_p(void *a)
{
	if ((long long)a == 0)
		return (write(1, "(nil)", 5));
	write(1, "0x", 2);
	return (2 + print_unsign((unsigned long)a, 16, "0123456789abcdef"));
}
