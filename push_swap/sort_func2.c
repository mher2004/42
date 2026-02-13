/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_func2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 18:23:45 by mher              #+#    #+#             */
/*   Updated: 2026/02/13 18:42:50 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void ra(stack **a, func_count *count, int bench)
{
    count->ra++;
    if (!bench)
        write(1, "ra\n", 3);
    
}

void rb(stack **b, func_count *count, int bench)
{
    count->rb++;
    if (!bench)
        write(1, "rb\n", 3);
    
}

void rr(stack **a, stack **b, func_count *count, int bench)
{
    count->rr++;
    if (!bench)
        write(1, "rr\n", 3);
    
}

void rra(stack **a, func_count *count, int bench)
{
    count->rra++;
    if (!bench)
        write(1, "rra\n", 3);
    
}

void rrb(stack **b, func_count *count, int bench)
{
    count->rrb++;
    if (!bench)
        write(1, "rrb\n", 3);
    
}