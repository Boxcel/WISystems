module Main where

import System.IO
import Text.Read (readMaybe)

-- Function to perform basic arithmetic operations
calculate :: Double -> Double -> String -> Maybe Double
calculate x y op = case op of
    "+" -> Just (x + y)
    "-" -> Just (x - y)
    "*" -> Just (x * y)
    "/" -> if y /= 0 then Just (x / y) else Nothing
    "^" -> Just (x ** y)
    _   -> Nothing

-- Function to perform scientific operations
scientificCalculate :: Double -> String -> Maybe Double
scientificCalculate x op = case op of
    "sqrt" -> Just (sqrt x)
    "log"  -> if x > 0 then Just (log x) else Nothing
    "exp"  -> Just (exp x)
    _      -> Nothing

-- Main function to interact with the user
main :: IO ()
main = do
    putStrLn "Welcome to the Haskell Scientific Calculator!"
    putStrLn "Enter your operation in the format: number1 operator number2 (for binary operations)"
    putStrLn "or: operator number (for unary operations like sqrt, log, exp)"
    putStrLn "Type 'exit' to quit."

    calculatorLoop

calculatorLoop :: IO ()
calculatorLoop = do
    putStr "> "
    hFlush stdout
    input <- getLine
    if input == "exit"
        then putStrLn "Goodbye!"
        else do
            let tokens = words input
            case tokens of
                [xStr, op, yStr] -> do
                    let mx = readMaybe xStr :: Maybe Double
                    let my = readMaybe yStr :: Maybe Double
                    case (mx, my) of
                        (Just x, Just y) -> case calculate(x, y, op) of
                            Just result -> print result
                            Nothing -> putStrLn "Error: Invalid operation or division by zero."
                        _ -> putStrLn "Error: Invalid numbers."
                [op, xStr] -> do
                    let mx = readMaybe xStr :: Maybe Double
                    case mx of
                        Just x -> case scientificCalculate x op of
                            Just result -> print result
                            Nothing -> putStrLn "Error: Invalid operation."
                        _ -> putStrLn "Error: Invalid number."
                _ -> putStrLn "Error: Invalid input format."
            calculatorLoop
