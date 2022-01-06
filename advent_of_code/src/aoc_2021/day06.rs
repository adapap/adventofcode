use crate::Part;

fn simulate(data: &Vec<i32>, days: i32) -> i64 {
    const REPEAT: usize = 7;
    let mut fish = [0; REPEAT + 2];
    for f in data {
        fish[*f as usize] += 1;
    }
    for _ in 0..days {
        fish[..].rotate_left(1);
        fish[REPEAT - 1] += fish[REPEAT + 1];
    }
    fish.iter().sum::<i64>()
}

pub fn solve(data: &str, part: &Part) -> String {
    let data: Vec<i32> = data.trim().split(',').map(|x| x.parse().unwrap()).collect();
    return match part {
        Part::A => simulate(&data, 80).to_string(),
        Part::B => simulate(&data, 256).to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "3,4,3,1,2";
        assert_eq!(self::solve(input, &Part::A), "5934");
        assert_eq!(self::solve(input, &Part::B), "26984457539");
    }
}
