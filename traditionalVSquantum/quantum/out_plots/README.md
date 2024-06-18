# Output Plots: Best, Worst, and Average Runs Comparison

This folder contains plots depicting the performance comparison between the dummy model and the layer 1 model for solving the Traveling Salesman Problem (TSP) using quantum computing.

## Plots Description

### Dummy Model Performance

- **Max Dummy**: Shows the best run for the dummy model, by best it is understood that is the run where the average length was the minimum.
- **Min Dummy**: Shows the worst run for the dummy model, by worst it is understood that is the run where the average length was the maximum.
- **Dummy Avg**: Shows how would an average run look like using the dummy model.

### Layer 1 Model Performance

- **Max L = 1**: Shows the best run for the 1 Layer model, by best it is understood that is the run where the average length was the minimum.
- **Min L = 1**: Shows the worst run for the 1 Layer model, by worst it is understood that is the run where the average length was the maximum.
- **L = 1 Avg**: Shows how would an average run look like using the 1 Layer model.

## Usage

- **Viewing Plots**: Open the `.jpg` file using the legend provided to analyze the performance trends of the models.
- **Comparison**: Compare the plots between the dummy model and the layer 1 model to understand how additional layers impact performance. Further comparisions are explained in the paper.

![Plot](https://github.com/adriangar8/social_innovation/assets/132783746/174932cf-6088-448d-9e1a-c929aee29986)

## Notes

- These plots are generated based on the experimental results obtained from running the TSP solver using the specified models and parameters.
- The plots provide insights into the convergence and effectiveness of the models in solving TSP instances over multiple training episodes.
