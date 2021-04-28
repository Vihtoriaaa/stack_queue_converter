"""Queue to stack converter."""
from arraystack import ArrayStack
import copy


def queue_to_stack(queue):
    """Converts queue to a stack"""
    output_stack = ArrayStack()
    start_queue = copy.deepcopy(queue)
    temporary_stack = ArrayStack()

    while start_queue.isEmpty() is False:
        elem = start_queue.pop()
        temporary_stack.push(elem)

    while temporary_stack.isEmpty() is False:
        elem = temporary_stack.pop()
        output_stack.push(elem)

    return output_stack
