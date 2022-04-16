import { prompt } from "../utils/stdin.js";

var valor1 = parseInt(await prompt("Ingrese cateto a: "));
var valor2 = parseInt(await prompt("Ingrese cateto b: "));
var hipotenusa = Math.pow(valor1, 2) + Math.pow(valor2, 2); ;


console.log(Math.sqrt(hipotenusa) + ' es el valor de la hipotenusa ');
