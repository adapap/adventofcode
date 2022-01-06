use crate::aoc::space::{Axis, NGrid, Point};
use crate::Part;
use std::collections::HashSet;

struct Board {
    data: NGrid<i32, 2>,
    marked: HashSet<Point<2>>,
    had_bingo: bool,
}

impl Board {
    fn new(data: Vec<Vec<i32>>) -> Board {
        let mut grid = NGrid::new(None);
        for (i, row) in data.into_iter().enumerate() {
            for (j, v) in row.into_iter().enumerate() {
                grid.set([i as i32, j as i32], v);
            }
        }
        let marked = HashSet::new();
        Board {
            data: grid,
            marked,
            had_bingo: false,
        }
    }
    fn mark_num(&mut self, n: i32) {
        for (k, v) in self.data.points() {
            if n == *v {
                self.marked.insert(*k);
            }
        }
    }
    fn check_bingo(&self) -> bool {
        let height = self.data.bounds.size(Axis::Y as usize);
        let width = self.data.bounds.size(Axis::X as usize);
        // Check horizontal
        for y in 0..height {
            let mut count = 0;
            for x in 0..width {
                if self.marked.contains(&[x, y]) {
                    count += 1;
                }
            }
            if count == width {
                return true;
            }
        }
        // Check vertical
        for x in 0..width {
            let mut count = 0;
            for y in 0..height {
                if self.marked.contains(&[x, y]) {
                    count += 1;
                }
            }
            if count == height {
                return true;
            }
        }
        // Check diagonals
        for n in 0..width {
            let mut left_count = 0;
            let mut right_count = 0;
            if self.marked.contains(&[n, n]) {
                left_count += 1;
            }
            if self.marked.contains(&[width - n, n]) {
                right_count += 1;
            }
            if left_count == 5 || right_count == 5 {
                return true;
            }
        }
        false
    }
    fn answer(&self, last_draw: i32) -> i32 {
        let mut unmarked_sum = 0;
        for (p, v) in self.data.points() {
            if !self.marked.contains(p) {
                unmarked_sum += v;
            }
        }
        unmarked_sum * last_draw
    }
}

pub fn solve(data: &str, part: &Part) -> String {
    let data: Vec<&str> = data.split("\n\n").collect();
    let draw_order: Vec<i32> = data[0]
        .trim()
        .split(',')
        .map(|x| x.parse().expect("error: not a number"))
        .collect();
    let mut boards: Vec<Board> = data[1..]
        .into_iter()
        .map(|s| {
            s.trim()
                .split('\n')
                // Parse individual rows into numbers
                .map(|t| {
                    t.trim()
                        .split_whitespace()
                        .map(|u| u.parse().expect("error: not a number"))
                        .collect()
                })
                .collect()
        })
        .map(|b| Board::new(b))
        .collect();
    let mut answer_a: Option<i32> = None;
    let mut answer_b = 0;
    for (_, draw) in draw_order.iter().enumerate() {
        for board in &mut boards {
            if !board.had_bingo {
                board.mark_num(*draw);
                if board.check_bingo() {
                    answer_b = board.answer(*draw);
                    if answer_a.is_none() {
                        answer_a = Some(answer_b);
                    }
                    board.had_bingo = true;
                }
            }
        }
    }
    return match part {
        Part::A => answer_a.unwrap().to_string(),
        Part::B => answer_b.to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7";
        assert_eq!(self::solve(input, &Part::A), "4512");
        assert_eq!(self::solve(input, &Part::B), "1924");
    }
}
