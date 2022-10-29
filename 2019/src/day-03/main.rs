use std::cmp;

#[derive(Debug, Clone, Copy)]
struct Position {
    x: i32,
    y: i32,
}

#[derive(Debug, Clone, Copy)]
struct Line {
    start: Position,
    end: Position,
}

fn get_lines(cable: Vec<&str>) -> Vec<Line> {
    let mut lines: Vec<Line> = Vec::new();
    let mut startp = Position { x: 0, y: 0 };
    for instruction in cable {
        let direction = &instruction[0..1];
        let amount = &instruction[1..].parse().unwrap();
        let endp = match direction {
            "R" => Position {
                x: &startp.x + amount,
                y: startp.y,
            },
            "L" => Position {
                x: startp.x - amount,
                y: startp.y,
            },
            "U" => Position {
                x: startp.x,
                y: startp.y + amount,
            },
            "D" => Position {
                x: startp.x,
                y: startp.y - amount,
            },
            _ => panic!(),
        };
        lines.push(Line {
            start: startp,
            end: endp,
        });
        startp = endp;
    }
    lines
}

fn is_vertical(line: &Line) -> bool {
    line.start.x == line.end.x
}

fn is_horizontal(line: &Line) -> bool {
    line.start.y == line.end.y
}

fn vert_hori_test(line_1: &Line, line_2: &Line) -> Option<Position> {
    let (l1_s, l1_e) = (line_1.start, line_1.end);
    let (l2_s, l2_e) = (line_2.start, line_2.end);
    if is_vertical(line_1) & is_horizontal(line_2) {
        let (min_x, max_x) = (cmp::min(l2_s.x, l2_e.x), cmp::max(l2_s.x, l2_e.x));
        let (min_y, max_y) = (cmp::min(l1_s.y, l1_e.y), cmp::max(l1_s.y, l1_e.y));
        if (l1_s.x > min_x) & (l1_s.x < max_x) & (l2_s.y > min_y) & (l2_s.y < max_y) {
            return Some(Position {
                x: l1_s.x,
                y: l2_s.y,
            });
        }
    }
    return None;
}

fn do_intersect(line_1: &Line, line_2: &Line) -> Option<Position> {
    let test_1 = vert_hori_test(line_1, line_2);
    let test_2 = vert_hori_test(line_2, line_1);
    if test_1.is_some() {
        return test_1;
    }
    if test_2.is_some() {
        return test_2;
    }
    None
}

fn get_steps(line: &Line) -> i32 {
    let mut dist;
    if is_horizontal(line) {
        dist = line.start.x - line.end.x
    } else {
        dist = line.start.y - line.end.y
    }
    if dist < 0 {
        dist *= -1
    }
    dist
}

fn main() {
    let input = include_str!("input");

    let mut lines = input.lines();
    let cable_1 = lines.next().unwrap().split(",").collect();
    let cable_2 = lines.next().unwrap().split(",").collect();

    let lines_1 = get_lines(cable_1);
    let lines_2 = get_lines(cable_2);

    let mut link_1 = 0;
    let mut link_2 = 0;
    let mut min_link = 1000000;
    let mut min_manhattan = 100000;

    for line_1 in lines_1.iter() {
        link_1 += get_steps(line_1);
        for line_2 in lines_2.iter() {
            link_2 += get_steps(line_2);
            if do_intersect(line_1, line_2).is_some() {
                let intersection = do_intersect(line_1, line_2).unwrap();
                let man_dist = intersection.x + intersection.y;
                if man_dist < min_manhattan {
                    min_manhattan = man_dist;
                }
                let residual_line_1 = Line {
                    start: line_1.end,
                    end: intersection,
                };
                let residual_line_2 = Line {
                    start: line_2.end,
                    end: intersection,
                };
                let residual_step_1 = get_steps(&residual_line_1);
                let residual_step_2 = get_steps(&residual_line_2);
                let link_total = link_1 - residual_step_1 + link_2 - residual_step_2;
                if link_total < min_link {
                    min_link = link_total;
                }
            }
        }
        link_2 = 0;
    }
    println!("part-1: {:?}", min_manhattan);
    println!("part-2: {:?}", min_link);
}
