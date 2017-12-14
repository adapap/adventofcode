//Difficulty: 8/10
let children = {}
let dict = {}
function incChildren(parent) {
	let allChildren = children[parent]
	for (let c in allChildren) {
		let child = allChildren[c]
		if (dict[child] == undefined) {
			dict[child] = dict[parent] + 1
		}
		else {
			dict[child]++
		}
		if (children[child] != undefined) {
			incChildren(child)
        }
	}
}

function solve(s) {
	let a = s.split('\n')
	for (let prog in a) {
		let name = a[prog].substring(0, a[prog].indexOf(' '))
		if (dict[name] == undefined) {
			dict[name] = 0
		}
		if (a[prog].indexOf('>') != -1) {
			let child = a[prog].substring(a[prog].indexOf('>') + 2, a[prog].length).split(', ')
			children[name] = child
			incChildren(name)
		}
	}
	for (let n in dict) {
		if (dict[n] == 0) {
			return n
		}
	}
}
//
weightDict = {}
children = {}
weight = null
layers = []
start = 'eugwuhl'

function solve2(s) {
	let a = s.split('\n')
	for (let w in a) {
		let name = a[w].substring(0, a[w].indexOf(' '))
		let val = a[w].substring(a[w].indexOf('(') + 1,a[w].indexOf(')'))
		weightDict[name] = parseInt(val)
	}
	for (let prog in a) {
		let name = a[prog].substring(0, a[prog].indexOf(' '))
		if (a[prog].indexOf('>') != -1) {
			let child = a[prog].substring(a[prog].indexOf('>') + 2, a[prog].length).split(', ')
			children[name] = child
		}
	}
	checkWeights(start)
	let lastLayer = layers[layers.length - 1]
	let prevLayer = layers[layers.length - 2]
	let lastSum = lastLayer[0] * lastLayer.length
	let prevUniq, prevNormal
	for (let num in prevLayer) {
		if (prevLayer.filter(e=>e==prevLayer[num]).length == 1) {
			prevUniq = prevLayer[num]
        }
		else {
			prevNormal = prevLayer[num]
        }
    }
	weight = prevNormal - lastSum
	
	return weight
}

function sumWeights(parent) {
	let sum = 0
	let allc = children[parent]
	sum += weightDict[parent]
	if (allc != undefined) {
		for (let c in allc) {
			sum += weightDict[allc[c]]
			if (children[allc[c]] != undefined) {
				for (d in children[allc[c]]) {
					sum += sumWeights(children[allc[c]][d])
                }
	        }
	    }
	}
	return sum
}

function checkWeights(parent) {
	let layer = []
	for (let c in children[parent]) {
		layer.push(sumWeights(children[parent][c]))
	}
	layers.push(layer)
	for (let numsum in layer) {
		if (layer.filter(e=>e==layer[numsum]).length == 1) {
			checkWeights(children[parent][numsum])
        }
    }
}