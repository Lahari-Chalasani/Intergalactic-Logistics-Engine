
# Intergalactic Space-Courier Logistics Engine
# Computer Networks Assignment 2
# Algorithms: Dijkstra and Bellman-Ford

import heapq

# Space stations
STATIONS = ["Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

# Standard routes: (destination, fuel cost, hazard rating)
# All costs are non-negative for Dijkstra's algorithm.
STANDARD_ROUTES = {
    "Earth": [
        ("Mars", 4, 2),
        ("Jupiter", 10, 3)
    ],
    "Mars": [
        ("Jupiter", 3, 1),
        ("Saturn", 8, 4)
    ],
    "Jupiter": [
        ("Saturn", 2, 1),
        ("Neptune", 9, 3)
    ],
    "Saturn": [
        ("Neptune", 3, 1)
    ],
    "Neptune": []
}


def dijkstra(graph, source, destination):
    """Find the minimum-cost route using Dijkstra's algorithm."""
    distances = {station: float("inf") for station in graph}
    previous = {station: None for station in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        cost, current = heapq.heappop(priority_queue)

        if cost != distances[current]:
            continue

        if current == destination:
            break

        for neighbor, fuel, hazard in graph[current]:
            new_cost = cost + fuel + hazard

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current
                heapq.heappush(
                    priority_queue, (new_cost, neighbor)
                )

    if distances[destination] == float("inf"):
        return None, distances, previous

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances, previous


# Quantum Rift routes:
# (source, destination, adjusted cost)
# Negative costs represent temporal energy rebates.
RIFT_ROUTES = [
    ("Earth", "Mars", 5),
    ("Earth", "Jupiter", 12),
    ("Mars", "Jupiter", 4),
    ("Mars", "Saturn", 10),
    ("Jupiter", "Saturn", 3),
    ("Jupiter", "Neptune", 8),
    ("Saturn", "Neptune", -4)
]


def bellman_ford(stations, edges, source, destination):
    """Find the minimum-cost route with negative edges."""
    distances = {station: float("inf") for station in stations}
    previous = {station: None for station in stations}

    distances[source] = 0

    # Relax all edges at most V - 1 times.
    for _ in range(len(stations) - 1):
        changed = False

        for u, v, weight in edges:
            if distances[u] != float("inf"):
                candidate = distances[u] + weight

                if candidate < distances[v]:
                    distances[v] = candidate
                    previous[v] = u
                    changed = True

        if not changed:
            break

    # Check for a reachable negative-weight cycle.
    for u, v, weight in edges:
        if (
            distances[u] != float("inf")
            and distances[u] + weight < distances[v]
        ):
            return None, distances, previous, True

    if distances[destination] == float("inf"):
        return None, distances, previous, False

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances, previous, False


def print_manifest(title, path, total_cost, route_details):
    """Print a stylized Galactic Shipping Manifest."""
    print("\n" + "=" * 55)
    print("       GALACTIC SHIPPING MANIFEST")
    print("       INTERGALACTIC COURIER SERVICE")
    print("=" * 55)
    print("Mission:", title)
    print("Cargo: HIGH-PRIORITY INTERSTELLAR PACKAGE")
    print("-" * 55)

    if path is None:
        print("STATUS: NO VALID ROUTE FOUND")
        print("=" * 55)
        return

    print("Route:", " -> ".join(path))
    print("\nSTELLAR CHECKPOINTS:")

    for index, station in enumerate(path, start=1):
        print(f"  {index}. {station}")

    print("\nROUTE DETAILS:")

    for detail in route_details:
        print("  " + detail)

    print("-" * 55)
    print(f"Total adjusted route cost: {total_cost}")
    print("STATUS: ROUTE CALCULATED")
    print("       * SAFE TRAVELS, SPACE COURIER! *")
    print("=" * 55)


def main():
    # 1. Dijkstra demonstration
    path, distances, previous = dijkstra(
        STANDARD_ROUTES, "Earth", "Neptune"
    )

    standard_details = []
    if path:
        for u, v in zip(path, path[1:]):
            for neighbor, fuel, hazard in STANDARD_ROUTES[u]:
                if neighbor == v:
                    standard_details.append(
                        f"{u} -> {v}: fuel={fuel}, "
                        f"hazard={hazard}, cost={fuel + hazard}"
                    )
                    break

        print_manifest(
            "STANDARD FUEL-EFFICIENT MISSION",
            path,
            distances["Neptune"],
            standard_details
        )
    else:
        print_manifest(
            "STANDARD MISSION", None, 0, []
        )

    # 2. Bellman-Ford demonstration
    path, distances, previous, has_negative_cycle = bellman_ford(
        STATIONS, RIFT_ROUTES, "Earth", "Neptune"
    )

    if has_negative_cycle:
        print("\nWARNING: Reachable negative cycle detected!")
    elif path:
        rift_details = []

        for u, v in zip(path, path[1:]):
            for start, end, weight in RIFT_ROUTES:
                if start == u and end == v:
                    label = (
                        "quantum rebate"
                        if weight < 0 else "route cost"
                    )
                    rift_details.append(
                        f"{u} -> {v}: {label} = {weight}"
                    )
                    break

        print_manifest(
            "QUANTUM RIFT REBATE MISSION",
            path,
            distances["Neptune"],
            rift_details
        )
    else:
        print_manifest(
            "QUANTUM RIFT MISSION", None, 0, []
        )


if __name__ == "__main__":
    main()
