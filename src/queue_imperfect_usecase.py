from src.queue_imperfect import QueueMatchmaking


def matchmake(queue: QueueMatchmaking, user: tuple[str, str]):
    name, action = user
    if action == "leave":
        queue.search_and_remove(name)
    elif action == "join":
        queue.push(name)
    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    return "No match found"
