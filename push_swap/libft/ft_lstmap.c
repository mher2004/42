/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 18:31:10 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/01/30 16:09:34 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new;
	t_list	*newnode;

	new = (t_list *)malloc(sizeof(t_list));
	if (!new || !lst || !f || !del)
		return (NULL);
	newnode = new;
	while (lst)
	{
		newnode->content = f(lst->content);
		if (lst->next)
		{
			newnode->next = (t_list *)malloc(sizeof(t_list));
			if (!newnode->next)
			{
				ft_lstclear(&new, del);
				return (NULL);
			}
			newnode = newnode->next;
		}
		else
			newnode->next = NULL;
		lst = lst->next;
	}
	return (new);
}
