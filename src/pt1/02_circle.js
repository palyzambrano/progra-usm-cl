import { prompt } from "../utils/stdin.js";

var radio = await prompt("Ingrese el radio: ");
var perimetro = 2 * Math.PI * radio;
var area = Math.PI * Math.pow(radio, 2);

console.log("perimetro: " + perimetro);
console.log("Área: " + area);
