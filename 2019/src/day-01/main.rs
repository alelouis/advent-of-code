fn cost(fuel: i32) -> i32 {
    ((fuel as f32 / 3.).floor() - 2.) as i32
}

fn solve1() -> i32 {
    include_str!("input")
        .lines()
        .map(|x| x.parse::<i32>().unwrap())
        .map(|x| cost(x))
        .sum()
}

fn solve2() -> i32 {
    let input = include_str!("input");
    let mut ans = 0;
    for line in input.lines() {
        let mut c = cost(line.parse::<i32>().unwrap());
        let mut fuel = 0;
        while cost(c) >= 0 {
            c = cost(c);
            fuel += c;
        }
        ans += fuel;
    }
    ans
}

fn main() {
    println!("part-1 answer : {}", solve1());
    println!("part-2 answer : {}", solve2() + solve1());
}
