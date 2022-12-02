int totalSqFt = 0;
int totalRibbon = 0;

// Read the input line by line.
foreach(string line in File.ReadLines(@"input.txt")){
    // Split the values into different vars.
    List<string> dimensionStrings = line.Split('x').ToList();
    List<int> dimensions = new List<int>();
    foreach(string number in dimensionStrings){
        dimensions.Add(Int32.Parse(number));
    }
    int length = dimensions[0];
    int width = dimensions[1];
    int height = dimensions[2];

    // Find smallest two dimensions.
    dimensions.Remove(dimensions.Max());

    // Calculate the perimeter and volume.
    int perimeter = ((2 * dimensions[0]) + (2 * dimensions[1]));
    int volume = (length * width * height);

    totalRibbon += (perimeter + volume);
    
    // Calculate the area of each side.
    List<int> sides = new List<int>();
    sides.Add(length * width);
    sides.Add(width * height);
    sides.Add(height * length);

    // Find the smallest side to use for slack.
    int slack = sides.Min();
    totalSqFt += slack;

    // Add the sides.
    foreach(int side in sides){
        totalSqFt += (side * 2);
    }
}

// Print the totals.
Console.WriteLine("Part 1: " + totalSqFt);
Console.WriteLine("Part 2: " + totalRibbon);
