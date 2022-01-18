use crate::Part;
use std::collections::HashMap;

pub fn solve(data: &str, part: &Part) -> String {
    let pairs = HashMap::from([(')', '('), (']', '['), ('}', '{'), ('>', '<')]);
    let char_score = HashMap::from([(')', 3), (']', 57), ('}', 1197), ('>', 25137)]);
    let autocomplete_score = HashMap::from([('(', 1), ('[', 2), ('{', 3), ('<', 4)]);
    let mut stack: Vec<char>;
    let mut score = 0;
    let mut autocomplete_scores: Vec<i64> = vec![];
    for line in data.lines() {
        stack = vec![];
        let mut corrupted = false;
        for c in line.chars() {
            if pairs.contains_key(&c) {
                let pair = *pairs.get(&c).unwrap();
                if stack.pop().unwrap_or('.') != pair {
                    score += char_score.get(&c).unwrap();
                    corrupted = true;
                    break;
                }
            } else {
                stack.push(c)
            }
        }
        if !corrupted {
            let mut total: i64 = 0;
            while !stack.is_empty() {
                total *= 5;
                total += autocomplete_score[&stack.pop().unwrap()];
            }
            autocomplete_scores.push(total);
        }
    }
    autocomplete_scores.sort();

    return match part {
        Part::A => score.to_string(),
        Part::B => autocomplete_scores[autocomplete_scores.len() / 2].to_string(),
    };
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = "[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]";
        assert_eq!(self::solve(input, &Part::A), "26397");
        assert_eq!(self::solve(input, &Part::B), "288957");
    }
}
