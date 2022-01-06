use crate::Part;

fn deduce_output(inputs: &Vec<&str>, output: &Vec<&str>) -> i32 {
    // Deduce '1' and '4' character sets
    let seg1 = inputs.iter().filter(|&x| x.len() == 2).next().unwrap();
    let seg4 = inputs.iter().filter(|&x| x.len() == 4).next().unwrap();
    let mut total = 0;
    let mut base = 1000;
    for &out in output {
        total += base
            * match (
                out.len(),
                out.chars().filter(|&x| seg1.contains(x)).count(),
                out.chars().filter(|&x| seg4.contains(x)).count(),
            ) {
                (6, 2, 3) => 0,
                (2, _, _) => 1,
                (5, 1, 2) => 2,
                (5, 2, 3) => 3,
                (4, _, _) => 4,
                (5, 1, 3) => 5,
                (6, 1, 3) => 6,
                (3, _, _) => 7,
                (7, _, _) => 8,
                (6, 2, 4) => 9,
                _ => panic!("invalid number"),
            };
        base /= 10;
    }
    total
}

pub fn solve(data: &str, part: &Part) -> String {
    let entries: Vec<&str> = data.trim().split("\n").collect();
    let mut count_1478 = 0;
    let segment_sizes: [usize; 4] = [2, 3, 4, 7];
    let mut total = 0;
    for entry in entries {
        let entry: Vec<&str> = entry.trim().split(" | ").collect();
        let inputs: Vec<&str> = entry[0].trim().split_whitespace().collect();
        let output: Vec<&str> = entry[1].trim().split_whitespace().collect();
        count_1478 += output
            .iter()
            .filter(|x| segment_sizes.contains(&x.len()))
            .count();
        total += deduce_output(&inputs, &output);
    }
    return match part {
        Part::A => count_1478.to_string(),
        Part::B => total.to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input =
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce";
        assert_eq!(self::solve(input, &Part::A), "26");
        assert_eq!(self::solve(input, &Part::B), "61229");
    }
}
