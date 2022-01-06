use crate::Part;

// In this function, `i` and `j` represent the bounds of a sliding window on some array `a`
// The goal is to loop over using a window of size n. For example, a sliding window of length 3:
// [1 |2 4 6| 8], n = 3
//    |j   i|
fn sliding_window(a: &Vec<i32>, n: usize) -> i32 {
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut curr_sum = 0;
    let mut total = 0;
    while i < a.len() {
        // Sliding window reached maximum size
        if i - j == n {
            let next_sum = curr_sum + a[i] - a[j];
            // If the next window is greater than the current window, add to our total
            if next_sum > curr_sum {
                total += 1;
            }
            // Increment left pointer
            j += 1;
            curr_sum = next_sum;
        } else {
            // Window has not reached size n
            curr_sum += a[i];
        }
        // Increment right pointer
        i += 1;
    }
    return total;
}

pub fn solve(data: &str, part: &Part) -> String {
    let data: Vec<i32> = data
        .split_whitespace()
        .map(|x| x.parse().expect("error: not a number"))
        .collect();
    return match part {
        Part::A => sliding_window(&data, 1).to_string(),
        Part::B => sliding_window(&data, 2).to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "199
200
208
210
200
207
240
269
260
263";
        assert_eq!(self::solve(input, &Part::A), "7");
        assert_eq!(self::solve(input, &Part::B), "5");
    }
}
