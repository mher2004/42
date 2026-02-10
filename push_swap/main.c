/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 20:21:42 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/10 17:36:45 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int main(int argc, char ** argv)
{
    int mode;

    if (error_checker(argv, argc))
        return (write(1, "Error\n", 6), 0);
    mode = mode_check(argv[1]);
    run_sort(argv, mode);
}