/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 19:25:18 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/06 23:58:15 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <stdlib.h>
# include <unistd.h>

int	print_num(long nb, int base, const char *hex);
int	print_s(char *text);
int	print_c(int text);
int	print_unsign(unsigned long nb, int base, const char *hex);
int	print_u(unsigned int text);
int	print_p(void *a);
int	print_d(int text);
int	print_x(unsigned int text, int x);
int	ft_printf(const char *text, ...);

#endif