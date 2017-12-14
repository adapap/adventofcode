//Difficulty: 8/10
//Part 1
function solve(s) {
	let a = s.split('\n')
	let dict = {}
	let groups = 0
	for (row of a) {
		let num = row.substring(0, row.indexOf(' '))
		let pipes = row.substring(row.indexOf('>') + 2, row.length).split(', ')
		for (let i=0; i<pipes.length; i++) {
			if (dict[num] == undefined) {
				dict[num] = []
			}
			dict[num].push(pipes[i])
		}
	}
	let found = dict[0]
	function loop() {
		for (key in dict) {
			if (found.includes(key)) {
				for (n of dict[key]) {
					if (!found.includes(n)) {
						found.push(n)
					}
				}
			}
		}
	}
	for (let z=0; z<Object.keys(dict).length; z++) {
		loop()
	}
	return found.length
}
//Part 2
function solve(s) {
	let a = s.split('\n')
	let dict = {}
	for (row of a) {
		let num = row.substring(0, row.indexOf(' '))
		let pipes = row.substring(row.indexOf('>') + 2, row.length).split(', ')
		for (let i=0; i<pipes.length; i++) {
			if (dict[num] == undefined) {
				dict[num] = []
			}
			dict[num].push(pipes[i])
		}
		dict[num].sort()
	}
	let excluded = []
	let getChildMap = (included) => {
		let arr = included
		for (key of arr) {
			let d = dict[key]
			for (i in d) {
				if (!arr.includes(d[i]) && d[i] != undefined) {
					arr.push(d[i])
				}
			}
		}
		if (arr == included) {
			arr.sort()
			for (e of arr) { excluded.push(e) } //Optimized recursion
			return arr
		}
		else {
			getChildMap(arr)
		}
	}
	let groups = []
	for (key in dict) {
		if (!excluded.includes(key)) {
			groups.push(getChildMap(dict[key]))
		}
	}
	return groups.length
	//Unoptimized
	/* return groups.reduce((a, v) => {
	  if (!a.set[v]) {
	  	a.set[v] = 1
	    a.count++
	  }
	  return a
	}, { set: {}, count: 0 }).count */
}