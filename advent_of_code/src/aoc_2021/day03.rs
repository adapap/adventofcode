use crate::{aoc, Part};
use std::collections::HashMap;

// Counts the number of bits at each index in the binary string, and returns the size of a binary string
fn count_bits(data: &Vec<&str>) -> (HashMap<(i32, char), i32>, i32) {
    // Keep track of counts of 0 and 1 at each index in <(index, char), count>
    let mut counts: HashMap<(i32, char), i32> = HashMap::new();
    // The length of one binary string
    let mut size = 0;
    for line in data {
        if size == 0 {
            size = line.len();
        }
        // Increment the key (index, char)
        for (i, char) in line.chars().enumerate() {
            *counts.entry((i as i32, char)).or_insert(0) += 1;
        }
    }
    (counts, size as i32)
}

// Returns whether a zero is more common at one index of the data
fn more_zeros_at(counts: &HashMap<(i32, char), i32>, i: i32) -> bool {
    return counts[&(i, '0')] > counts[&(i, '1')];
}

pub fn solve(data: &str, part: &Part) -> String {
    let data: &Vec<&str> = &data.split_whitespace().collect();
    let mut gamma_rate = String::new();
    let (counts, size) = count_bits(data);
    let mut max = 0b0;
    for i in 0..size {
        max += 0b1 << i;
        if more_zeros_at(&counts, i as i32) {
            gamma_rate.push('0');
        } else {
            gamma_rate.push('1');
        }
    }
    let gamma_rate = aoc::number::bin_to_i32(&gamma_rate);
    let epsilon_rate = max - gamma_rate;
    /* Part B */
    // Filter data by keys until there is one entry remaining
    let mut data_ = data.clone();
    let mut index = 0;
    while data_.len() > 1 {
        let mut match_char = '1';
        let (counts, _) = count_bits(&data_);
        if more_zeros_at(&counts, index as i32) {
            match_char = '0';
        }
        data_ = data_
            .into_iter()
            .filter(|x| x.chars().nth(index as usize).unwrap() == match_char)
            .collect();
        index += 1;
    }
    let oxygen_generator_rating = data_[0];
    data_ = data.clone();
    index = 0;
    while data_.len() > 1 {
        let mut match_char = '0';
        let (counts, _) = count_bits(&data_);
        if more_zeros_at(&counts, index as i32) {
            match_char = '1';
        }
        data_ = data_
            .into_iter()
            .filter(|x| x.chars().nth(index as usize).unwrap() == match_char)
            .collect();
        index += 1;
    }
    let co2_scrubber_rating = data_[0];
    let answer = aoc::number::bin_to_i32(&oxygen_generator_rating)
        * aoc::number::bin_to_i32(&co2_scrubber_rating);
    return match part {
        Part::A => format!("{}", gamma_rate * epsilon_rate),
        Part::B => format!("{}", answer),
    };
}
