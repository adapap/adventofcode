//Difficulty: 3/10
//Part 1
function solve(s) {
	let a = s.split(',')
	let x = 0, y = 0, z = 0
	for (dir of a) {
		switch(dir) {
			case 'ne':
				x++
				z--
				break
			case 'n':
				y++
				z--
				break
			case 'nw':
				y++
				x--
				break
			case 'sw':
				z++
				x--
				break
			case 's':
				z++
				y--
				break
			case 'se':
				y--
				x++
				break
		}
	}
	let ad = [Math.abs(x), Math.abs(y), Math.abs(z)]
	return Math.max(...ad)
}
//Part 2
function solve(s) {
	let a = s.split(',')
	let x = 0, y = 0, z = 0
	let md = 0
	for (dir of a) {
		switch(dir) {
			case 'ne':
				x++
				z--
				break
			case 'n':
				y++
				z--
				break
			case 'nw':
				y++
				x--
				break
			case 'sw':
				z++
				x--
				break
			case 's':
				z++
				y--
				break
			case 'se':
				y--
				x++
				break
		}
		let ad = [Math.abs(x), Math.abs(y), Math.abs(z)]
		let m = Math.max(...ad)
		if (m > md) {
			md = m
		}
	}
	return md
}