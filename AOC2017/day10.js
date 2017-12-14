//Difficulty: 7/10
//Part 1
function solve(s) {
	let lenses = s.split(',').map(e=>parseInt(e))
	let a = []
	let currentPos = 0, skipSize = 0
	for (let i=0; i<256; i++) {
		a.push(i)
	}
console.log(a)
	for (l in lenses) {
		let len = lenses[l]
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
	return a[0] * a[1]
}

//Part 2
function solve(s) {
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