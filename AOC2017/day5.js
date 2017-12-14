//Difficulty: 1/10
function maze(s) {
	let a = s.split('\n').map(e=>parseInt(e))
	let index = 0
	let steps = 0
	while(a[index] != undefined) {
		a[index]++
		index += a[index] - 1
		steps++
	}
	return steps
}

function maze2(s) {
	let a = s.split('\n').map(e=>parseInt(e))
	let index = 0
	let steps = 0
	while(a[index] != undefined) {
		if (a[index] >= 3) {
			a[index]--
			index += a[index] + 1
		}
		else {
			a[index]++
			index += a[index] - 1
		}
		steps++
	}
	return steps
}