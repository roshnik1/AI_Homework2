import queue

# Class for the Notes (or vertices) of our Graph


class Location:
    def __init__(self, new_location):
        self.location = new_location
        self.adjacent_roads = {}

    def add_road(self, road, weight=0):
        self.adjacent_roads[road] = weight

    def get_roads(self):
        return self.adjacent_roads.keys()

    def get_location(self):
        return self.location

    def get_weight(self, road):
        return self.adjacent_roads[road]

# Class for the Graph of Romania


class WeightedGraph:
    def __init__(self):
        self.cities = {}
        self.total_cities = 0

    def __iter__(self):
        return iter(self.cities.values())

    def add_city(self, new_city):
        self.total_cities = self.total_cities + 1
        new_location = Location(new_city)
        self.cities[new_city] = new_location
        return new_location

    # Use this function to build the WeightedGraph
    def add_roads(self, start, end, weight=0):
        if start not in self.cities:
            self.add_city(start)
        if end not in self.cities:
            self.add_city(end)
        # Add (both) roads to the Locations
        # TODO: do we need both directions in the Graph?
        self.cities[start].add_road(self.cities[end], weight)
        self.cities[end].add_road(self.cities[start], weight)

    def get_cities(self):
        return self.cities.keys()


def goalTest(current_city, goal_city):
    if current_city.get_location() == goal_city.get_location():
        return True
    else:
        return False


def breadthFirstSearch(starting_city, goal_city):
    # TODO: Solution is more akin to explored list - make it only the shortest path taken
    print(starting_city.get_location() + ' --> ' + goal_city.get_location())
    solution = queue.Queue()

    solution.put(starting_city.get_location())

    # Solution is complete if start/end city are the same
    if goalTest(starting_city, goal_city):
        return solution

    frontier = queue.Queue()
    frontier.put(starting_city)
    explored = []

    while True:
        # Failure State, return empty path as solution
        if frontier.empty():
            return queue.Queue()

        # Explore first city in frontier
        current_city = frontier.get()
        explored.append(current_city)

        # Find neighboring cities that haven't been explored nor planning to be explored
        for road in current_city.get_roads():
            if road not in explored and road not in frontier.queue:
                # TODO: Don't add to solution yet
                solution.put(road.get_location())
                # If it's the place we're looking for, we're done
                if goalTest(road, goal_city):
                    return solution

                # Otherwise, it'll be explored
                frontier.put(road)

    # TODO: Performance metrics in terms of # explored
    # TODO: Performance metrics in terms of distance in solution


def depthFirstSearch(starting_city, goal_city):
    # TODO: Use solution instead of explored
    print(starting_city.get_location() + ' --> ' + goal_city.get_location())

    explored = [starting_city]

    # Solution is complete if start/end city are the same
    if goalTest(starting_city, goal_city):
        return explored

    frontier = queue.LifoQueue()
    frontier.put(starting_city)
    explored = []

    while True:
        # Failure State, return empty path as solution
        if frontier.empty():
            return []

        # Explore first city in frontier
        current_city = frontier.get()
        explored.append(current_city)

        # Find neighboring cities that haven't been explored nor planning to be explored
        for road in current_city.get_roads():
            if road not in explored and road not in frontier.queue:
                # If it's the place we're looking for, we're done
                if goalTest(road, goal_city):
                    explored.append(road)
                    return explored

                # Otherwise, it'll be explored
                frontier.put(road)

    # TODO: Performance metrics in terms of # explored
    # TODO: Performance metrics in terms of distance in solution


if __name__ == '__main__':
    # Build Graph
    romania = WeightedGraph()

    # Add the roads in Romania from east to west, and then north to south
    romania.add_roads('Oradea', 'Zerind', 71)
    romania.add_roads('Oradea', 'Sibiu', 151)
    romania.add_roads('Zerind', 'Arad', 75)
    romania.add_roads('Arad', 'Timisoara', 118)
    romania.add_roads('Arad', 'Sibiu', 140)
    romania.add_roads('Timisoara', 'Lugoj', 111)
    romania.add_roads('Lugoj', 'Mehadia', 70)
    romania.add_roads('Mehadia', 'Drobeta', 75)
    romania.add_roads('Drobeta', 'Craiova', 120)
    romania.add_roads('Sibiu', 'Fagaras', 99)
    romania.add_roads('Sibiu', 'Rimnicu Vilcea', 80)
    romania.add_roads('Rimnicu Vilcea', 'Craiova', 146)
    romania.add_roads('Rimnicu Vilcea', 'Pitesti', 97)
    romania.add_roads('Craiova', 'Pitesti', 138)
    romania.add_roads('Fagaras', 'Bucharest', 211)
    romania.add_roads('Pitesti', 'Bucharest', 101)
    romania.add_roads('Giurgiu', 'Bucharest', 90)
    romania.add_roads('Bucharest', 'Urziceni', 85)
    romania.add_roads('Neamt', 'Iasi', 87)
    romania.add_roads('Urziceni', 'Hirsova', 98)
    romania.add_roads('Iasi', 'Vaslui', 92)
    romania.add_roads('Urziceni', 'Vaslui', 142)
    romania.add_roads('Hirsova', 'Eforie', 86)

    goal_city = romania.cities['Bucharest']

    # Print all of the roads in Romania
    for city in romania:
        # for road in city.get_roads():
        #     starting_city = city.get_location()
        #     ending_city = road.get_location()
        #     print(starting_city, ending_city, city.get_weight(road))

        print(breadthFirstSearch(city, goal_city).queue)

        for x in depthFirstSearch(city, goal_city):
            print(x.get_location())

# TODO: aStarSearch()
# TODO: bestFirstSearch()

# TODO: Comments on correctness/efficiency as outlined at top of page 2