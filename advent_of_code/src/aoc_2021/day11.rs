use crate::aoc::space::{NGrid, Point};
use crate::Part;
use std::collections::HashSet;

fn flash(grid: &mut NGrid<i32, 2>, point: Point<2>, seen: &mut HashSet<Point<2>>) {
    if seen.contains(&point) {
        return;
    }
    seen.insert(point);
    for adjacent in grid.adjacent(&point) {
        let adj_value = grid.get(&adjacent);
        if adj_value.is_none() {
            continue;
        }
        let adj_value = *adj_value.unwrap();
        grid.set(adjacent, adj_value + 1);
        // Recursive flash
        if adj_value > 9 {
            flash(grid, point, seen);
        }
    }
}

fn simulate(grid: &mut NGrid<i32, 2>, until: Option<i32>) -> i32 {
    let mut flashes = 0;
    let mut steps = 0;
    loop {
        // Increment all points on grid
        for (point, value) in grid.points().clone() {
            let value = value + 1;
            grid.set(point, value);
        }
        // Begin chain of "flashes"
        let mut seen: HashSet<Point<2>> = HashSet::new();
        loop {
            let last_seen = grid.points().clone();
            for (point, _) in grid.points().clone() {
                let value = *grid.get(&point).unwrap_or(&0);
                if value > 9 {
                    flash(grid, point, &mut seen);
                }
            }
            if grid.points().clone() == last_seen {
                break;
            }
        }
        let mut num_flashed = 0;
        // Reset all "flashed" to 0
        for (point, value) in grid.points().clone() {
            if value > 9 {
                flashes += 1;
                num_flashed += 1;
                grid.set(point, 0);
            }
        }
        steps += 1;
        match until {
            Some(step) => {
                if steps >= step {
                    break;
                }
            }
            None => {
                if num_flashed == grid.points().len() {
                    return steps;
                }
            }
        }
    }
    flashes
}

pub fn solve(data: &str, part: &Part) -> String {
    let mut grid: NGrid<i32, 2> = NGrid::new(None);
    // Populate initial grid
    for (y, row) in data.lines().enumerate() {
        for (x, c) in row.chars().enumerate() {
            grid.set([x as i32, y as i32], c.to_digit(10).unwrap() as i32)
        }
    }
    let flashes = simulate(&mut grid, Some(100));
    let synchronized = simulate(&mut grid, None) + 100;
    return match part {
        Part::A => flashes.to_string(),
        Part::B => synchronized.to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526";
        assert_eq!(self::solve(input, &Part::A), "1656");
        assert_eq!(self::solve(input, &Part::B), "195");
    }
}
