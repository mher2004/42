/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mmkrtchy <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 21:16:06 by mmkrtchy          #+#    #+#             */
/*   Updated: 2026/02/26 16:03:32 by mmkrtchy         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"
# include <limits.h>

typedef struct t_stck
{
	int				num;
	int				index;
	struct t_stck	*next;
	struct t_stck	*prev;
}					t_stack;

typedef struct t_funcs
{
	int				sa;
	int				sb;
	int				ss;
	int				pa;
	int				pb;
	int				ra;
	int				rb;
	int				rr;
	int				rra;
	int				rrb;
	int				rrr;
}					t_func_count;

typedef struct s_algo
{
	t_stack			*a;
	t_stack			*b;
	t_func_count	*count;
	int				*nums;
	int				size;
	int				disorder;
	int				mode;
	int				bench_flag;
}					t_algo;

int					check_duplicates(char **container);
int					duplicate_checker(int *number, int size);
int					check_no_num(char **container);
int					check_long_num(char **container);
int					mode_check(char *mode);
void				free_container(char **container);
int					filler(char **dest, char **src);
int					check_nums(char **argv, int start, int end);
int					error_checker(char **argv, int argc);

char				**filling_container(char **argv, int start, int argc);
void				char_to_int(char **container, int *numbers);
int					*filling_nums(char **argv, int start, int argc, int *count);
int					get_start(char **argv, int argc);

void				sa(t_stack **a, t_func_count *count, int c);
void				sb(t_stack **b, t_func_count *count, int c);
void				ss(t_stack **a, t_stack **b, t_func_count *count);
void				p_helper(t_stack *node, t_stack **push);
void				pa(t_stack **a, t_stack **b, t_func_count *count);
void				pb(t_stack **a, t_stack **b, t_func_count *count);
void				ra(t_stack **a, t_func_count *count);
void				rb(t_stack **b, t_func_count *count);
void				rr(t_stack **a, t_stack **b, t_func_count *count);
void				rra(t_stack **a, t_func_count *count);
void				rrb(t_stack **b, t_func_count *count);
void				rrr(t_stack **a, t_stack **b, t_func_count *count);

void				int_to_stack(int *nums, int size, t_stack **a);
int					get_index(int *numbers, int num);
int					*sort(int *nums, int size);
void				switch_ints(int *a, int *b);
int					compute_disorder(int *numbers, int size);

int					stack_size(t_stack *a);
int					find_position(t_stack *a, int target_index);
int					find_min_index(t_stack *a);
void				bring_index_to_top(t_stack **a, int target_index,
						t_func_count *count);
void				selection_sort(t_stack **a, t_stack **b,
						t_func_count *count);
int					is_sorted(t_stack *a);
void				free_stack(t_stack **stack);

int					get_chunk_fdist(t_stack *stack, int start, int end);
int					get_chunk_bdist(t_stack *stack, int start, int end);
int					get_max_ind(t_stack *stack);
int					get_back_dist(t_stack *stack, int index);
int					get_front_dist(t_stack *stack, int index);
int					get_chunk_step(int max_index);
void				bring_to_topa(t_stack **stack, int front, int back,
						t_func_count *count);
void				bring_to_topb(t_stack **stack, int front, int back,
						t_func_count *count);
void				fill_back(t_stack **a, t_stack **b, t_func_count *count);
void				chunk_sort(t_stack **a, t_stack **b, t_func_count *count);

int					max_bits(int size);
void				radix_sort(t_stack **a, t_stack **b, t_func_count *count);

void				execute_strategy(t_algo *algo);
void				init_algo_params(t_algo *algo, char **argv);
void				putstr_stderr(char *s);
void				putnbr_stderr(long n);
void				print_bench(t_algo *algo, char *strat);
char				*get_strategy_name(t_algo *algo);
void				print_ops(t_algo *algo);
int					get_total_ops(t_algo *algo);
void				print_disorder(int d);
void				print_strategy_total(char *strat, int total);
#endif