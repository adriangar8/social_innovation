# Social Innovation - Energy Saving in Quantum Computing
Our project aims to find a preliminary answer to the general efficiency comparison of quantum com-
puting against traditional computing by evaluating the computation speed, the result accuracy and
the energy consumption among other equally important aspects. To deal with this comparison the
core of the Travelling Salesman Problem (TSP) has been coded and adapted for both quantum and
traditional paradigms. Other preliminary results indicate that quantum computing could lead to a
significant advantage in some specific problem domains with reduced computational complexity and
faster processing speeds. Further than that, our study explores the potential energy savings that
quantum systems can offer due to different operational principles. This research is looking forward
to highlight the practical benefits and limitations of the quantum computing paradigm and wants to
provide insights into future applications and integration with already existing technologies

## Repository structure
![alt text](docs/Cos.png)

# Travelling salesman problem 
The travelling salesman problem also known as TSP is a well known problem, and many algorithms has been proposed to solve it
## The problem:
We have a salseman that have to go through a set of cities, and it have to find the shortest path in order to travel through all the cities, by going to each city exactly once, and without repeating any city. This problem can be modeled as a graph where the nodes are the cities, and the edges between cities represent the distance between them. 
## Optimal Solution:
Many algorithms have been proposed to solve this problem, but the brute force solution of finding all the possible paths and traverse them to find the shortest one, is the only one guraranteed to find the optimal solution. This brute force solution is not very scalable because it is an NP-hard problem that has an exponential computional complexity, so the complexity rapidly explodes, consuming much more resources that what's feasibly possible to have. 
## Suboptimal Solutions:
Due to the NP-hard comlexity of the problem many suboptimal algorithms have been proposed in order to find suboptimal solutions to the problem, good enough to approximate the results. One of the most famous and best performing solutions is the Cristofides algorithm, that has a complexity of $n^2$


# Traditional 
