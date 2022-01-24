// Fetches and returns input for an Advent of Code puzzle
pub mod input {
    use crate::{Part, Puzzle};
    use dotenv_codegen::dotenv;
    use reqwest;
    use std::{error, fs, path::Path};

    static BASE_URL: &str = "https://adventofcode.com";

    fn get_token() -> String {
        String::from(dotenv!("AOC_TOKEN"))
    }

    async fn fetch(puzzle: &Puzzle) -> Result<String, Box<dyn error::Error>> {
        let token = get_token();
        let url = format!("{}/{}/day/{}/input", BASE_URL, puzzle.year, puzzle.day);
        let result = reqwest::Client::new()
            .get(url)
            .header("cookie", format!("session={}", token))
            .send()
            .await?;
        if result.status() != reqwest::StatusCode::OK {
            return Err("Check if token is expired and internet is connected".into());
        }
        Ok(result.text().await?)
    }

    pub async fn read(puzzle: &Puzzle) -> Option<String> {
        let day = format!("{:0>2}", puzzle.day);
        let path = format!("./src/aoc_{}/inputs/day{}.txt", puzzle.year, day);
        let path = Path::new(&path);
        // Check if file exists (cached), otherwise fetch from API
        if !path.exists() {
            match fetch(puzzle).await {
                Ok(data) => {
                    if let Err(_) = fs::write(path, data) {
                        println!("Failed to cache puzzle data");
                        return None;
                    }
                }
                Err(err) => {
                    println!("Failed to fetch puzzle data: {}", err);
                    return None;
                }
            }
        }
        // Read file as string
        if let Ok(data) = fs::read_to_string(path) {
            return Some(data);
        }
        None
    }

    pub async fn submit(puzzle: &Puzzle, part: &Part, data: &str) {
        let token = get_token();
        let url = format!("{}/{}/day/{}/answer", BASE_URL, puzzle.year, puzzle.day);
        let level = match part {
            Part::A => "1",
            Part::B => "2",
        };
        let payload = [("level", level), ("answer", data)];
        let response = reqwest::Client::new()
            .post(url)
            .header("cookie", format!("session={}", token))
            .form(&payload)
            .send()
            .await
            .unwrap_or_else(|err| {
                panic!("Failed to submit puzzle answer: {}", err);
            });
        let result = response
            .text()
            .await
            .unwrap_or_else(|err| panic!("Failed to convert response to text: {}", err));
        if result.contains("Your puzzle answer was") {
            println!("You already submitted an answer for day {}!", puzzle.day);
        } else if result.contains("That's the right answer") {
            println!(
                "Submitted correct answer for day {}! (Answer: {})",
                puzzle.day, &data
            );
        } else if result.contains("That's not the right answer")
            || result.contains("You need to actually provide an answer")
        {
            println!(
                "Incorrect answer for day {}! (Answer: {})",
                puzzle.day, &data
            );
        } else {
            println!(
                "Unexpected error while submitting answer. Response was:\n{}",
                result
            );
        }
    }
}

// Arithmetic operations, conversions, etc.
pub mod number {
    pub fn bin_to_i32(s: &str) -> i32 {
        isize::from_str_radix(s, 2).unwrap() as i32
    }
}

// Advanced iteration operations and functions on sequences
pub mod sequence {
    use itertools::{Itertools, MultiProduct};
    // Finds the cartesian product up to a k-length sequence
    // Example: [1 2] (k = 2) -> [1 1], [1 2], [2 1], [2 2]
    pub trait KProduct: Iterator + Clone
    where
        Self::Item: Clone,
    {
        fn k_product(self, repeat: usize) -> MultiProduct<Self> {
            std::iter::repeat(self)
                .take(repeat)
                .multi_cartesian_product()
        }
    }

    impl<T: Iterator + Clone> KProduct for T where T::Item: Clone {}
}

#[allow(unused)]
// Generic n-dimension grids and grid calculations
pub mod space {
    use super::sequence::KProduct;
    use std::cmp;
    use std::collections::HashMap;
    use std::hash::Hash;
    use std::ops::RangeInclusive;
    // Helper types and enums for NGrids
    #[derive(PartialOrd, PartialEq)]
    pub enum Axis {
        X = 0,
        Y = 1,
        Z = 2,
        W = 3,
    }
    pub type Point<const N: usize> = [i32; N];
    pub struct Bounds<const N: usize> {
        min: [i32; N],
        max: [i32; N],
    }
    impl<const N: usize> Bounds<N> {
        // Creates an empty bounds checker
        fn new() -> Bounds<N> {
            Bounds {
                min: [0; N],
                max: [0; N],
            }
        }
        // Calculates the size of a boundary on an axis
        pub fn size(&self, axis: usize) -> i32 {
            if axis >= N {
                panic!("error: cannot get bounds of axis {}", axis)
            }
            (self.max[axis] - self.min[axis]).abs() + 1
        }
        // An iterator over the range of x-values
        pub fn x_range(&self) -> RangeInclusive<i32> {
            self.min[0]..=self.max[0]
        }
        // An iterator over the domain of y-values
        pub fn y_range(&self) -> RangeInclusive<i32> {
            self.min[1]..=self.max[1]
        }
    }
    // NGrid Implementation
    pub struct NGrid<V, const N: usize> {
        pub bounds: Bounds<N>,
        default: Option<V>,
        points: HashMap<Point<N>, V>,
    }
    impl<V, const N: usize> NGrid<V, N>
    where
        V: std::fmt::Display,
    {
        // Create a new NGrid with an optional default value
        pub fn new(default: Option<V>) -> NGrid<V, N> {
            NGrid {
                bounds: Bounds::new(),
                default,
                points: HashMap::new(),
            }
        }
        // Set a point in the grid
        pub fn set(&mut self, point: Point<N>, value: V) {
            self.points.insert(point, value);
            // Update grid bounds
            for (i, val) in (0..=N).zip(point) {
                self.bounds.min[i] = cmp::min(self.bounds.min[i], val);
                self.bounds.max[i] = cmp::max(self.bounds.max[i], val);
            }
        }
        // Retrieve a point in the grid
        pub fn get(&self, point: &Point<N>) -> Option<&V> {
            return self.points.get(point).or(self.default.as_ref());
        }
        // Returns the points in the grid
        pub fn points(&self) -> &HashMap<Point<N>, V> {
            return &self.points;
        }
        // Returns all values matching the specified axis
        pub fn on_axis(&self, axis: usize, value: i32) -> Vec<(&Point<N>, &V)> {
            if axis >= N {
                panic!("error: axis is larger than dimensions")
            }
            self.points
                .iter()
                .filter(|(k, v)| k[axis] == value)
                .collect()
        }
        // Returns all points orthogonal to a point, if they exist
        pub fn cardinal(&self, origin: &Point<N>) -> Vec<Point<N>> {
            if N < 2 {
                panic!("error: need 2 dimensions to find cardinal neighbors");
            }
            let mut values = vec![];
            for delta in [-1, 1] {
                let mut point: Point<N> = origin.clone();
                point[0] += delta;
                values.push(point);
                let mut point: Point<N> = origin.clone();
                point[1] += delta;
                values.push(point);
            }
            values
        }
        // Returns all points adjacent to a point in any dimension
        pub fn adjacent(&self, origin: &Point<N>) -> Vec<Point<N>> {
            let mut values = vec![];
            let deltas = [-1, 0, 1];
            for delta in deltas.into_iter().k_product(N) {
                let mut point: Point<N> = origin.clone();
                for i in 0..N {
                    point[i] += delta[i];
                }
                // Ignore the origin
                if point == *origin {
                    continue;
                }
                values.push(point);
            }
            values
        }
        // Renders a 2D snapshot of the grid
        pub fn snapshot_2d(&self) -> String {
            if N != 2 {
                panic!("error: grid is not 2D")
            }
            let mut rows: Vec<String> = vec![];
            for y in self.bounds.y_range() {
                let mut row = String::new();
                for x in self.bounds.x_range() {
                    let mut point: Point<N> = [0; N];
                    point[0] = x;
                    point[1] = y;
                    match self.get(&point) {
                        Some(v) => row.push_str(&v.to_string()),
                        None => row.push(' '),
                    }
                }
                rows.push(row);
            }
            rows.join("\n")
        }
    }
}
