class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        # Sort by position (largest position first)
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:

            # Time needed to reach target
            time = (target - pos) / spd

            # If current car takes longer,
            # it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

            # Else it joins the fleet ahead

        return len(stack)