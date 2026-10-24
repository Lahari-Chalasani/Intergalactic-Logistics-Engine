
# The Intergalactic Space-Courier Logistics Engine

## Project Description
This project models an intergalactic star-system network where planets and space stations are connected through hyperspace jump-lanes. Each route has a weight representing fuel consumption, solar storm hazards, or jump tolls.

## Algorithms Implemented
1.Dijkstra's Algorithm:Finds a minimum-cost route for standard space-courier missions.
2.Bellman-Ford Algorithm:Handles negative edge weights representing Quantum Rift Subsidies and temporal energy rebates.

## Features
-> Models planets and space stations as network nodes.
-> Represents hyperspace jump-lanes as edges.
-> Calculates optimal routes based on route costs.
-> Handles negative weights using Bellman-Ford.
-> Displays a Galactic Shipping Manifest with route checkpoints, costs, and hazard details.

## Technologies Used
 Python 3

## How to Run
1.Install Python 3.
2.Open the project folder in VS Code.
3.Open the terminal.
4.Run the following command:python main.py

## Expected Output
The program displays:
-> The standard route using Dijkstra's Algorithm.
-> The quantum rift route using Bellman-Ford Algorithm.
-> The Galactic Shipping Manifest with selected checkpoints and route costs.
