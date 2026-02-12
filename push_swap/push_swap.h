/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 21:16:06 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/12 19:50:12 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"

int		check_duplicates(char **container);
int		check_no_num(char **container);
int		check_long_num(char **container);
int		mode_check(char *mode);
void	free_container(char **container);
int		filler(char **dest, char **src);
int		check_nums(char **argv, int start, int end);
int		error_checker(char **argv, int argc);

char **filling_container(char **argv, int start, int argc);
void char_to_int(char **container, int *numbers);
int *filling_nums(char **argv, int start, int argc, int *count);
int get_start(char **argv, int argc);


#endif