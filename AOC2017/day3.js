//Difficulty: 9/10
function manhattan(n) {
	let size = Math.ceil(Math.sqrt(n))
	if (size % 2 == 0) { size++ }
	let max = size - 1
	let min = max / 2
	let dc = max
	let c = size * size - n
	return Math.abs(min-(c%dc)) + min
}

//v1
var a = [[1]]
function neighbors(a, ai, aj) {
	let val = 0
	for (let i = ai-1; i < ai+2; i++) {
		for (let j = aj-1; j < aj+2; j++) {
			if (a[i] != undefined) {
				if (a[i][j] != undefined && !(i == ai && j == aj)) {
					val += a[i][j]
				}
			}
		}
	}
	return val
}

function largestNum(n) {
	let numberCount = 1
	let size = 1
	let lastNum = 1
	let pos = 0
	let repeatCount = 1
	let tempCount = 1
	let arr_i = 0
	let arr_j = 0
	for (let test = 0; test < 6; test++) {
		let nextSize = Math.ceil(Math.sqrt(numberCount + 1))
		if (nextSize % 2 == 0) { nextSize++ }
		if (nextSize > size) {
			//Add ring of zeros
			let zeroRow = []
			for (let z = 0; z < nextSize; z++) {
				zeroRow.push(0)
			}
			a.splice(0,0,zeroRow)
			a.push(zeroRow)
			for (let i = 1; i < a.length - 1; i++) {
				a[i].splice(0,0,0)
				a[i].push(0)
			}
			arr_i++
			arr_j++
			size += 2
		}
		switch(pos) {
			case 0:
				arr_j++
				break
			case 1:
				arr_i--
				repeatCount++
				break
			case 2:
				arr_j--
				break
			case 3:
				arr_i++
				repeatCount++
				break
		}
		a[arr_i][arr_j] = neighbors(a, arr_i, arr_j)
		//console.log("i: " + arr_i + "j: " + arr_j + "val: " + a[arr_i][arr_j])
		if (arr_i == 1) {
			let b = a
			console.log(b)
		}
		lastNum = a[arr_i][arr_j]
		//console.log(lastNum)
		tempCount--
		if (tempCount == 0) {
			tempCount = repeatCount
			pos++
		}
		numberCount++
	}
	return lastNum
}

//v2
function solve(n) {
	let dir = 0
	let pos = { '0_0': 1 }
	let x = 0, y = 0
	let maxX = 0, maxY = 0
	let minX = 0, minY = 0
	let last = 1
	while (last <= n) {
		switch(dir) {
			case 0:
				x++
				if (x > maxX) {
					maxX = x
					dir = 1
				}
				break
			case 1:
				y++
				if (y > maxY) {
					maxY = y
					dir = 2
				}
				break
			case 2:
				x--
				if (x < minX) {
					minX = x
					dir = 3
				}
				break
			case 3:
				y--
				if (y < minY) {
					minY = y
					dir = 0
				}
				break
		}
		let sum = 0
		for (let i = y-1; i < y+2; i++) {
			for (let j = x-1; j < x+2; j++) {
				let str = i + '_' + j
				if (pos[str] != undefined && !(i == y && j == x)) {
					sum += pos[str]
				}
			}
		}
		pos[y + '_' + x] = sum
		last = sum
	}
	return last
}