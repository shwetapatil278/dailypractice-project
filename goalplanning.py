
# Initial and goal states
state = ['A', 'B', 'C']
goal = ['C', 'B', 'A']

def goal_stack_planning(state, goal):
    stack = goal[::-1]
    plan = []

    while stack:
        block = stack.pop()

        if state.index(block) != goal.index(block):
            state.remove(block)
            state.insert(goal.index(block), block)
            plan.append("Move " + block)

    return plan

print("Initial State:", state)
print("Goal State:", goal)

plan = goal_stack_planning(state.copy(), goal)

for step in plan:
    print(step)

print("Goal Achieved!")
