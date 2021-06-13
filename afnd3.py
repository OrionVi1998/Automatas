# transitions = [
#     {"a": {1}},
#     {"b": {0, 2}},
#     {"c": {0}}
# ]

transitions = [
    {"a": {0, 1}},
    {"b": {2, 3}}
]

# NFA diagrama
# https://i.stack.imgur.com/GKQzg.png

starting_state = 0
accepting_states = {3}


def nfa2(palabra):
    cur_states = {starting_state}

    for char in palabra:
        if not cur_states:
            return "reject"

        # print(char, [transitions[s].get(char, set()) for s in cur_states])
        cur_states = set.union(*(transitions[s].get(char, set()) for s in cur_states))

    # print(cur_states, accepting_states)

    return "accept" if cur_states & accepting_states else "reject"


print(nfa2("abb"))
