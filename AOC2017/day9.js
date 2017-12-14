//Difficulty: 5/10
function solve(s) {
	let a = s.split('\n')
	let total = 0
	for (r in a) {
		let scoreInc = 0
		let score = 0
		let row = a[r].split('')
		let ignore = 0, garbage = false
		for (char in row) {
			let c = row[char]
			if (c == '!' && !ignore) {
				ignore = 2
			}
			if (c == '<' && !ignore) {
				garbage = true
			}
			if (c == '>' && !ignore) {
				garbage = false
			}
			if (c == '{' && !ignore && !garbage) {
				scoreInc++
			}
			if (c == '}' && !ignore && !garbage) {
				score += scoreInc
				scoreInc--
			}
			if (ignore > 0) ignore--
			row[char] = '-'
		}
		total += score
	}
	return total
}

//Part 2
function solve(s) {
	let a = s.split('\n')
	let total = 0
	for (r in a) {
		let scoreInc = 0
		let score = 0
		let row = a[r].split('')
		let ignore = 0, garbage = false, garbCount = 0, lead = false
		for (char in row) {
			let c = row[char]
			lead = false
			if (c == '!' && !ignore) {
				ignore = 2
			}
			if (c == '<' && !ignore) {
				if (!garbage) { lead = true }
				garbage = true
			}
			if (c == '>' && !ignore) {
				if (garbage) { lead = true }
				garbage = false
			}
			if (c == '{' && !ignore && !garbage) {
				scoreInc++
			}
			if (c == '}' && !ignore && !garbage) {
				score += scoreInc
				scoreInc--
			}
			if (garbage && !ignore && !lead) {
				garbCount++
			}
			if (ignore > 0) ignore--
			row[char] = '-'
		}
		total += garbCount
	}
	return total
}