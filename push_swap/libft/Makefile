# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmkrtchy <mmkrtchy@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 20:00:58 by mmkrtchy          #+#    #+#              #
#    Updated: 2026/02/09 19:40:00 by mmkrtchy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a
CC = cc
CFLAGS = -Wall -Wextra -Werror

SRCS =  ft_atoi.c ft_lstdelone.c ft_printf_utils.c ft_strlen.c \
ft_bzero.c         ft_lstiter.c    ft_putchar_fd.c    ft_strmapi.c \
ft_calloc.c        ft_lstlast.c    ft_putendl_fd.c    ft_strncmp.c \
ft_isalnum.c       ft_lstmap.c     ft_putnbr_fd.c     ft_strnstr.c \
ft_isalpha.c       ft_lstnew.c     ft_putstr_fd.c     ft_strrchr.c \
ft_isascii.c       ft_lstsize.c    ft_split.c         ft_strtrim.c \
ft_isdigit.c       ft_memchr.c     ft_strchr.c        ft_substr.c \
ft_isprint.c       ft_memcmp.c     ft_strdup.c        ft_tolower.c \
ft_itoa.c          ft_memcpy.c     ft_striteri.c      ft_toupper.c \
ft_lstadd_back.c   ft_memmove.c    ft_strjoin.c \
ft_lstadd_front.c  ft_memset.c     ft_strlcat.c \
ft_lstclear.c      ft_printf.c     ft_strlcpy.c 


OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
