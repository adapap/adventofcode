use std::collections::HashSet;
use std::fmt;
use std::hash::Hash;

use crate::aoc::{path::Graph, sequence};
use crate::Part;

#[derive(PartialEq, Eq, Hash, Clone)]
struct Node {
    label: String,
    small: bool,
}

impl fmt::Debug for Node {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.label)
    }
}

impl Node {
    fn new(label: &str) -> Node {
        Node {
            label: String::from(label),
            small: label.to_lowercase() == label,
        }
    }
}

pub fn solve(data: &str, part: &Part) -> String {
    // Construct graph from data
    let mut graph = Graph::<Node>::new();
    for line in data.lines() {
        let edge: Vec<&str> = line.split("-").collect();
        graph.add_undirected_edge(Node::new(edge[0]), Node::new(edge[1]));
    }
    let is_goal = |node: &Node| node.label == "end";
    let is_valid = |nodes: &Vec<Node>| {
        let small: Vec<_> = nodes.into_iter().filter(|x| x.small).collect();
        HashSet::<&Node>::from_iter(small.clone()).len() == small.len()
    };
    let paths = graph.all_paths(Node::new("start"), is_goal, is_valid);
    let part_a = paths.len();
    let is_valid = |nodes: &Vec<Node>| {
        let counter = sequence::counter(nodes);
        let mut visited_twice = false;
        for (node, count) in counter {
            // Don't visit start/end more than once
            if (node.label == "start" || node.label == "end") && count > 1 {
                return false;
            }
            // Can only visit a small cave a maximum of two times
            if node.small && count >= 2 {
                if visited_twice || count > 2 {
                    return false;
                }
                visited_twice = true;
            }
        }
        true
    };
    let paths = graph.all_paths(Node::new("start"), is_goal, is_valid);
    return match part {
        Part::A => part_a.to_string(),
        Part::B => paths.len().to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "start-A
start-b
A-c
A-b
b-d
A-end
b-end";
        assert_eq!(self::solve(input, &Part::A), "10");
        assert_eq!(self::solve(input, &Part::B), "36");
    }
    #[test]
    fn test2() {
        let input = "dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc";
        assert_eq!(self::solve(input, &Part::A), "19");
        assert_eq!(self::solve(input, &Part::B), "103");
    }
    #[test]
    fn test3() {
        let input = "fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW";
        assert_eq!(self::solve(input, &Part::A), "226");
        assert_eq!(self::solve(input, &Part::B), "3509");
    }
}
