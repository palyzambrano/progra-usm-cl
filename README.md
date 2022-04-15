<div>
  <h1 align="center">program-usm-cl</h1>
  <h4 align="center">
    JavaScript (NodeJS) implementation of programming exercises from Chile's
    "Santa Maria" University (USM)
  </h4>
</div>

## Motivation

As part of helping some folks from DuocUC learning programming fundamentals
and JavaScript for Web Development. [Exercises published on a public domain][1]
are implemented in JavaScript.

The full list of exercises is [available here][2].

## Getting Started

You will need to install [NodeJS][3] in your system, I recommend installing the
LTS (LTS stands for Long Term Support) version.

Then clone this repository:

```bash
git clone https://github.com/EstebanBorai/progra-usm-cl.git
```

Step into project directory using your terminal.

```bash
cd ./progra-usm-cl
```

Install any dependencies using `npm` (Comes with NodeJS installation).

```bash
npm install
```

Locally and use `node` to run execute the exercises:

```bash
node src/pt1/01_greeting.js
```

## How to add exercises

As you go through exercises, you will have to create JavaScript files inside
of the `src` directory. Given that exercises are split into 3 main chapters,
the `src` directory must contain 3 directories, one for each chapter.

Each file mus be prefixed with the exercise number as follows:

```
01_greeting.js
```

The resulting structure would be:

```
src/pt1/01_greeting.js
```

## Utilities

Utilities for perfoming tasks like reading from user keyboard input are included
inside of the `src/utils/stdin.js` file. If you have any issues using this
module please open an [issue here][4].

Whenever you want to read from user input you must import the `prompt` function
from the `stdin.js` module.

```js
import { prompt } from "../utils/stdin.js";        // Imports the `prompt` function

const name = await prompt("Ingrese su nombre: ");  // Awaits for user input

console.log("Hola, " + name);                      // Prints: Hola, {name}
```

## Contributions

Every contribution is very welcome, feel free to open issues or pull requests.

[1]: http://progra.usm.cl
[2]: http://progra.usm.cl/apunte/ejercicios/index.html
[3]: https://nodejs.org/en/
[4]: https://github.com/EstebanBorai/progra-usm-cl/issues
