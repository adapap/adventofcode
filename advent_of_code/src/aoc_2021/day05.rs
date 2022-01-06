use crate::aoc::space::NGrid;
use crate::Part;

fn count_overlap(lines: &Vec<Vec<i32>>, ordinal: bool) -> i32 {
    let mut grid: NGrid<i32, 2> = NGrid::new(Some(0));
    for line in lines {
        let (x1, y1, x2, y2) = (line[0], line[1], line[2], line[3]);
        // Ignore lines that are not aligned with an axis for part A
        if x1 != x2 && y1 != y2 && !ordinal {
            continue;
        }
        let dx = (x2 - x1).signum();
        let dy = (y2 - y1).signum();
        let mut x = x1;
        let mut y = y1;
        grid.set([x, y], grid.get(&[x, y]).unwrap() + 1);
        while x != x2 || y != y2 {
            x += dx;
            y += dy;
            grid.set([x, y], grid.get(&[x, y]).unwrap() + 1);
        }
    }
    grid.points().iter().filter(|(_, &v)| v >= 2).count() as i32
}

pub fn solve(data: &str, part: &Part) -> String {
    // Parse input into vectors
    let lines: Vec<Vec<i32>> = data
        .trim()
        .split('\n')
        .map(|line| {
            line.split(" -> ")
                .map(|point| {
                    point
                        .split(',')
                        .map(|v| v.parse().expect("error: not a number"))
                        .collect::<Vec<i32>>()
                })
                .flatten()
                .collect()
        })
        .collect();
    return match part {
        Part::A => count_overlap(&lines, false).to_string(),
        Part::B => count_overlap(&lines, true).to_string(),
    };
}
