//Difficulty: 1/10
function solve(s) {
	let a = s.split('\t').map(e=>parseInt(e))
	let steps = 0
	let dict = {}
	let max, index
	while (dict[a.join('_')] == undefined) {
		dict[a.join('_')] = true
		max = Math.max(...a)
		index = a.indexOf(max)
		a[index] = 0
		index = (index == a.length - 1) ? 0 : index + 1
		while (max) {
			a[index]++
			max--
			if (a[index+1]==undefined) {
				index = 0
			}
			else {
				index++
			}
		}
		steps++
	}
	return steps
}

function solve2(s) {
	let a = s.split('\t').map(e=>parseInt(e))
	let steps = 0
	let dict = {}
	let max, index
	while (dict[a.join('_')] == undefined) {
		dict[a.join('_')] = steps
		max = Math.max(...a)
		index = a.indexOf(max)
		a[index] = 0
		index = (index == a.length - 1) ? 0 : index + 1
		while (max) {
			a[index]++
			max--
			if (a[index+1]==undefined) {
				index = 0
			}
			else {
				index++
			}
		}
		steps++
	}
	return steps - dict[a.join('_')]
}