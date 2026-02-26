*This project has been created as part of the 42 curriculum by mmkrtchy, rmesropy*

# Push Swap

## DESCRIPTION                                  


Push_swap is an algorithmic project whose objective is to sort a stack of
integers using two stacks (a and b) and a limited set of operations:

    sa, sb, ss
    pa, pb
    ra, rb, rr
    rra, rrb, rrr

The goal is to generate the smallest possible sequence of Push_swap operations
that sorts stack a in ascending order.

This project focuses on:
    • Algorithmic complexity (Big-O in operation model)
    • Strategy selection based on input disorder
    • Operation-count optimization
    • Runtime strategy selection


## PROJECT RULES                                 

- Language: C
- No global variables
- Compilation flags: -Wall -Wextra -Werror
- Memory leaks forbidden
- Errors must print "Error\n" to stderr
- Duplicate numbers forbidden
- Only allowed external functions:
      read, write, malloc, free, exit
      ft_printf (self-implemented)

Program name: push_swap
Bonus program: checker


## DISORDER METRIC                                


Disorder is measured BEFORE performing any operations.

It is defined as:

    mistakes / total_pairs

Where:

    For every pair (i, j), i < j:
        If a[i] > a[j] → mistake++

Value range:

    0.0   → already sorted
    1.0   → reverse sorted (worst case)

This metric determines the adaptive strategy.


## IMPLEMENTED STRATEGIES                            
  


We implemented the following strategies:

## 1. SIMPLE STRATEGY — O(n²)

Algorithm: Selection Sort adaptation

Principle:

    - Repeatedly find minimum element in stack a
    - Push it to stack b
    - Restore sorted order back to a

Operation Complexity:

    Each extraction costs O(n)
    Repeated n times → O(n²)

Why chosen:

    - Deterministic
    - Easy to control
    - Good for small inputs or nearly sorted data

Forced with:

    --simple


## 2. MEDIUM STRATEGY — O(n√n)


Algorithm: Chunk-Based Sorting

Principle:

    - Divide sorted index space into √n chunks
    - Push elements chunk by chunk to stack b
    - Reinsert in optimal order

Complexity Justification:

    - √n chunks
    - Each chunk handles O(n) operations
    → O(n√n)

Why chosen:

    - Good tradeoff for medium disorder
    - Significantly reduces operation count vs O(n²)
    - Performs well for 100–500 elements

Forced with:

    --medium

## 3. COMPLEX STRATEGY — O(n log n)


Algorithm: Radix Sort (LSD Binary)

Principle:

    - Index elements
    - Sort bit-by-bit using pb and ra
    - Repeat for log₂(n) bits

Complexity Justification:

    - For each bit: O(n)
    - Number of bits: log₂(n)
    → O(n log n)

Why chosen:

    - Very stable operation count
    - Excellent performance on large random inputs
    - Predictable upper bound

Forced with:

    --complex

## 4. ADAPTIVE STRATEGY


Based on measured disorder:

    disorder < 0.2         → O(n²)  (Selection Sort)
    0.2 ≤ disorder < 0.5   → O(n√n) (Chunk Sort)
    disorder ≥ 0.5         → O(n log n) (Radix)

Rationale:

Low disorder:

    Few inversions → quadratic method efficient enough

Medium disorder:

    Balanced partitioning improves efficiency

High disorder:

    Need logarithmic scaling to avoid explosion in operations

Default behavior:

    --adaptive


# PROGRAM USAGE                                 
  


Compile:

    make

Run:

    ./push_swap [strategy_flag] numbers...

Strategy Flags:

    --simple
    --medium
    --complex
    --adaptive (default)

Example:

    ./push_swap --complex 4 67 3 87 23

Benchmark mode:

    --bench

Example:

    ./push_swap --adaptive --bench 5 1 4 2 3

Benchmark outputs (stderr):

    - Disorder (%)
    - Strategy name
    - Theoretical complexity
    - Total operation count
    - Count per instruction


## PERFORMANCE TARGETS                               
  


For 100 numbers:

    < 2000  (minimum)
    < 1500  (good)
    < 700   (excellent)

For 500 numbers:

    < 12000 (minimum)
    < 8000  (good)
    < 5500  (excellent)

Our radix strategy satisfies excellent thresholds.

  
## RESOURCES                                  
  


Algorithm References:

    - Big-O Notation (Wikipedia)
    - Radix Sort documentation
    - Stack Abstract Data Type documentation

AI Usage:

    - Used for brainstorming chunk size strategies
    - Used for complexity validation discussion
    - Used for documentation structure drafting
    - All algorithms were manually implemented and fully understood

Peer Review:

    - Strategies validated through benchmarking
    - Operation counts tested against official checker
    - Code reviewed collaboratively


  
## CONTRIBUTION SUMMARY                            
  


rmesropy:

    - Selection sort implementation
    - Right mode activation
    - Benchmark output system

mmkrtchy:

    - Chunk sort implementation
    - Radix implementation
    - Parsing system

Both:

    - Optimization
    - Testing & debugging
## Thank You!