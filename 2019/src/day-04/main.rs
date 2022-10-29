fn is_adjacent(s: &String, part2: bool) -> bool {
    let mut adjacent: Vec<bool> = s
        .chars()
        .collect::<Vec<char>>()
        .windows(2)
        .map(|t| (t[0] == t[1]))
        .collect();

    return if part2 {
        adjacent.push(false);
        adjacent.insert(0, false);
        adjacent.windows(3).any(|t| !t[0] & t[1] & !t[2])
    } else {
        adjacent.iter().any(|t| *t)
    };
}

fn is_decreasing(s: &String) -> bool {
    s.chars()
        .collect::<Vec<char>>()
        .windows(2)
        .all(|t| t[0].to_digit(10) <= t[1].to_digit(10))
}

fn iter_number(start: i32, end: i32, part2: bool) -> i32 {
    (start..end)
        .map(|x| x.to_string())
        .map(|x| is_decreasing(&x) & is_adjacent(&x, part2))
        .map(|x| x as i32)
        .sum()
}

fn main() {
    let input = include_str!("input");
    let split = input.split("-").collect::<Vec<&str>>();
    let start: i32 = split[0].parse().unwrap();
    let end: i32 = split[1].parse().unwrap();

    println!("part-1: {:?}", iter_number(start, end, false));
    println!("part-2: {:?}", iter_number(start, end, true));
}
