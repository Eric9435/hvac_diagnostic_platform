def build_priority_actions(recommendations: list[str]) -> list[str]:
    unique_actions = []
    for item in recommendations:
        if item not in unique_actions:
            unique_actions.append(item)
    return unique_actions[:8]
