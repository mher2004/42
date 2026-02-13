/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_func1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mher <mher@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 18:23:45 by mher              #+#    #+#             */
/*   Updated: 2026/02/13 19:58:38 by mher             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void sa(stack **a, func_count *count, int bench, int c)
{
    stack *first;
    stack *second;
    stack *last;

    if (!*a || *a == (*a)->next)
        return;
    if (c)
        count->sa++;
    if (!bench)
        write(1, "sa\n", 3);
    first = *a;
    second = first->next;
    last = first->prev;
    if (second->next != first) 
    {
        last->next = second;
        second->prev = last;
        first->next = second->next;
        second->next->prev = first;
        second->next = first;
        first->prev = second;
    }
    *a = second;
}

void sb(stack **b, func_count *count, int bench, int c)
{
    stack *first;
    stack *second;
    stack *last;
    
    if (!*b || *b == (*b)->next)
        return;
    if (c)
        count->sb++;
    if (!bench)
        write(1, "sb\n", 3);
    first = *b;
    second = first->next;
    last = first->prev;
    if (second->next != first) 
    {
        last->next = second;
        second->prev = last;
        first->next = second->next;
        second->next->prev = first;
        second->next = first;
        first->prev = second;
    }
    *b = second;
}

void ss(stack **a, stack **b, func_count *count, int bench)
{
    count->ss++;
    if (!bench)
        write(1, "ss\n", 3);
    sa(a, count, 1, 0);
    sb(b, count, 1, 0);
}

pa1(stack **a, stack **b)
{
    stack *node;

    node
    if (!*b)
    {
        (*b)->index = (*a)->index;
        (*b)->num = (*a)->num;
        (*b)->next = *b;
        (*b)->prev = *b;
    }
    if (!*b)
    {
        (*b)->index = (*a)->index;
        (*b)->num = (*a)->num;
        (*b)->next = *b;
        (*b)->prev = *b;
    }
    if (!*b)
    {
        (*b)->index = (*a)->index;
        (*b)->num = (*a)->num;
        (*b)->next = *b;
        (*b)->prev = *b;
    }
}

pa2(stack **a, stack **b)
{
    
}

void pa(stack **a, stack **b, func_count *count, int bench)
{
    stack *node;
    
    if (!*a)
        return;
    node = *a;
    count->pa++;
    if (!bench)
        write(1, "pa\n", 3);
    if ((*a)->next == *a)
        *a = NULL;
    else
    {
        (*a)->next->prev = (*a)->prev;
        (*a)->prev->next = (*a)->next;
        *a = (*a)->next;
    }
    
}

void pb(stack **a, stack **b, func_count *count, int bench)
{
    count->pb++;
    if (!bench)
        write(1, "pb\n", 3);
    
}