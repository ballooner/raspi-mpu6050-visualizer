import sys
import os
from pathlib import Path
from collections import deque

def main():
    # Make sure file argument is provided
    if len(sys.argv) < 2:
        print("Please enter the path of a .csv file as an argument!")
        return

    # Make sure file exists and that it is a CSV file
    inputFilePath = Path(sys.argv[1])
    if not inputFilePath.is_file() or inputFilePath.suffix != ".csv":
        print("Please enter the path of a .csv file as an argument!")
        return

    # Create CSV output file path
    outputFilePath = inputFilePath.parent / "filteredData.csv"

    movingAverage(inputFilePath, outputFilePath)

def movingAverage(inputPath, outputPath):
    inputFile = open(inputPath, 'r')
    outputFile = open(outputPath, 'w')

    outputFile.write(inputFile.readline()) # Write the input file header

    valueQueues = [deque() for _ in range(3)] # Create an array to hold the deques for each sensor value
    total = [0 for _ in range(3)]             # Create array to hold the current total for each sensor value

    for line in inputFile:
        currValues = line.strip().split(",")

        for i in range(len(valueQueues)): # Append each sensor value to the corresponding queue
            value = float(currValues[i])
            valueQueues[i].append(value)
            total[i] += value

            if len(valueQueues[i]) > 5:
                total[i] -= valueQueues[i].popleft()
                
        
        avg0 = total[0] / len(valueQueues[0])
        avg1 = total[1] / len(valueQueues[1])
        avg2 = total[2] / len(valueQueues[2])

        outputFile.write(f"{avg0:.5f},{avg1:.5f},{avg2:.5f},{currValues[3]}\n")
        
    # Cleanup
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()
