// Input is one line so read it in as a string.
string input = File.ReadAllText(@"input.txt").ToString();

// Start on floor 0.
int currentFloor = 0;

// Counters for Part 2.
int currentChar = 0;
int part2 = 0;

// Loop through each char in the string and go up/down as directed.
foreach(char direction in input){
    switch(direction){
        case '(':
            currentFloor++;
            break;
        case ')':
            currentFloor--;
            break;
        default:
            throw new InvalidDataException("Input did not match expected format!");
    }

    // Increment our counter.
    currentChar++;

    // If we are on -1 and part2 is still 0, update it.
    if(currentFloor == -1 && part2 == 0){
        part2 = currentChar;
    }
}

// Print out the answers.
Console.WriteLine("Part 1: " + currentFloor);
Console.WriteLine("Part 2: " + part2);
