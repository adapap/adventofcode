use std::env;
mod aoc;
// Import all puzzle solutions
mod aoc_2021;

pub struct Puzzle {
    year: String,
    day: String,
}

#[derive(Debug)]
pub enum Part {
    A,
    B,
}

#[tokio::main]
async fn main() {
    // Handle CLI arguments
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        println!("Usage: cargo run <year> <day + part> [-s, --submit]");
        return;
    }
    let submit_flag = args.contains(&"-s".to_string()) || args.contains(&"--submit".to_string());
    let year = String::from(&args[1]);
    let day = String::from(&args[2][0..&args[2].len() - 1]);
    let part = match String::from(&args[2][&args[2].len() - 1..]).as_str() {
        "a" => Part::A,
        "b" => Part::B,
        _ => {
            println!("error: part must be either 'a' or 'b'");
            return;
        }
    };
    let puzzle = Puzzle { year, day };
    let data = aoc::input::read(&puzzle).await;
    if data.is_none() {
        return;
    }
    let answer = match puzzle.year.as_str() {
        "2021" => aoc_2021::solve(&puzzle.day.as_str(), &data.unwrap(), &part),
        _ => {
            println!("error: invalid year {}", puzzle.year);
            return;
        }
    };
    println!("{} Day {}{:?}: {}", puzzle.year, puzzle.day, part, answer);
    if submit_flag {
        aoc::input::submit(&puzzle, &part, &answer).await;
    }
}
