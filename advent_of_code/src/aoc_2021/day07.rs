use crate::Part;
use std::cmp;

fn min_dist(crabs: &Vec<i32>, constant: bool) -> i32 {
  let mut min = i32::MAX;
  let start: i32 = *crabs.iter().min().unwrap();
  let end: i32 = *crabs.iter().max().unwrap();
  for n in start..=end {
    let mut sum = 0;
    for crab in crabs {
      // Part A adds |B - A|
      // Part B adds sum(1..|B - A|)
      let mut diff = (crab - n).abs();
      if !constant {
        diff = ((diff + 1) * diff) / 2;
      }
      sum += diff;
    }
    min = cmp::min(sum, min);
  }
  min
}

pub fn solve(data: &str, part: &Part) -> String {
  let crabs: Vec<i32> = data.trim().split(',').map(|x| x.parse().unwrap()).collect();
  return match part {
    Part::A => min_dist(&crabs, true).to_string(),
    Part::B => min_dist(&crabs, false).to_string(),
  };
}
