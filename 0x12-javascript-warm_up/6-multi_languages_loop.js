#!/usr/bin/node
const myVar = 'C is fun\nPython is cool\nJavaScript is amazing';
let s = '';
let i;

for (i = 0; i < myVar.length; i++) {
  s += myVar[i];
}
console.log(s);
