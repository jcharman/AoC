using System.Text.RegularExpressions;

List<char> vowels = new List<char>{'a','e','i','o','u'};
List<string> badStrings = new List<string>{"ab", "cd", "pq", "xy"};
int goodStrings = 0;

foreach(string line in File.ReadLines("input.txt")){
    int vowelsInLine = 0;
    foreach(char letter in line){
        if(vowels.IndexOf(letter) != -1){
            vowelsInLine++;
        }
    }
    if(vowelsInLine < 3){
        continue;
    }

    int repeatedLetters = 0;
    for(int i = 1; i < line.Count(); i++){
        if(line[i-1] == line[i]){
            repeatedLetters++;
        }
    }
    if(repeatedLetters < 1){
        continue;
    }

    int containsBadStrings = 0;
    foreach(string badString in badStrings){
        if(line.Contains(badString)){
            containsBadStrings++;
        }
    }
    if(containsBadStrings > 0){
        continue;
    }

    goodStrings++;
}
Console.WriteLine("Part 1: " + goodStrings);

goodStrings = 0;
foreach(string line in File.ReadLines("input.txt")){
    int repeatedPairs = 0;
    for(int i = 1; i < line.Count(); i++){
        string currentPair = (line[i-1].ToString() + line[i].ToString());
        int numMatches = Regex.Matches(line, currentPair).Count();
        if(numMatches > 1){
            repeatedPairs++;
        }
    }
    if(repeatedPairs<1){
        continue;
    }
    int repeatedLettersPart2 = 0;
    for(int i = 0; i < line.Count()-2; i++){
        if(line[i+2] == line[i]){
            repeatedLettersPart2++;
        }
    }
    if(repeatedLettersPart2 < 1){
        continue;
    }

    goodStrings++;

}
Console.WriteLine("Part 2: " + goodStrings);
