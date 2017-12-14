//Difficulty: 1/10
function solveCaptcha(input) {
	let str = input
	let sum = 0
	for (let i=0; i<str.length; i++) {
		if (i == str.length - 1 && (str.charAt(i) == str.charAt(0))) {
			sum += parseInt(str.charAt(i))
		}
		else { if (str.charAt(i) == str.charAt(i+1)) {
			sum += parseInt(str.charAt(i))
		}}
	}
	return sum
}

function solveCaptcha2(input) {
	let str = input
	let sum = 0
	for (let i=0; i<str.length; i++) {
		if (i > str.length/2) {
			if (str.charAt(i) == str.charAt(i - str.length/2)) sum += parseInt(str.charAt(i))
		}
		else {
			if (str.charAt(i) == str.charAt(i + str.length/2)) sum += parseInt(str.charAt(i))
		}
	}
	return sum
}