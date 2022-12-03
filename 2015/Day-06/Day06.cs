// Define a 2D array to hold the light values.
bool[,] lights = new bool[1000,1000];
int[,] brightness = new int[1000,1000];

// Parse the instructions.
foreach(string line in File.ReadLines("input.txt")){
    string[] words = line.Split(' ');
    string action = string.Empty;
    string start = string.Empty;
    string end = string.Empty;

    switch(words[0]){
        case "turn":
            action = words[1];
            start = words[2];
            end = words[4];
            break;
        case "toggle":
            action = words[0];
            start = words[1];
            end = words[3];
            break;
    }

    int startX = Int32.Parse(start.Split(',')[0]);
    int startY = Int32.Parse(start.Split(',')[1]);
    int endX = Int32.Parse(end.Split(',')[0]);
    int endY = Int32.Parse(end.Split(',')[1]);

    // Iterate through the x numbers.
    for(int x = startX; x <= endX; x++){
        // Iterate through the y values for this row.
        for(int y = startY; y <= endY; y++){
            switch(action){
                case "on":
                    lights[x,y] = true;
                    brightness[x,y]++;
                    break;
                case "off":
                    lights[x,y] = false;
                    if(brightness[x,y] > 0){
                        brightness[x,y]--;
                    }
                    break;
                case "toggle":
                    brightness[x,y] += 2;
                    switch(lights[x,y]){
                        case true:
                            lights[x,y] = false;
                            break;
                        case false:
                            lights[x,y] = true;
                            break;
                    }
                    break;
                }
        }
    }
}

// Count up how many lights are on.
int lightsOn = 0;
foreach(bool light in lights){
    if(light == true){
        lightsOn++;
    }
}

// Count up the total brightness.
int totalBrightness = 0;
foreach(int level in brightness){
    totalBrightness += level;
}

// Print totals.
Console.WriteLine("Part 1: " + lightsOn);
Console.WriteLine("Part 2: " + totalBrightness);
