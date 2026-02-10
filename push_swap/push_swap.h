/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 21:16:06 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/10 21:23:38 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

#include "libft/libft.h"

int check_duplicates(char **container);
int check_no_num(char **container);
int check_long_num(char **container);
int mode_check(char *mode);
void free_container(char **container);
int filler(char **dest, char **src);
int check_nums(char **argv, int start, int end);
int error_checker(char ** argv, int argc);

#endif