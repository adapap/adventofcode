use crate::Part;

// Keeps track of our submarine's position and depth as it moves around
struct Submarine {
  aim: i32,
  position: i32,
  depth: i32,
}

impl Submarine {
  fn answer(self) -> i32 {
    self.position * self.depth
  }
}

pub fn solve(data: &str, part: &Part) -> String {
  let data: Vec<&str> = data.split('\n').collect();
  // Initialize our submarine positions
  let mut submarine_1 = Submarine {
    aim: 0,
    position: 0,
    depth: 0,
  };
  let mut submarine_2 = Submarine {
    aim: 0,
    position: 0,
    depth: 0,
  };
  // Parse the input data instructions
  for line in data {
    if let Some((direction, amount)) = line.split_once(' ') {
      let amount: i32 = amount.parse().expect("error: amount is not a number");
      // Adjust submarine fields based on input command
      match direction {
        "up" => {
          submarine_1.depth -= amount;
          submarine_2.aim -= amount;
        }
        "down" => {
          submarine_1.depth += amount;
          submarine_2.aim += amount;
        }
        "forward" => {
          submarine_1.position += amount;
          submarine_2.position += amount;
          submarine_2.depth += submarine_2.aim * amount;
        }
        _ => panic!("error: invalid direction {}", direction),
      }
    }
  }
  return match part {
    Part::A => submarine_1.answer().to_string(),
    Part::B => submarine_2.answer().to_string(),
  };
}
