/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 16:45:14 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/07 00:12:27 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_c(int a)
{
	return (write(1, &a, 1));
}

int	print_unsign(unsigned long nb, int base, const char *hex)
{
	char	buf[32];
	int		i;
	int		len;

	if (nb == 0)
		return (write(1, "0", 1));
	i = 0;
	while (nb)
	{
		buf[i++] = hex[nb % base];
		nb /= base;
	}
	len = i;
	while (i--)
		write(1, &buf[i], 1);
	return (len);
}

int	func(va_list args, char m)
{
	int	count;

	count = 0;
	if (m == 'c')
		count += print_c(va_arg(args, int));
	else if (m == 's')
		count += print_s(va_arg(args, char *));
	else if (m == 'd' || m == 'i')
		count += print_num((long)va_arg(args, int), 10, "0123456789");
	else if (m == 'p')
		count += print_p(va_arg(args, void *));
	else if (m == 'u')
		count += print_num((long)va_arg(args, unsigned int), 10, "0123456789");
	else if (m == 'x' || m == 'X')
		count += print_x(va_arg(args, unsigned int), m != 'x');
	else if (m == '%')
		count += print_c('%');
	return (count);
}

int	ft_printf(const char *text, ...)
{
	int		i;
	int		count;
	va_list	args;

	va_start(args, text);
	i = -1;
	count = 0;
	while (text[++i])
	{
		if (text[i] == '%' && text[i + 1])
			count += func(args, text[++i]);
		else
			count += write(1, &text[i], 1);
	}
	va_end(args);
	return (count);
}

// #include <stdio.h>

// int	main(void)
// {
// 	printf(" %p %p \n", 0, 0);
// 	ft_printf(" %p %p ", 0, 0);
// }
