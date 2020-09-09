const airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ');

const routes = [
  ['PHX', 'LAX'],
  ['PHX', 'JFK'],
  ['JFK', 'OKC'],
  ['JFK', 'HEL'],
  ['JFK', 'LOS'],
  ['MEX', 'LAX'],
  ['MEX', 'BKK'],
  ['MEX', 'LIM'],
  ['MEX', 'EZE'],
  ['LIM', 'BKK']
];

const graph = new Map();
function addAirport(source) {
  graph.set(source, []);
}
function addNode(source, destination) {
  graph.get(source).push(destination);
  graph.get(destination).push(source);
}
airports.forEach(addAirport);
routes.forEach(node => addNode(...node));
console.log(graph);

function findDestination(source, route, graph) {
  let queue = [source];
  let flag = false;
  let visited = new Set();

  while (queue.length > 0 || !flag) {
    let airport = queue.shift();
    destinations = graph.get(airport);
    for (const destination of destinations) {
      if (destination === route) {
        console.log('Found Airport!');
        flag = true;
        break;
      }
      if (!visited.has(destination)) {
        visited.add(destination);
        queue.push(destination);
      }
    }
  }
  return flag;
}

function dfs(source, goal, visited = new Set(), path = []) {
  console.log(source);
  destinations = graph.get(source);
  for (destination of destinations) {
    if (destination === goal) {
      console.log('Destination is found!');
    }
    if (!visited.has(destination)) {
      visited.add(destination);
      dfs(destination, goal, visited);
    }
  }
  console.log(path);

  return flag;
}

dfs('LAX', 'BKK');
