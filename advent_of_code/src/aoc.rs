// Fetches and returns input for an Advent of Code puzzle
pub mod input {
    use crate::Puzzle;
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
}

// Arithmetic operations, conversions, etc.
pub mod number {
    pub fn bin_to_i32(s: &str) -> i32 {
        isize::from_str_radix(s, 2).unwrap() as i32
    }
}

#[allow(unused)]
// Generic n-dimension grids and grid calculations
pub mod space {
    use std::cmp;
    use std::collections::HashMap;
    use std::hash::Hash;
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
    }
    // NGrid Implementation
    pub struct NGrid<V, const N: usize> {
        pub bounds: Bounds<N>,
        default: Option<V>,
        points: HashMap<Point<N>, V>,
    }
    impl<V, const N: usize> NGrid<V, N> {
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
                panic! {"error: axis is larger than dimensions"}
            }
            self.points
                .iter()
                .filter(|(k, v)| k[axis] == value)
                .collect()
        }
    }
}
