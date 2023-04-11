def solution(H):
    stack = []
    block_count = 0
    for height in H:
        while len(stack) != 0 and height < stack[-1]:
            # If the height of current block is less than
            #    the previous ones, the previous ones have
            #    to end before current point. They have no
            #    chance to exist in the remaining part.
            # So the previous blocks are completely finished.
            print(f"found {height} less than last element of stack : {stack[-1]}")
            print(f"stack before: {stack}")
            stack.pop()
            block_count += 1
            print(f"stack after: {stack}; block_count : {block_count}")

        if len(stack) == 0 or height > stack[-1]:
            # If the height of current block is greater than
            #    the previous one, a new block is needed for
            #    current position.
            stack.append(height)
            print(f"stack added: {stack}")
        # Else (the height of current block is same as that
        #    of previous one), they should be combined to
        #    one block.
    # Some blocks with different heights are still in the stack.

    block_count += len(stack)
    return block_count


H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))
