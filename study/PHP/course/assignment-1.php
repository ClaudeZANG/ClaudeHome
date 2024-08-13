Assignment - 1

<?php /*
// 1. Write a PHP script to get the PHP version and configuration information.

// Get the PHP version
$php_version = phpversion();

// Get the PHP configuration information
$php_config = phpinfo();

// Display PHP version
echo "PHP version: $php_version<br>";

// Display PHP configuration information
echo "PHP configuration:<br>";
echo $php_config;
*/ ?>



<!-- <br>2. Create a simple HTML form and accept the user name and display the name through PHP echo statement.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Name Form</title>
</head>
<body>
    <form method="POST">
        <label for="username">Enter your name:</label>
        <input type="text" id="username" name="username">
        <button type="submit">Submit</button>
    </form>

    <?php /*
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST["username"];
        echo "Hello, $username!";
    }
    */ ?>
</body>
</html> -->

<!-- <br>3.Write a PHP script to get the client IP address.<br>
<?php /*
//#3. Write a PHP script to get the client IP address.

// Get the client's IP address
$client_ip = $_SERVER['REMOTE_ADDR'];

// Display the client's IP address
echo "Client IP Address: $client_ip";
*/ ?> -->



<!-- <br>4. Write a PHP script, which changes the color of the first character of a word.<br>
<?php /*
// Input string
$input_string = "Write a PHP script, which changes the color of the first character of a word.";

// Function to change the color of the first character of a word
function colorizeFirstCharacter($string) {
    // Split the input string into an array of words
    $words = explode(" ", $string);
    
    // Iterate through each word
    foreach ($words as &$word) {
        // Get the first character of the word
        $first_char = substr($word, 0, 1);
        // Get the rest of the word
        $rest_of_word = substr($word, 1);
        // Apply CSS style to color the first character
        $word = "<span style='color:red;'>$first_char</span>$rest_of_word";
    }
    
    // Join the words back into a string
    $result = implode(" ", $words);
    
    return $result;
}

// Call the function and display the result
echo colorizeFirstCharacter($input_string);
*/ ?> -->


<!-- <br>5. Write a PHP script, to check whether the page is called from 'https' or 'http'.<br>
<? /*php
// Function to check if the page is called from 'https' or 'http'
function checkProtocol() {
    // Check if the current request is over HTTPS
    if(isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') {
        return "This page is called from HTTPS.";
    } else {
        return "This page is called from HTTP.";
    }
}

// Call the function and display the result
echo checkProtocol();
*/ ?> -->


<!-- <br>6. Write a PHP script to redirect a user to a different page.<br>
<?php /*
// Define the URL to redirect the user to
$redirect_url = "https://www.differentPage.com";

// Perform the redirection
header("Location: $redirect_url");
exit; // Ensure that no further code is executed after redirection
*/ ?> -->


<!-- <br>7. Write a simple PHP program to check that emails are valid. 
Hints : Use FILTER_VALIDATE_EMAIL filter that validates value as an e-mail address. 
Note : The PHP documentation does not say that FILTER_VALIDATE_EMAIL should pass the 
RFC5321<br>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Validation</title>
</head>
<body>
    <h2>Email Validation</h2>
    <form method="POST">
        <label for="email">Enter your email:</label>
        <input type="text" id="email" name="email">
        <button type="submit">Validate</button>
    </form>

    <?php /*
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve the email entered by the user
        $email = $_POST["email"];

        // Validate the email using FILTER_VALIDATE_EMAIL
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            echo "The email '$email' is valid.";
        } else {
            echo "The email '$email' is not valid.";
        }
    }
    */ ?>
</body>
</html> -->


<!-- <br>8. Write a PHP script to count number of lines in a file.<br>
<?php /*
// Specify the path to the file
$file_path = "path/to/your/file.txt";

// Open the file for reading
$file = fopen($file_path, "r");

// Initialize a variable to count the lines
$line_count = 0;

// Loop through each line in the file
while (!feof($file)) {
    // Read each line
    fgets($file);
    
    // Increment the line count
    $line_count++;
}

// Close the file
fclose($file);

// Display the number of lines
echo "The file '$file_path' contains $line_count lines.";
*/ ?> -->

<!-- <br>9. Write a PHP script to get the document root directory under which the current script is 
executing, as defined in the server's configuration file.<br>
<?php /*
// Get the document root directory
$document_root = $_SERVER['DOCUMENT_ROOT'];

// Display the document root directory
echo "Document root directory: $document_root";
*/ ?> -->

<!-- <br>10. Write a PHP script to get the time of the last modification of the current page.<br>
<?php /*
// Get the last modification time of the current page
$last_modified_time = filemtime(__FILE__);

// Format the last modification time
$last_modified_formatted = date("Y-m-d H:i:s", $last_modified_time);

// Display the last modification time
echo "Last modified time of the current page: $last_modified_formatted";
*/ ?> -->

<!-- <br>11. Write a PHP program to check whether a number is an Armstrong number or not. Return true if 
the number is Armstrong otherwise return false. 
Note: An Armstrong number of three digits is an integer so that the sum of the cubes of its digits 
is equal to the number itself. For example, 153 is an Armstrong number since 1**3 + 5**3 + 3**3 = 153<br>
<?php /*
// Function to check if a number is an Armstrong number
function isArmstrong($number) {
    $sum = 0;
    $temp = $number;
    
    // Calculate the number of digits in the number
    $digits = strlen((string)$number);
    
    // Calculate the sum of the cubes of its digits
    while ($temp != 0) {
        $remainder = $temp % 10;
        $sum += $remainder ** $digits;
        $temp = (int)($temp / 10);
    }
    
    // Check if the number is Armstrong or not
    if ($number == $sum) {
        return true;
    } else {
        return false;
    }
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["number"])) {
    // Get the number entered by the user
    $number = $_POST["number"];
    
    // Call the function to check if it's an Armstrong number
    if (isArmstrong($number)) {
        $result = "$number is an Armstrong number.";
    } else {
        $result = "$number is not an Armstrong number.";
    }
}
*/ ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Armstrong Number Checker</title>
</head>
<body>
    <h2>Armstrong Number Checker</h2>
    <form method="POST">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Check</button>
    </form>
    <?php /* if (isset($result)) echo "<p>$result</p>"; */ ?>
</body>
</html> -->


<!-- <br>12. Write a PHP program to remove duplicates from a sorted list.<br>
<?php /*
// Function to remove duplicates from a sorted list
function removeDuplicates($sorted_list) {
    $result = array(); // Initialize an empty array to store unique elements
    
    // Loop through the sorted list
    foreach ($sorted_list as $element) {
        // Check if the current element is not equal to the last element in the result array
        if (empty($result) || $element != end($result)) {
            // If not equal, add the element to the result array
            $result[] = $element;
        }
    }
    
    return $result;
}

// Sorted list with duplicates
$sorted_list_with_duplicates = array(1, 2, 2, 3, 4, 4, 4, 5, 5, 6);

// Remove duplicates from the sorted list
$unique_list = removeDuplicates($sorted_list_with_duplicates);

// Display the unique list
echo "Original list with duplicates: " . implode(", ", $sorted_list_with_duplicates) . "<br>";
echo "List after removing duplicates: " . implode(", ", $unique_list);
*/ ?> -->


<!-- <br>13. Write a PHP program to print out the multiplication table up to 12 * 12.<br>
<?php /*
// Function to print multiplication table up to 12 * 12
function printMultiplicationTable() {
    // Nested loop to generate multiplication table
    for ($i = 1; $i <= 12; $i++) {
        echo "<p>Multiplication table for $i:</p>";
        echo "<table border='1'>";
        for ($j = 1; $j <= 12; $j++) {
            echo "<tr>";
            echo "<td>$i * $j</td>";
            echo "<td>=</td>";
            echo "<td>" . ($i * $j) . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    }
}

// Call the function to print multiplication table
printMultiplicationTable();
*/ ?> -->


<!-- <br>14. Write a PHP program that multiplies corresponding elements of two given lists.<br>
<?php /*
// Function to multiply corresponding elements of two lists
function multiplyLists($list1, $list2) {
    // Check if the lists have the same length
    if (count($list1) != count($list2)) {
        return "Lists must have the same length.";
    }

    $result = array();

    // Multiply corresponding elements of the lists
    for ($i = 0; $i < count($list1); $i++) {
        $result[] = $list1[$i] * $list2[$i];
    }

    return $result;
}

// Example lists
$list1 = array(1, 2, 3, 4, 5);
$list2 = array(2, 3, 4, 5, 6);

// Call the function and display the result
$result = multiplyLists($list1, $list2);
echo "Result: ";
print_r($result);
*/ ?> -->


<!-- <br>15. Write a PHP program to compute the sum of the digits of a number.<br>
<?php /*
// Function to compute the sum of digits of a number
function sumOfDigits($number) {
    // Convert the number to a string
    $numberStr = (string) $number;

    // Initialize sum
    $sum = 0;

    // Iterate through each digit and add it to the sum
    for ($i = 0; $i < strlen($numberStr); $i++) {
        $sum += (int) $numberStr[$i];
    }

    return $sum;
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the number from the form
    $number = $_POST["number"];

    // Call the function and display the result
    echo "Sum of digits of $number: " . sumOfDigits($number);
}
*/ ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sum of Digits</title>
</head>
<body>
    <form method="post">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Calculate</button>
    </form>
</body>
</html> -->


<!-- <br>16. Write a PHP program to compute the amount of the debt in n months. The borrowing amount is $100,000 and the loan adds 5% interest of the debt and rounds it to the nearest 1,000 above month by month.<br>
<?php /*
// Function to compute the debt amount after n months
function computeDebt($months) {
    // Initial borrowing amount
    $debt = 100000;

    // Monthly interest rate
    $interestRate = 0.05;

    // Compute debt for each month
    for ($i = 0; $i < $months; $i++) {
        // Add interest to debt
        $debt += $debt * $interestRate;

        // Round debt to the nearest 1000
        $debt = round($debt, -3);
    }

    return $debt;
}

// Test the function with n months
$n = 5; // Change this value to test with different number of months
echo "Debt after $n months: $" . computeDebt($n);
*/ ?> -->

<!-- <br>17. Write a PHP program to sort an array of positive integers using the Bead-Sort Algorithm.<br>
<?php /*
// Function to sort an array of positive integers using Bead-Sort Algorithm
function beadSort($arr) {
    // Find maximum element in the array
    $max = max($arr);

    // Create an array of empty strings
    $beads = array_fill(0, $max, '');

    // Place beads on strings
    foreach ($arr as $num) {
        for ($i = 0; $i < $num; $i++) {
            $beads[$i] .= '*';
        }
    }

    // Count the number of beads in each string
    foreach ($beads as &$strand) {
        $strand = strlen($strand);
    }

    // Initialize sorted array
    $sortedArr = array();

    // Reconstruct sorted array from counted beads
    foreach ($beads as $beadCount) {
        $sortedArr[] = $beadCount;
    }

    return $sortedArr;
}

// Test the function with an array of positive integers
$array = array(5, 3, 8, 2, 7);
echo "Original Array: " . implode(", ", $array) . "<br>";
echo "Sorted Array: " . implode(", ", beadSort($array));
*/ ?> -->


<!-- <br>18. Write a PHP function to change the following array's all values to upper or lower case.<br>
<?php /*
//#18. Write a PHP function to change the following array's all values to upper or lower case.
function changeCase($array, $toLower = false) {
    // Initialize an empty array to store the result
    $result = array();
    
    // Loop through each element of the input array
    foreach ($array as $key => $value) {
        // Convert the value to lower case if $toLower is true, otherwise to upper case
        $newValue = $toLower ? strtolower($value) : strtoupper($value);
        
        // Add the modified value to the result array
        $result[$key] = $newValue;
    }
    
    // Return the modified array
    return $result;
}

// Example array
$inputArray = array("Apple", "Banana", "Orange", "Grapes");

// Convert all values to upper case
$upperCaseArray = changeCase($inputArray);

// Convert all values to lower case
$lowerCaseArray = changeCase($inputArray, true);

// Display the original and modified arrays
echo "Original Array: ";
print_r($inputArray);
echo "<br>";
echo "Upper Case Array: ";
print_r($upperCaseArray);
echo "<br>";
echo "Lower Case Array: ";
print_r($lowerCaseArray);
*/ ?> -->


<!-- <br>19. Write a PHP script to generate simple random password [do not use rand() function] from a given string.<br>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Password Generator</title>
</head>
<body>
    <form method="post" action="">
        <label for="characters">Enter characters for generating password:</label>
        <input type="text" id="characters" name="characters" required>
        <button type="submit">Generate Password</button>
    </form>

    <?php /*
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (!empty($_POST["characters"])) {
            // Function to generate random password
            function generatePassword($length, $characters) {
                $password = '';
                $charLength = strlen($characters);

                // Use current timestamp as seed for randomness
                mt_srand(time());

                for ($i = 0; $i < $length; $i++) {
                    // Generate random index within the range of characters
                    $index = mt_rand(0, $charLength - 1);

                    // Append the character at the random index to the password
                    $password .= $characters[$index];
                }

                return $password;
            }

            // Get characters from form input
            $charString = $_POST["characters"];

            // Generate random password of length 8
            $password = generatePassword(8, $charString);

            // Display the generated password
            echo "<p>Generated Password: $password</p>";
        } else {
            echo "<p>Please enter characters for generating the password.</p>";
        }
    }
    */ ?>
</body>
</html> -->

<!-- <br>20. Write a PHP script to convert a string into an arbitrary array<br>
<?php /*
// Function to convert a string into an arbitrary array
function stringToArray($inputString) {
    $array = [];

    // Split the string into an array using a delimiter (comma in this case)
    $array = explode(',', $inputString);

    return $array;
}

// Input string
$inputString = "apple,banana,grape,orange";

// Convert the string into an array
$array = stringToArray($inputString);

// Display the resulting array
echo "<pre>";
print_r($array);
echo "</pre>";
*/ ?> -->

<!-- <br>21. Write a PHP script to extract the filename component of a URL path.<br>
<?php /*
// Function to extract the filename component of a URL path
function extractFilename($url) {
    // Use basename() function to get the filename component of the URL
    $filename = basename($url);
    return $filename;
}

// Example URL
$url = "https://www.example.com/path/to/file.txt";

// Extract the filename component from the URL
$filename = extractFilename($url);

// Display the extracted filename
echo "Filename: $filename";
*/ ?> -->


<!-- <br>22. Write a PHP script to insert a string at the specified position in a given string.<br>
<?php /*
// Function to insert a string at the specified position in a given string
function insertString($originalString, $stringToInsert, $position) {
    // Use substr_replace() function to insert the string at the specified position
    $modifiedString = substr_replace($originalString, $stringToInsert, $position, 0);
    return $modifiedString;
}

// Given string
$originalString = "Hello, world!";

// String to insert
$stringToInsert = "PHP ";

// Position to insert the string
$position = 7;

// Insert the string at the specified position
$modifiedString = insertString($originalString, $stringToInsert, $position);

// Display the modified string
echo "Modified String: $modifiedString";
*/ ?> -->


<!-- <br>23. Write a PHP script to get the characters after the last '/' in an url.<br>
<?php /*
// Function to get the characters after the last '/' in a URL
function getCharactersAfterLastSlash($url) {
    // Use strrchr() function to find the last occurrence of '/'
    // Then, use substr() function to get the characters after the last '/'
    $charactersAfterLastSlash = substr(strrchr($url, '/'), 1);
    return $charactersAfterLastSlash;
}

// Example URL
$url = "https://www.PHP.com/path/1/2/3";

// Get the characters after the last '/'
$charactersAfterLastSlash = getCharactersAfterLastSlash($url);

// Display the characters after the last '/'
echo "Characters after the last '/': $charactersAfterLastSlash";
*/ ?> -->

<!-- <br>24. Write a PHP class that calculates the factorial of an integer.<br>
<?php /*
class FactorialCalculator {
    // Function to calculate the factorial of an integer
    public static function calculateFactorial($number) {
        // Base case: if the number is 0 or 1, factorial is 1
        if ($number == 0 || $number == 1) {
            return 1;
        } else {
            // Recursive case: calculate factorial using recursion
            return $number * self::calculateFactorial($number - 1);
        }
    }
}

// Check if a number is provided by the user
if(isset($_POST['number'])) {
    // Get the number input from the user
    $number = $_POST['number'];
    
    // Validate if the input is a positive integer
    if (filter_var($number, FILTER_VALIDATE_INT) && $number >= 0) {
        // Calculate the factorial
        $factorial = FactorialCalculator::calculateFactorial($number);
        echo "Factorial of $number is $factorial";
    } else {
        echo "Please enter a valid positive integer.";
    }
}
*/ ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factorial Calculator</title>
</head>
<body>
    <form method="POST">
        <label for="number">Enter a number:</label>
        <input type="text" id="number" name="number">
        <button type="submit">Calculate Factorial</button>
    </form>
</body>
</html> -->

<!-- <br>25. Write a PHP Calculator class (called MyCalculator),which will accept two values as arguments, then add them, subtract them, multiply them together, or divide them on request.<br>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <h2>Calculator</h2>
    <form method="POST">
        <label for="num1">Enter the first number:</label>
        <input type="number" id="num1" name="num1" required>
        <br>
        <label for="num2">Enter the second number:</label>
        <input type="number" id="num2" name="num2" required>
        <br>
        <label for="operation">Select operation:</label>
        <select id="operation" name="operation" required>
            <option value="add">Addition</option>
            <option value="subtract">Subtraction</option>
            <option value="multiply">Multiplication</option>
            <option value="divide">Division</option>
        </select>
        <br>
        <input type="submit" value="Calculate">
    </form>

    <h2>Calculator Result</h2>
    <?php /*
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve form data
        $num1 = $_POST["num1"];
        $num2 = $_POST["num2"];
        $operation = $_POST["operation"];

        // Perform calculation based on selected operation
        switch ($operation) {
            case "add":
                $result = $num1 + $num2;
                echo "$num1 + $num2 = $result";
                break;
            case "subtract":
                $result = $num1 - $num2;
                echo "$num1 - $num2 = $result";
                break;
            case "multiply":
                $result = $num1 * $num2;
                echo "$num1 * $num2 = $result";
                break;
            case "divide":
                if ($num2 != 0) {
                    $result = $num1 / $num2;
                    echo "$num1 / $num2 = $result";
                } else {
                    echo "Cannot divide by zero!";
                }
                break;
            default:
                echo "Invalid operation selected";
        }
    }
    */ ?>
</body>
</html> -->

