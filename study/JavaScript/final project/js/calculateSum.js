// Function to calculate sum of two numbers
function calculateSum() {
    var num1 = parseFloat(document.getElementById('number1').value);
    var num2 = parseFloat(document.getElementById('number2').value);
    var sum = num1 + num2;
    document.getElementById('result').innerText = 'Sum: ' + sum;
}

// Adding event listener to the calculate button
document.getElementById('calculateBtn').addEventListener('click', calculateSum);
