import { prompt } from "../utils/stdin.js";

var nota01 = parseInt(await prompt("Ingrese primera nota: "));
var nota02 = parseInt(await prompt("Ingrese segunda nota: "));
var nota03 = parseInt(await prompt("Ingrese tercera nota: "));
var nota04 = parseInt(await prompt("Ingrese cuarta nota: "));
var suma = nota01 + nota02 + nota03 + nota04;
var promedio = suma / 4;

console.log("El promedio es: " + promedio);
