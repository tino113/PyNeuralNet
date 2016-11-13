# PyNeuralNet
Python Implementation of a generalized neural net

# Plan - Generalized Neural Network framework

### Method
- Take x amount of input data
- Create y layers of abstraction
- Create \<z nodes in abstraction layer (where z is the number of nodes in the previous layer of abstraction)
- Assign random weights on connections between links between each consecutive layer of abstraction
- Extract results as desired output data
- Using differently randomly generated networks evaluate performance based on a fitness function f determined by success in the output layer
- Combine the most successful networks, maintain a healthy population of p by deleting networks with a fitness <= 0 and generating new networks to maintain population numbers
- Iterate until fitness becomes significantly high

### Training case 1
Train a neural network to as closely as possible mimic a given target image. Fitness being defined by percentage of pixels of a similar colour. (similarity defined by three factors, closeness in RGB or HLS)

### Structures Required
- **Nodes** (perform simple operations on all data fed by an axiom)
- **Axioms** (Weighted Links which feed data between nodes)
- **Abstraction Layer** (collections of nodes which are connected by axioms to all nodes of the previous layer and all nodes of the following layer)
- **Network** (collections of abstraction layers)

### Functions required
- **Fitness** (bespoke to each training case)
- **Mutate** (on a new birth there is a small chance of mutation of axiom weights, a smaller chance of creating a new node in an existing abstraction layer, and an even smaller chance of creating an entirely new abstraction layer)
- **Reproduce** (can be asexual or sexual, random weighting is used to determine the amount of genetic data shared between parents, may contain 1 to n partners (n.b. Not limited to 1 or 2 partners))
- **Generate** (generates a new random network, max layers, max nodes per layer and max axiom weighting can all be determined)
- **Input** (converts data from a source into nodes for first abstraction layer, Bespoke to different data types.)
- **Output** (converts data from a abstraction layer into data, bespoke for each data type.)


### Timing and Threading
Each Network runs on its own thread, each thread can take as long as it likes however they must all be compared by the fitness function at some point.

When all networks have finished evaluating (or when max time is reached) networks reproduce

Axioms and nodes run in loops

Abstraction layers larger than a certain size can be run as a multi threaded process
Axioms pass information between abstraction layers, nodes hold abstraction data relevant to their current cycle. Axioms hold data taken from the previous calculation cycle.

- Input layer converts information
- Axiom takes information from input layer, multiplies it by it’s internal weighting and holds the result
- The next layer requests data from the axiom and then performs all it’s calculation
- The next axiom requests data from it’s input layer, multiplies it by it’s internal weighting and holds the result.
- The process continues until all abstraction layers have been iterated
- The output process request data from the last layer of axioms and displays the result.

