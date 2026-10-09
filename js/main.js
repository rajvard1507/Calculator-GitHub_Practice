import {
    square,
    cube,
    squareRoot,
    cubeRoot,
    power,
    exponential,
    naturalLog,
    logBase10,
    sine,
    cosine,
    tangent,
    factorial,
    reciprocal,
    percentage
} from "./scientific.js";

const display = document.querySelector("#display");
const expressionDisplay = document.querySelector("#expression");
const historyList = document.querySelector("#history-list");

let expression = "";
let justCalculated = false;

let calculationHistory = [];

try {
    const saved = JSON.parse(
        localStorage.getItem("novacalc-history") || "[]"
    );

    if (Array.isArray(saved)) {
        calculationHistory = saved;
    }
} catch {
    calculationHistory = [];
}

function updateDisplay() {
    display.value = expression || "0";
}

function saveHistory(originalExpression, result) {
    calculationHistory.unshift({
        expression: originalExpression,
        result: String(result),
        time: new Date().toLocaleString()
    });

    calculationHistory = calculationHistory.slice(0, 30);

    try {
        localStorage.setItem(
            "novacalc-history",
            JSON.stringify(calculationHistory)
        );
    } catch (error) {
        console.error("Could not save history:", error);
    }

    renderHistory();
}

function renderHistory() {
    historyList.replaceChildren();

    if (calculationHistory.length === 0) {
        const empty = document.createElement("p");
        empty.className = "empty-history";
        empty.textContent = "No calculations yet.";
        historyList.appendChild(empty);
        return;
    }

    for (const item of calculationHistory) {
        const entry = document.createElement("div");
        entry.className = "history-item";

        const previousExpression = document.createElement("div");
        previousExpression.className = "history-expression";
        previousExpression.textContent = item.expression;

        const result = document.createElement("div");
        result.className = "history-result";
        result.textContent = `= ${item.result}`;

        const time = document.createElement("div");
        time.className = "history-time";
        time.textContent = item.time;

        entry.append(previousExpression, result, time);

        entry.addEventListener("click", () => {
            expression = item.result;
            justCalculated = true;
            updateDisplay();
        });

        historyList.appendChild(entry);
    }
}

function formatResult(value) {
    if (typeof value !== "number" || !Number.isFinite(value)) {
        throw new Error("The result is outside the supported numeric range.");
    }

    if (Object.is(value, -0) || Math.abs(value) < 1e-12) {
        return "0";
    }

    return String(Number(value.toPrecision(12)));
}

// Safely evaluate basic arithmetic without JavaScript eval().
function evaluateExpression(input) {
    const tokens = input.match(
        /(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?|[()+*/-]/gi
    );

    if (!tokens || tokens.join("") !== input.replace(/\s+/g, "")) {
        throw new Error("Invalid expression.");
    }

    let position = 0;

    function parseExpression() {
        let value = parseTerm();

        while (tokens[position] === "+" || tokens[position] === "-") {
            const operator = tokens[position++];
            const right = parseTerm();

            value = operator === "+"
                ? value + right
                : value - right;
        }

        return value;
    }

    function parseTerm() {
        let value = parseUnary();

        while (
            tokens[position] === "*" ||
            tokens[position] === "/"
        ) {
            const operator = tokens[position++];
            const right = parseUnary();

            if (operator === "/" && right === 0) {
                throw new Error("Cannot divide by zero.");
            }

            value = operator === "*"
                ? value * right
                : value / right;
        }

        return value;
    }

    function parseUnary() {
        if (tokens[position] === "+") {
            position++;
            return parseUnary();
        }

        if (tokens[position] === "-") {
            position++;
            return -parseUnary();
        }

        return parsePrimary();
    }

    function parsePrimary() {
        if (tokens[position] === "(") {
            position++;

            const value = parseExpression();

            if (tokens[position] !== ")") {
                throw new Error("Missing closing parenthesis.");
            }

            position++;
            return value;
        }

        const token = tokens[position++];

        if (!token || !/^(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?$/i.test(token)) {
            throw new Error("Invalid number.");
        }

        const value = Number(token);

        if (!Number.isFinite(value)) {
            throw new Error("Invalid number.");
        }

        return value;
    }

    const result = parseExpression();

    if (position !== tokens.length) {
        throw new Error("Invalid expression.");
    }

    return result;
}

function calculate() {
    if (!expression) return;

    const originalExpression = expression;

    try {
        const result = evaluateExpression(expression);
        const formatted = formatResult(result);

        expressionDisplay.textContent = `${originalExpression} =`;
        expression = formatted;
        updateDisplay();

        saveHistory(originalExpression, formatted);
        justCalculated = true;
    } catch (error) {
        expressionDisplay.textContent = error.message;
        expression = "";
        display.value = "Error";
        justCalculated = false;
    }
}

function applyScientificOperation(action) {
    try {
        const input = justCalculated
            ? expression
            : expression || "";

        const number = Number(input);

        if (input.trim() === "" || !Number.isFinite(number)) {
            throw new Error("Enter a valid number first.");
        }

        const functions = {
            square,
            cube,
            sqrt: squareRoot,
            cbrt: cubeRoot,
            exp: exponential,
            ln: naturalLog,
            log: logBase10,
            sin: sine,
            cos: cosine,
            tan: tangent,
            factorial,
            reciprocal
        };

        let result;

        if (action === "power") {
            const exponent = Number(
                prompt("Enter the exponent:")
            );

            if (!Number.isFinite(exponent)) {
                return;
            }

            result = power(number, exponent);
        } else if (action === "percentage") {
            const percent = Number(
                prompt("Calculate what percentage?")
            );

            if (!Number.isFinite(percent)) {
                return;
            }

            result = percentage(number, percent);
        } else {
            result = functions[action](number);
        }

        const formatted = formatResult(result);
        const originalExpression = `${action}(${number})`;

        expressionDisplay.textContent = `${originalExpression} =`;
        expression = formatted;
        updateDisplay();

        saveHistory(originalExpression, formatted);
        justCalculated = true;
    } catch (error) {
        expressionDisplay.textContent = error.message;
        expression = "";
        display.value = "Error";
        justCalculated = false;
    }
}

document.querySelectorAll("[data-value]").forEach(button => {
    button.addEventListener("click", () => {
        const value = button.dataset.value;

        if (justCalculated && /[\d.(]/.test(value)) {
            expression = "";
            expressionDisplay.textContent = "";
        }

        if (value === ".") {
            const currentNumber = expression.split(/[+\-*/()]/).pop();

            if (currentNumber.includes(".")) return;

            if (currentNumber === "") {
                expression += "0";
            }
        }

        expression += value;
        justCalculated = false;
        updateDisplay();
    });
});

document.querySelectorAll("[data-action]").forEach(button => {
    button.addEventListener("click", () => {
        const action = button.dataset.action;

        if (action === "clear") {
            expression = "";
            expressionDisplay.textContent = "";
            display.value = "0";
            justCalculated = false;
            return;
        }

        if (action === "delete") {
            expression = expression.slice(0, -1);
            updateDisplay();
            justCalculated = false;
            return;
        }

        if (action === "calculate") {
            calculate();
            return;
        }

        if (action === "sign") {
            if (expression) {
                expression = `-(${expression})`;
                updateDisplay();
            }
            return;
        }

        applyScientificOperation(action);
    });
});

document.querySelector("#clear-history").addEventListener("click", () => {
    calculationHistory = [];
    localStorage.removeItem("novacalc-history");
    renderHistory();
});

document.querySelector("#theme-toggle").addEventListener("click", () => {
    document.body.classList.toggle("light-theme");

    localStorage.setItem(
        "novacalc-theme",
        document.body.classList.contains("light-theme")
            ? "light"
            : "dark"
    );
});

if (localStorage.getItem("novacalc-theme") === "light") {
    document.body.classList.add("light-theme");
}

document.addEventListener("keydown", event => {
    if (/^[0-9.]$/.test(event.key)) {
        if (justCalculated) {
            expression = "";
            justCalculated = false;
        }

        expression += event.key;
        updateDisplay();
    } else if (["+", "-", "*", "/", "(", ")"].includes(event.key)) {
        expression += event.key;
        justCalculated = false;
        updateDisplay();
    } else if (event.key === "Enter" || event.key === "=") {
        event.preventDefault();
        calculate();
    } else if (event.key === "Backspace") {
        expression = expression.slice(0, -1);
        updateDisplay();
    } else if (event.key === "Escape") {
        expression = "";
        display.value = "0";
        expressionDisplay.textContent = "";
        justCalculated = false;
    }
});

renderHistory();
updateDisplay();