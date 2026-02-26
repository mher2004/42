# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 20:00:58 by mmkrtchy          #+#    #+#              #
#    Updated: 2026/02/26 16:03:25 by mmkrtchy         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap
CC = cc
CFLAGS = -Wall -Wextra -Werror -g3 -I. -I./libft
LIBFT = ./libft/libft.a

SRCS =  main.c checks.c checks2.c fill_nums.c disorder.c \
 sort_func1.c sort_func2.c sort_func3.c int_to_stack.c \
 simple_algo.c check_mode_bench.c print_stderr.c  \
 medium_helper1.c medium_helper2.c complex_algo.c medium_algo.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS) $(LIBFT)
	$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)

$(LIBFT):
	make -C ./libft

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)
	make -C ./libft clean

fclean: clean
	rm -f $(NAME)
	make -C ./libft fclean

re: fclean all

.PHONY: all clean fclean re
