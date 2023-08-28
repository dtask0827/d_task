import heapq
# import time

def count_and_min(value_list):
    min_value = float("inf")
    for val in value_list:
        if val < min_value:
            min_value = val
            count = 1
        elif val == min_value:
            count += 1
    return (count, min_value)


def computeCheckoutTime_1(customers, n):
    """
    Should be named compute_checkout_time
    less efficient but more intuitive sollution.
    """
    if customers == []:
        return 0
    time_spent = 0
    queue_left = n
    customers_in_queue = []
    for cust in customers:
        if queue_left > 0:
            customers_in_queue.append(cust)
            queue_left -= 1
        else:
            # can be multiple at once, so we need it and count
            queue_left, first_to_checkout = count_and_min(customers_in_queue)
            time_spent += first_to_checkout
            customers_in_queue = [
                c - first_to_checkout
                for c in customers_in_queue
                if c != first_to_checkout
            ]
            customers_in_queue.append(cust)
            queue_left -= 1
    time_spent += max(customers_in_queue)
    return time_spent


def computeCheckoutTime_2(customers: list, n: int) -> int:
    """
    I believe this is the most efficient solution possible. Fails if n == 0.
    It uses the heap data structure, which is a binary tree, where the first value is smallest.
    We fill the counters completely, and then keep adding the next customer to the 1st node in the heap (min value)
    The max value returned will be the last counter to have a person check out.

    :param customers: : an array of positive integers representing the customers. Each integer represents a customer, and its value is the amount of time they require to check out.
    :return: a positive integer, the number of checkout counters.
    """
    checkout_counters = [0] * n
    for cust in customers:
        heapq.heapreplace(checkout_counters, checkout_counters[0] + cust)
    return max(checkout_counters)


# def time_func(func, args, num_loops=5000):
#     start_time = time.time()
#     for _ in range(num_loops):
#         func(*args)
#     print(time.time() - start_time)


# time_func(computeCheckoutTime_1, ([49, 49, 38, 33, 43, 9, 14, 12, 31, 42, 33, 49], 5))
# time_func(computeCheckoutTime_2, ([49, 49, 38, 33, 43, 9, 14, 12, 31, 42, 33, 49], 5))
