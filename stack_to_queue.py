"""Stack to queue converter."""
from arrayqueue import ArrayQueue
import copy


def stack_to_queue(stack):
    """Converts stack to a queue"""
    start_stack = copy.deepcopy(stack)
    output_queue = ArrayQueue()

    while start_stack.isEmpty() is False:
        elem = start_stack.pop()
        output_queue.add(elem)

    return output_queue
