//Difficulty: 2/10
function solve(s) {
	let input = s.split('\n')
	let dict = {}
	let max
	for (cmd in input) {
		let cmds = input[cmd].split(' ')
		if (dict[cmds[0]] == undefined) {
			dict[cmds[0]] = 0
		}
		if (dict[cmds[4]] == undefined) {
			dict[cmds[4]] = 0
		}
		let evalStr = 'dict[\'' + cmds[4] + '\']' + cmds[5] + parseInt(cmds[6])
		if (eval(evalStr)) {
			if (cmds[1] == 'inc') {
				dict[cmds[0]] += parseInt(cmds[2])
				if (max == undefined) {
					max = dict[cmds[0]]
				}
				else {
					if (dict[cmds[0]] > max) {
						max = dict[cmds[0]]
					}
				}
			}
			else {
				dict[cmds[0]] -= parseInt(cmds[2])
				if (max == undefined) {
					max = dict[cmds[0]]
				}
				else {
					if (dict[cmds[0]] > max) {
						max = dict[cmds[0]]
					}
				}
			}
		}
	}
	return max
}