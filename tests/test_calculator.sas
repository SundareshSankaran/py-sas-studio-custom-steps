/* Define macro variables for custom step inputs */
%let num1 = 123;          /* First numeric value */
%let num2 = 241;          /* Second numeric value */
%let operation = ADD;     /* Calculation function: ADD, SUBTRACT, MULTIPLY, or DIVIDE */

/* Perform the calculation and store the result */
data work.calculator_result;
    /* Define variables and length */
    length Operation $10 Error_Message $100;
    
    /* Assign inputs to dataset variables */
    Num1 = &num1.;
    Num2 = &num2.;
    Operation = upcase("&operation.");
    Result = .;
    Error_Message = "";

    /* Determine operation and calculate result */
    select (Operation);
        when ("ADD")      Result = Num1 + Num2;
        when ("SUBTRACT") Result = Num1 - Num2;
        when ("MULTIPLY") Result = Num1 * Num2;
        when ("DIVIDE") do;
            if Num2 = 0 then do;
                Error_Message = "Error: Division by zero is undefined.";
                put "ERROR: " Error_Message;
            end;
            else do;
                Result = Num1 / Num2;
            end;
        end;
        otherwise do;
            Error_Message = "Error: Invalid operation specified. Choose ADD, SUBTRACT, MULTIPLY, or DIVIDE.";
            put "ERROR: " Error_Message;
        end;
    end;
run;

/* Display the result in the SAS Studio Results tab */
title "Calculator Output";
proc print data=work.calculator_result noobs;
    var Num1 Operation Num2 Result Error_Message;
run;

