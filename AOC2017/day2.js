//Difficulty: 2/10
function checksum(s) {
	let sum = 0
	let a1 = s.split('\n')
	for (a in a1) {
		let b = a1[a].match(/\S+/g) || []
		for (c in b) { b[c] = parseInt(b[c]) }
		sum += Math.max(...b) - Math.min(...b)
	}
	return sum
}

function modsum(s) {
	let sum = 0
	let a1 = s.split('\n')
	for (a in a1) {
		let b = a1[a].match(/\S+/g) || []
		b.sort((a,b)=>b-a)
		let res
		for (let i=0; i<b.length - 1; i++) {
			let j = i + 1
			while (j<b.length) {
				if (b[i] % b[j] == 0) {
					sum += b[i] / b[j]
				}
				j++
			}
		}
	}
	return sum
}