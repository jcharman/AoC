class Santa{
    public int x;
    public int y;

    public void move(char direction){
        switch(direction){
            case '^':
                this.y++;
                break;
            case 'v':
                this.y--;
                break;
            case '>':
                this.x++;
                break;
            case '<':
                this.x--;
                break;
            default:
                throw new InvalidDataException("Input did not match expected format!");
        }
    }
}

class Program{
    // Load in the input.
    static string input = File.ReadAllText(@"input.txt").ToString();

    static int partOne(){
        Santa santa = new Santa();

        // Put all houses we've delivered to in a list.
        List<string> delivered = new List<string>();
        foreach(char direction in input){
            delivered.Add(santa.x.ToString() + "," + santa.y.ToString());
            santa.move(direction);
        }

        // Dedupe the list.
        return(delivered.Distinct().ToList().Count());
    }

    static int partTwo(){
        Santa realSanta = new Santa();
        Santa roboSanta = new Santa();

        // Evry other move, move one set of coordinates and add them to the list.
        int currentMove = 0;
        List<string> delivered = new List<string>();

        foreach(char move in input){
            switch(currentMove%2){
                case 0:
                    delivered.Add(roboSanta.x.ToString() + "," + roboSanta.y.ToString());
                    roboSanta.move(move);
                    break;
                default:
                    delivered.Add(realSanta.x.ToString() + "," + realSanta.y.ToString());
                    realSanta.move(move);
                    break;
                    
            }
            currentMove++;
        }

        // Return the deduped list.
        return(delivered.Distinct().ToList().Count());
    }

    static void Main(){
        // Print Answers.
        Console.WriteLine("Part 1: " + partOne().ToString());
        Console.WriteLine("Part 2: " + partTwo().ToString());
    }
}
