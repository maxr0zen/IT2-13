const display = document.getElementById('display');
const buttons = document.querySelector('.buttons');

let currentInput = '';
let operator = null;
let firstOperand = null;

function handleButtonClick(event) {
    const value = event.target.getAttribute('data-value');

    if (value === null) {
        return; // Игнорировать клики не на кнопках
    }

    switch (value) {
        case '+':
        case '-':
        case '*':
        case '/':
            if (currentInput !== '') {
                if (firstOperand === null) {
                  firstOperand = parseFloat(currentInput);
                }
              else {
                  calculate();
                  firstOperand = parseFloat(currentInput);
              }
              operator = value;
                currentInput = '';
            }
            break;
         case '=':
            calculate();
            break;
        case 'clear':
            currentInput = '';
            operator = null;
            firstOperand = null;
            display.value = '';
            break;
        default:
            currentInput += value;
            display.value = currentInput;
    }
}

function calculate() {
  if (firstOperand !== null && operator !== null && currentInput !== '') {
      const secondOperand = parseFloat(currentInput);
        let result;

        switch (operator) {
            case '+':
                result = firstOperand + secondOperand;
                break;
            case '-':
                result = firstOperand - secondOperand;
                break;
            case '*':
                result = firstOperand * secondOperand;
                break;
            case '/':
              if (secondOperand === 0) {
                result = 'Ошибка'
                break
              }
              result = firstOperand / secondOperand;
               break;
        }
         display.value = result;
        currentInput = result.toString();
        firstOperand = null;
        operator = null;
    }
}

buttons.addEventListener('click', handleButtonClick);
