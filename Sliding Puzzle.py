class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = ''.join(map(str, sum(board, [])))
        target = "123450"

        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            state, steps = queue.popleft()

            if state == target:
                return steps

            zero = state.index('0')

            for nxt in moves[zero]:
                arr = list(state)
                arr[zero], arr[nxt] = arr[nxt], arr[zero]
                new_state = ''.join(arr)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

        return -1
