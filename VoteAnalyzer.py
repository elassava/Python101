import sys # imports the required libraries.
import matplotlib.pyplot as plt
import numpy as np
import random

fileName = sys.argv[1] # Takes the file name as an command-line argument.
nominees = sys.argv[2]  # Takes the nominees as an command-line argument.
nominees = nominees.split(",") # Appends the nominees into a list, seperating by comma.

def readFile(fileName): # Reads the given file and appends it into a list line by line.
    f = open(f"{fileName}") # Open file
    lines = [line.strip("\n").split(",") for line in f] # Writes the txt file into a list.
    return lines

def sortDict(dict): # Sorts the given dict by descending value.
    sortedValues = sorted(dict.values(), reverse=True) # Sorts the dictionary's values.
    sortedDict = {}
    for vote in sortedValues: # Checks if the vote value in sortedValues is equal to vote's actual key in original dictionary, if it is, updates the new dictionary.
        for key in dict.keys():
            if dict[key] == vote:
                sortedDict[key] = dict[key]
    return sortedDict

def nomineeIndex(nominee): # Returns the index of given nominee in the given file.
    lines = readFile(fileName)
    indexOfNominee = lines[0].index(nominee) 
    return indexOfNominee

def retrieveData(fileName, nominees): # Evaluates the given file by nominees and returns an ordered (parallel to order of nominees) list containing every nominee's votes.
    lines = readFile(fileName)           
    votes = []
    for nominee in nominees: # Appends the vote list by states for each nominee.
        indexOfNominee = lines[0].index(nominee)
        for line in lines[1:]:
            votes.append(int(line[indexOfNominee]))
            
    with open("retrievedData.txt", "w") as retrievedData: # Writes the "votes" list into a text file.
        retrievedData.write(f"votes = {votes}")
    return votes
votes = retrieveData(fileName, nominees)

def sortTotalVotes(nominees): # Calculates the total vote for each nominee, creates a dictionary in ("nominee":"total vote") format.
    lines = readFile(fileName)
    voteDict = {} 
    for nominee in nominees:
        indexOfNominee = lines[0].index(nominee)
        totalVotes = 0
        for line in lines[1:]:
            totalVotes += int(line[indexOfNominee])
            voteDict[f"{nominee}"] = totalVotes
    sortedVoteDict = sortDict(voteDict) # Sorts the voteDict dictionary by descending order.
    return sortedVoteDict

def DispBarPlot(): # Displays a bar plot of most voted 2 nominee's votes state by state.
    lines = readFile(fileName) 
    totalVotes = sortTotalVotes(nominees) 
    mostVoted = list(totalVotes.items())[0] # Most voted nominee
    secondVoted = list(totalVotes.items())[1] # 2nd voted nominee
    indexOne = nomineeIndex(mostVoted[0]) # Index of most voted nominee in the csv file.
    indexTwo = nomineeIndex(secondVoted[0]) # Index of 2nd voted nominee in the csv file.
    states = [line[0] for line in lines[1:]]
    votesOne = [int(line[indexOne]) for line in lines[1:]] # Creates a list for most voted nominee.
    votesTwo = [int(line[indexTwo]) for line in lines[1:]] # Creates a list for 2nd voted nominee.
    x = np.arange(len(states))
    plt.bar(x+0.2, votesOne, width=0.2, color='blue', edgecolor="black") # Creates a bar plot for most voted nominee.
    plt.bar(x, votesTwo, width=0.2,  color='red', edgecolor="black") # Creates a bar plot for 2nd voted nominee.
    plt.xticks(x, states, rotation=90) 
    plt.xlabel("States") # Labels the x-axis.
    plt.ylabel("Vote Counts") # Labels the y-axis.
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    figure = plt.gcf()
    figure.set_size_inches(15, 8)
    plt.tight_layout()
    plt.legend([mostVoted[0], secondVoted[0]]) # Shows a legend above the plot.
    plt.savefig("ComparativeVotes.pdf") # Saves the figure as a pdf file.
    plt.show()
    
def votePercentages(nominees): # Calculates the percantage of votes for each nominee.
    totalVotes = sortTotalVotes(nominees) 
    allVotes = 0 # Set initial value for all votes.
    percentageDict = {}
    for vote in totalVotes.values():
        allVotes += vote
    for nominee in nominees:
        percentage = (100 * int(totalVotes[f"{nominee}"])) / allVotes
        percentageDict[nominee] = percentage
    return percentageDict

def compareVoteonBar(): # Compares the vote percentages in descending order.
    votePrc = votePercentages(nominees) 
    xList = [] 
    colorsDict = {} # Creates a colors dictionary.
    colors = ["red", "blue", "orange", "green"] 
    sortedVotePrc = sortDict(votePrc) # Sorts the percentage dict in descending order.
    for value in sortedVotePrc.values():
        value = ("%.3f" % value)
        xList.append(str(f"{value} %"))
    i = 0 
    for key in sortedVotePrc.keys():
            colorsDict[key] = colors[i]
            i += 1
    xAxis = xList
    yAxis = list(sortedVotePrc.values())
    x, y = xAxis, yAxis
    legends = sortedVotePrc.keys()
    plt.bar(x, y, label = legends, color = colorsDict.values(), edgecolor="black")
    plt.xlabel("Nominees")
    plt.ylabel("Percentages")
    plt.legend()
    plt.savefig("CompVotePercs.pdf")
    plt.show()

def obtainHistogram(L): # Calculates the ones and tens' frequency in a given list.
    ones = []
    tens = []
    for i in L:
        if len(str(i)) == 1:
            ones.append(str(i)[-1:])
            tens.append("0") # If number has only one digit, append 0 as tens' digit.
            
        else:
            ones.append(str(i)[-1:]) 
            tens.append(str(i)[-2:-1])          
    countedDigits = {}
    frequencyList = []
    allNumbers = len(ones)+len(tens)
    for i in range(10): # Counts all numbers between 0-9 (included) in the list.
        c1 = ones.count(str(i))
        c2 = tens.count(str(i))
        freq = c1+c2 # Total times of the number has appeared in the list.
        countedDigits[f"{i}"] = freq 
        frequency = (countedDigits[f"{i}"]) / allNumbers # Calculates the frequency.
        frequencyList.append(float("%.3f" % frequency))
    return frequencyList 
freqVotes = obtainHistogram(votes) # Get the histogram for "votes" list.

def meanValue(L): # Calculates the mean value of given list.
    totalValue = 0
    for value in L:
        totalValue += value
    meanValue = totalValue / len(L)
    mVList = [meanValue for i in range(len(L))] # Appends the mean value into a list "length of the list" times.
    return mVList
mVList = meanValue(freqVotes)

def plotHistogram(frequencyList): # Creates a histogram for votes' frequency list. 
    xAxis = [str(i) for i in range(10)] 
    yAxis = frequencyList 
    zAxis = meanValue(frequencyList)
    plt.plot(xAxis, yAxis, label="Digit Dist.", color="red")
    plt.plot(xAxis, zAxis, label="Mean", linestyle="dashed", color="green")
    plt.title("Histogram of least sign. digits")
    plt.xlabel("Digits")
    plt.ylabel("Distribution")
    plt.legend()
    plt.savefig("Histogram.pdf")
    plt.show()
    
def plotSampleHistogram(frequencyList, sampleNumber, color): # Creates a histogram for given samples.
    xAxis = [str(i) for i in range(10)]
    yAxis = frequencyList
    zAxis = meanValue(frequencyList)
    plt.plot(xAxis, yAxis, label="Digit Dist.",  color=color)
    plt.plot(xAxis, zAxis, label="Mean", linestyle="dashed", color="green")
    plt.title(f"Histogram of least sign. digits - Sample {sampleNumber}")
    plt.xlabel("Digits")
    plt.ylabel("Distribution")
    plt.legend()
    plt.savefig(f"HistogramOfSample{sampleNumber}.pdf")
    plt.show()

def plotHistogramWithSample(): # Creates 5 randomized sample lists to be evaluated.
    list1, list2, list3, list4, list5 = [], [], [], [], []
    sampleLists = [list1, list2, list3, list4, list5]
    for i in range(11) : list1.append(random.randint(0,100))
    for i in range(51) : list2.append(random.randint(0,100))
    for i in range(101) : list3.append(random.randint(0,100))
    for i in range(1001) : list4.append(random.randint(0,100))
    for i in range(10001) : list5.append(random.randint(0,100))
    sampleNumber = 1
    colors = ["cyan", "blue", "black", "pink", "purple", "orange"] 
    for lists in sampleLists:  
        color = random.choice(colors)
        frqList = obtainHistogram(lists)
        plotSampleHistogram(frqList, sampleNumber, color)
        colors.remove(color)
        sampleNumber += 1
    
def calculateMSE(L1, L2): # Calculates the "Mean Squared Error" for 2 given lists.
    zippedLists = zip(L1, L2)
    divided = 0
    divisor = len(L1)
    for i, j in zippedLists:
        calc = (i-j)**2 
        divided += calc
    mseValue = divided / divisor
    mseValue = "%.4f" % mseValue
    return mseValue
mseValue = calculateMSE(freqVotes, mVList) 

def compareMSEs(mseValue):
    numberOfSample = 10000 # Number of random samples to generate.
    random_MSEs = []
    for i in range(numberOfSample): # Creates "number_sample" amount of lists.
        sampleList = []
        while len(sampleList) < len(votes): # Appends random integers into the list until it's lenght is equal to votes' lenght. 
            sampleList.append(random.randint(0,1000))
        c = calculateMSE(obtainHistogram(sampleList), meanValue(obtainHistogram(sampleList))) # Calculates the MSE value of lists one by one.
        random_MSEs.append(c) # Appends the MSE values into a list.
        
    greaterCount = sum(1 for mse in random_MSEs if mse >= mseValue) 
    lowerCount = sum(1 for mse in random_MSEs if mse < mseValue) # Count the number of MSE values that are greater/lower than the MSE for the USA data.
    p_value = greaterCount / numberOfSample # Calculates the p_value.
    return p_value, greaterCount, lowerCount, numberOfSample
p_value, greaterCount, lowerCount, numberOfSample = compareMSEs(mseValue)

def interpret_results(mseValue): 
    alpha = numberOfSample * 5 / 100 # Set the significance level
    if lowerCount <= alpha:
        return(f"Finding: We reject the null hypothesis at the p= {p_value} level")

    else:
        return("Finding: There is no statistical evidence to reject null hypothesis")
        
DispBarPlot()
compareVoteonBar()
plotHistogram(freqVotes)
plotHistogramWithSample()

myAnswerList = [f"MSE value of 2012 USA election is {mseValue}\n",
f"The number of MSE of random samples that are larger than or equal to USA election MSE is {greaterCount}\n",
f"The number of MSE of random samples that are smaller than USA election MSE is {lowerCount}\n",
f"2012 USA election rejection level p is {p_value}\n", interpret_results(mseValue)]

def showAnswers(myAnswerList):
    with open("myAnswers.txt", "w") as file:
        for answer in myAnswerList:
            print(answer, end="")
            file.write(answer)
    
showAnswers(myAnswerList)
    


        

    
