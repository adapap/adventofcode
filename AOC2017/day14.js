//Difficulty: 5/10
//Part 1
//Day 10 solution
function hash(s) {
	let currentPos = 0, skipSize = 0
	let a = []
	for (let i=0; i<256; i++) {
		a.push(i)
	}
	let lenses = []
	for (char of s) {
		lenses.push(char.charCodeAt(0))
	}
	lenses.push(17, 31, 73, 47, 23)
	for (let z=0; z<64; z++) {
		for (l in lenses) {
			let len = lenses[l]
			if (len > 1) {
				let skip = skipSize
				let rev
				if (a[currentPos + len] == undefined) {
					rev = a.slice(currentPos, a.length).concat(a.slice(0,len-(a.length-currentPos))).reverse()
					let count = 0
					for (let i=currentPos; count<rev.length; i++) {
						if (i==a.length) { i=0; a[0] = rev[count] }
						else {
							a[i] = rev[count]
						}
						count++
					}
				}
				else {
					rev = a.slice(currentPos, currentPos + len).reverse()
					let count = 0
					for (let i=currentPos; count<rev.length; i++) {
						a[i] = rev[count]
						count++
					}
				}
				while (len--) {
					currentPos++
					if (currentPos >= a.length) { currentPos = 0 }
				}
				while (skip--) {
					currentPos++
					if (currentPos >= a.length) { currentPos = 0 }
				}
				skipSize++
			}
		}
	}
	let sparse = a
	let dense = []
	for (let i = 0; i < 16; i++) {
	    const o = sparse.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b)
	    dense.push(o)
	}
	const zeropad = n => ('0' + n).substr(-2)
	const hash = dense.map(n => zeropad(n.toString(16))).join('')
	return hash
}

function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

function solve(s) {
	let count = 0
	for (let i=0; i<128; i++) {
		let hex = hash(s + '-' + i)
		let bin = ''
		for (char of hex) {
			bin += pad(parseInt(char,16).toString(2), 4)
		}
		count += bin.split('').filter(e=>e==1).length
	}
	return count
}

//Part 2
//Part 1
//Day 10 solution
function hash(s) {
	let currentPos = 0, skipSize = 0
	let a = []
	for (let i=0; i<256; i++) {
		a.push(i)
	}
	let lenses = []
	for (char of s) {
		lenses.push(char.charCodeAt(0))
	}
	lenses.push(17, 31, 73, 47, 23)
	for (let z=0; z<64; z++) {
		for (l in lenses) {
			let len = lenses[l]
			if (len > 1) {
				let skip = skipSize
				let rev
				if (a[currentPos + len] == undefined) {
					rev = a.slice(currentPos, a.length).concat(a.slice(0,len-(a.length-currentPos))).reverse()
					let count = 0
					for (let i=currentPos; count<rev.length; i++) {
						if (i==a.length) { i=0; a[0] = rev[count] }
						else {
							a[i] = rev[count]
						}
						count++
					}
				}
				else {
					rev = a.slice(currentPos, currentPos + len).reverse()
					let count = 0
					for (let i=currentPos; count<rev.length; i++) {
						a[i] = rev[count]
						count++
					}
				}
				while (len--) {
					currentPos++
					if (currentPos >= a.length) { currentPos = 0 }
				}
				while (skip--) {
					currentPos++
					if (currentPos >= a.length) { currentPos = 0 }
				}
				skipSize++
			}
		}
	}
	let sparse = a
	let dense = []
	for (let i = 0; i < 16; i++) {
	    const o = sparse.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b)
	    dense.push(o)
	}
	const zeropad = n => ('0' + n).substr(-2)
	const hash = dense.map(n => zeropad(n.toString(16))).join('')
	return hash
}

function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

function solve(s) {
	let matrix = []
	for (let i=0; i<128; i++) {
		let hex = hash(s + '-' + i)
		let bin = ''
		for (char of hex) {
			bin += pad(parseInt(char,16).toString(2), 4)
		}
		matrix.push(bin.split('').map(e=>+e))
	}
	let group = (array, i, j, value) => {
	    if (array[i] && array[i][j] === -1) {
	        array[i][j] = value
	        group(array, i-1, j, value)
	        group(array, i+1, j, value)
	        group(array, i, j-1, value)
	        group(array, i, j+1, value)
	        return true
	    }
	}
	let data = matrix
	let value = 1
	data.forEach(function (a) {
	    a.forEach(function (b, i, bb) {
	        bb[i] = -b
	    })
	})
	data.forEach(function (a, i, aa) {
	    a.forEach(function (b, j, bb) {
	        group(aa, i, j, value) && value++
	    })
	})
	return value - 1
}