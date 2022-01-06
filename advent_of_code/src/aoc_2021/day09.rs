use crate::aoc::space::{NGrid, Point};
use crate::Part;
use std::collections::HashSet;

fn flood_fill(grid: &NGrid<u32, 2>, origin: &Point<2>, seen: &mut HashSet<Point<2>>) {
    // Fill into cardinal directions
    let origin_value = *grid.get(&origin).unwrap();
    seen.insert(*origin);
    for point in grid.cardinal(origin) {
        if seen.contains(&point) {
            continue;
        }
        let value = *grid.get(&point).unwrap_or(&9);
        if value != 9 && value > origin_value {
            flood_fill(grid, &point, seen);
        }
    }
}

pub fn solve(data: &str, part: &Part) -> String {
    let mut grid: NGrid<u32, 2> = NGrid::new(None);
    for (y, row) in data.lines().enumerate() {
        for (x, char) in row.chars().enumerate() {
            grid.set(
                [x as i32, y as i32],
                char.to_digit(10).expect("error: not a number"),
            );
        }
    }
    // Calculate sum of low points
    let mut low_point_sum = 0;
    let mut low_points = vec![];
    for (point, cmp_val) in grid.points() {
        let is_low_point = grid.cardinal(point).iter().all(|p| {
            let v = grid.get(p);
            return v.is_none() || (v.unwrap() > cmp_val);
        });
        if is_low_point {
            low_point_sum += 1 + cmp_val;
            low_points.push(point);
        }
    }
    // Flood fill from all low points
    let mut region_sizes = vec![];
    for point in &low_points {
        let mut seen = HashSet::new();
        flood_fill(&grid, point, &mut seen);
        region_sizes.push(seen.len());
    }
    region_sizes.sort();
    region_sizes.reverse();
    let largest_basins = region_sizes[..3].iter().fold(1, |acc, x| acc * x);
    return match part {
        Part::A => low_point_sum.to_string(),
        Part::B => largest_basins.to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "2199943210
3987894921
9856789892
8767896789
9899965678";
        assert_eq!(self::solve(input, &Part::A), "15");
        assert_eq!(self::solve(input, &Part::B), "1134");
    }
}
