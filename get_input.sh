value=$(printf "%02d" $1)
curl https://adventofcode.com/2021/day/$1/input --cookie "session=53616c7465645f5f6aac791e3bb0009e639d867b72f96866074eb40f75aeb996467b3362c7575b7a24eea355829d772c" > 2021/day-$value/input
