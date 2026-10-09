// Scientific Calculator Operations

// Square
export function square(number) {
    return number ** 2;
}

// Cube
export function cube(number) {
    return number ** 3;
}

// Square Root
export function squareRoot(number) {
    if (number < 0) {
        throw new Error("Square root of a negative number is not supported.");
    }

    return Math.sqrt(number);
}

// Cube Root
export function cubeRoot(number) {
    return Math.cbrt(number);
}

// Power
export function power(base, exponent) {
    return base ** exponent;
}

// Exponential: e^x
export function exponential(number) {
    return Math.exp(number);
}

// Natural Logarithm
export function naturalLog(number) {
    if (number <= 0) {
        throw new Error("Input must be positive.");
    }

    return Math.log(number);
}

// Base-10 Logarithm
export function logBase10(number) {
    if (number <= 0) {
        throw new Error("Input must be positive.");
    }

    return Math.log10(number);
}

// Trigonometric Functions (degrees)
export function sine(degrees) {
    return Math.sin(degrees * Math.PI / 180);
}

export function cosine(degrees) {
    return Math.cos(degrees * Math.PI / 180);
}

export function tangent(degrees) {
    const radians = degrees * Math.PI / 180;

    if (Math.abs(Math.cos(radians)) < 1e-10) {
        throw new Error("Tangent is undefined at this angle.");
    }

    return Math.tan(radians);
}

// Factorial
export function factorial(number) {
    if (!Number.isInteger(number) || number < 0) {
        throw new Error("Factorial requires a non-negative integer.");
    }

    if (number > 170) {
        throw new Error("Number is too large.");
    }

    let result = 1;

    for (let i = 2; i <= number; i++) {
        result *= i;
    }

    return result;
}

// Reciprocal
export function reciprocal(number) {
    if (number === 0) {
        throw new Error("Cannot divide by zero.");
    }

    return 1 / number;
}

// Percentage
export function percentage(number, percent) {
    return (number * percent) / 100;
}