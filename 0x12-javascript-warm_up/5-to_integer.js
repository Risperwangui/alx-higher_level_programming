#1/usr/bin/node
if (isNAN(process.argv[2]) || process.argv[2] === undefined) {
	cosole.log('Not a number');
} else {
	console.log('My number:', parseInt(process.argv[2]));
}
