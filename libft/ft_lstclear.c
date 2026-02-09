/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 18:15:36 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/01/30 16:08:10 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*nn;

	if (!lst || !(*lst) || !del)
		return ;
	while (*lst)
	{
		nn = (*lst)->next;
		ft_lstdelone(*lst, del);
		*lst = nn;
	}
	*lst = NULL;
}
