import { prompt } from "../utils/stdin.js";

var valor = parseInt(await prompt("Ingrese una longitud: "));
var convertir = valor / 2.54;

console.log(valor + " cm = " + convertir.toFixed(4) + " in");
