//Difficulty: 4/10
function passphrase(s) {
	let arr = s.split('\n')
	let count = 0
	for (let a in arr) {
		let arrB = arr[a].split(' ')
		let valid = true
		for (let b in arrB) {
			if (arrB.indexOf(arrB[b]) != arrB.lastIndexOf(arrB[b])) {
				valid = false
            }
		}
		if (valid) count++
	}
	return count
}

function passphrase2(s) {
	let arr = s.split('\n')
	let count = 0
	for (let a in arr) {
		let arrB = arr[a].split(' ')
		let valid = true
		for (let b in arrB) {	
			let arrC = 	arrB.map(e=>e.split('').sort().join(''))
			if (arrC.indexOf(arrC[b]) != arrC.lastIndexOf(arrC[b])) {
				valid = false
            }
		}
		if (valid) count++
	}
	return count
}