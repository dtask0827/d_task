# https://github.com/Domurba/Codewars_katas/blob/master/python/5_kyu/Directions_Reduction--by_Kolhelma--.py
# solved a similar codewars problem a while back when I was learning.
# also build an ETL-ish type pipeline, which takes my codewars solutions and psuhes them to github https://github.com/Domurba/CW_pipeline
# this solution is optimal because it iterates over the list only once, so should be O(n).
# Timing multiple loops or using %timeit in ipynb would give us an idea on how different solutions perform.


# import time
MATCHING = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}


def pathReduc(directions: list) -> list:
    """
    Should be named path_reduc
    Takes a list of directions and removes unnecessary paths

    :param directions: list of UPPERCASE strings representing the directions. E.g. "NORTH", "SOUTH", "EAST", "WEST"
    :return: list of strings representing the simplified directions 
    """
    reduced = []
    for i in directions:
        if reduced and MATCHING[i] == reduced[-1]:
            reduced.pop()
        else:
            reduced.append(i)
    return reduced


# def time_func(func, args, num_loops=5000000):
#     start_time = time.time()
#     for _ in range(num_loops):
#         func(args)
#     print(time.time() - start_time)


# time_func(pathReduc, ["NORTH", "EAST", "EAST",
#           "WEST", "NORTH", "NORTH", "SOUTH"])
