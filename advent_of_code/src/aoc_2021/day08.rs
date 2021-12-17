use crate::Part;
use std::collections::{HashMap, HashSet};

fn deduce_output(inputs: &Vec<&str>, output: &Vec<&str>) -> i32 {
  let chars: HashSet<char> = "abcdefg".chars().collect();
  // Start with a mapping from char to possible char set
  let mut number_map: HashMap<i32, HashSet<char>> = HashMap::new();
  let mut char_map: HashMap<char, char> = HashMap::new();
  for (i, char) in chars.iter().enumerate() {
    number_map.insert(i as i32 + 1, chars.iter().copied().collect());
  }
  // Induction to resolve which number corresponds to which inputs
  // Simple terms: 1, 4, 7, 8 all have constant segment sizes (8 is useless)
  let const_segments = HashMap::from([(2, 1), (4, 4), (3, 7)]);
  for input in inputs {
    let input_chars: HashSet<char> = input.chars().collect();
    let n = input.len();
    if const_segments.contains_key(&n) {
      number_map.insert(const_segments[&n], input_chars);
    }
  }
  // A (top) is {7} - {4}
  char_map.insert(
    'a',
    *number_map[&7].difference(&number_map[&4]).next().unwrap(),
  );
  println!("Inputs: {:?}, Chars: {:?}", number_map, char_map);
  0
}

pub fn solve(data: &str, part: &Part) -> String {
  let entries: Vec<&str> = data.trim().split("\n").collect();
  let mut count_1478 = 0;
  let segment_sizes: [usize; 4] = [2, 3, 4, 7];
  for entry in entries {
    let entry: Vec<&str> = entry.trim().split(" | ").collect();
    let inputs: Vec<&str> = entry[0].trim().split_whitespace().collect();
    let output: Vec<&str> = entry[1].trim().split_whitespace().collect();
    count_1478 += output
      .iter()
      .filter(|x| segment_sizes.contains(&x.len()))
      .count();
    let output = deduce_output(&inputs, &output);
  }
  return match part {
    Part::A => count_1478.to_string(),
    Part::B => "".to_string(),
  };
}
