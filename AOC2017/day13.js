//Difficulty: 7/10
//Part 1
function solve(s) {
	let a = s.split('\n')
	let fw = {}
	for (firewall of a) {
		fw[firewall.substring(0,firewall.indexOf(':'))] = parseInt(firewall.substring(firewall.indexOf(':') + 2, firewall.length))
	}
	let layer = {}
	let max = 0
	for (f in fw) {
		if (f > max) { max = parseInt(f) }
		layer[f] = 0
	}
	let dirs = new Array(max + 1).fill(1)
	let packetIndex = 0
	let severity = 0
	while (packetIndex < (max + 1)) {
		if (layer[packetIndex] == 0) {
			severity += packetIndex * fw[packetIndex]
		}
		for (pos in layer) {
			if (layer[pos] + dirs[pos] > (fw[pos] - 1) || layer[pos] + dirs[pos] < 0) {
				dirs[pos] *= -1
			}
			if (fw[pos] != 1) {
				layer[pos] += dirs[pos]
			}
		}
		packetIndex++
	}
	return severity
}

//Part 2
function solve(s) {
	let a = s.split('\n')
	let fw = {}
	for (firewall of a) {
		fw[firewall.substring(0,firewall.indexOf(':'))] = parseInt(firewall.substring(firewall.indexOf(':') + 2, firewall.length))
	}
	let open = (time, index) => {
    	return !(time % ((fw[index]-1) * 2) == 0)
    }
    let isSafe = (time) => {
    	for (i=0; i<100; i++) {
    		let ind = i + time
    		if (fw[i] != undefined && !open(ind, i)) {
    			return false
    		} 
    	}
    	return true
    }
    let start = 0
    while(!safe(start)) {
    	start++
    }
    return start
}