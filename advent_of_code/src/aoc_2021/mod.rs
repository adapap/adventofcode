use crate::Part;

mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;
mod day08;
mod day09;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;
mod day15;
mod day16;
mod day17;
mod day18;
mod day19;
mod day20;
mod day21;
mod day22;
mod day23;
mod day24;
mod day25;

pub fn solve(day: &str, data: &str, part: &Part) -> String {
    return match day {
        "1" => day01::solve(&data, &part),
        "2" => day02::solve(&data, &part),
        "3" => day03::solve(&data, &part),
        "4" => day04::solve(&data, &part),
        "5" => day05::solve(&data, &part),
        "6" => day06::solve(&data, &part),
        "7" => day07::solve(&data, &part),
        "8" => day08::solve(&data, &part),
        "9" => day09::solve(&data, &part),
        "10" => day10::solve(&data, &part),
        "11" => day11::solve(&data, &part),
        // "12" => day12::solve(&data, &part),
        // "13" => day13::solve(&data, &part),
        // "14" => day14::solve(&data, &part),
        // "15" => day15::solve(&data, &part),
        // "16" => day16::solve(&data, &part),
        // "17" => day17::solve(&data, &part),
        // "18" => day18::solve(&data, &part),
        // "19" => day19::solve(&data, &part),
        // "20" => day20::solve(&data, &part),
        // "21" => day21::solve(&data, &part),
        // "22" => day22::solve(&data, &part),
        // "23" => day23::solve(&data, &part),
        // "24" => day24::solve(&data, &part),
        // "25" => day25::solve(&data, &part),
        _ => unimplemented!("day {} in year {}", day, "2021"),
    };
}
