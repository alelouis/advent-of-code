fn read_input() -> Vec<i32> {
    include_str!("input")
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect()
}

fn solve1(data: &mut Vec<i32>, noun: i32, verb: i32) -> i32 {
    let mut head: usize = 0;
    data[1] = noun;
    data[2] = verb;
    loop {
        let op = data[head];
        let left = data[head + 1] as usize;
        let right = data[head + 2] as usize;
        let target = data[head + 3] as usize;
        head += 4;
        match op {
            1 => data[target] = data[left] + data[right],
            2 => data[target] = data[left] * data[right],
            99 => break,
            _ => (),
        }
    }
    data[0]
}

fn solve2(data: &mut Vec<i32>) -> i32 {
    let mut ans = 0;
    for noun in 0..=99 {
        for verb in 0..=99 {
            if solve1(&mut data.clone(), noun, verb) == 19690720 {
                ans = 100 * noun + verb;
            }
        }
    }
    ans
}

fn main() {
    let mut data = read_input();
    println!("part-1 answer : {}", solve1(&mut data.clone(), 12, 2));
    println!("part-2 answer : {}", solve2(&mut data));
}
