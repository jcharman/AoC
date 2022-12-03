using System.Security.Cryptography;
using System.Text;

// Placeholders for values that need to be updated by multiple threads.
int nextNum;
int theNumber;

// Read the input into a string.
string input = File.ReadAllText(@"input.txt").ToString();

// Generate an MD5 from our input plus a number. Update the global var if MD5 matches goal.
bool checkMD5(int num, string goal){
    string currentMd5 = new string('x', goal.Count());
    using (MD5 md5 = MD5.Create()){
        byte[] hashBytes = md5.ComputeHash(Encoding.ASCII.GetBytes(input+num.ToString()));
        var sBuilder = new StringBuilder();
        for (int i = 0; i < hashBytes.Length; i++)
        {
            sBuilder.Append(hashBytes[i].ToString("x2"));
        }
        currentMd5 = sBuilder.ToString();
    }
    if(currentMd5.Substring(0,goal.Count()) == goal && theNumber == 0){
        theNumber = num;
        return true;
    }
    return false;
}

// Keep running checkMD5 incrementing the number it appends each time.
void mine(string goal){
    while(checkMD5(nextNum, goal) == false && theNumber == 0){
        nextNum++;
    }
}

// Start n threads all running the mine function for a given goal
int startThreads(string goal, int numThreads){
    theNumber = 0;
    nextNum = 0;
    for(int i = 0; i < numThreads; i++){
        Thread thread = new Thread(() => mine(goal)){
            Name = "thread" + "_" + goal + i.ToString()
        };
        thread.Start();
    }
    while(theNumber == 0){

    }
    return theNumber;
}

// Print the result.
DateTime start = DateTime.Now;
Console.WriteLine("Part 1: " + startThreads("00000", 4));
Console.WriteLine("Part 2: " + startThreads("000000", 4));
Console.WriteLine("Time taken: " + DateTime.Now.Subtract(start));
