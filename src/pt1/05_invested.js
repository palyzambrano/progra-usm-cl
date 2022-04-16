import { prompt } from "../utils/stdin.js";

var valor = await prompt("Ingrese un valor: ");
var valor2 = valor.split('');
var convertir = valor2.reverse();



console.log(convertir + ' es su digito invertido');
