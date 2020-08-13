# H15_camila.py
#
# This program will open and read a file that contains information about the World Serie winners from 1903 to 2009.
# It creates two dictionaries with the name of each team, and the year they won. At the end it calculate how many times each time won.

print('Hello to the World Series Winners Program. Enter a year in the range of 1903 to 2009 to discover who \
was the winner for that year, and how many times this team won the World Series.')
print('')

def main():
    '''
    Open and read file named WorldSeries.txt
    Parameters:
      - IOError - Raise an exception if file cannot be readen
      - Exception - Raise an exception in case another error occur 
    '''
    
    try:
        # Open file WorldSeries.txt
        file = open('WorldSeries.txt', 'r')
        # Read lines in the file
        lines = file.readlines()
        # Close file
        file.close()
       
    # Raise an exception in case file is not found or cannot be readen
    except IOError:
        print('An error occurred in reading file')
      
    # Raise an exception in case any other error occurr and show the details     
    except Exception as details:
        print('An error accured: ', details)
        
    # In case there is no exceptions raised, call function createDictionary(lines)
    else:
        createDictionary(lines)                
 
def createDictionary(lines):
    '''
    Prompt user to enter a year between 1903 and 2009, if the year typed is not in in this range, ask again.
    Open a dictionary and include the information from the file on it. Each line from the file represents a year.
    Parameters:
      - User can make no more than 3 attempts to enter the year desired.
    Return:
      - The name of the team who won that year
    '''

    nTrial = 1
    maxTrial = 3
    
    # Prompt user to enter the year
    year = int(input('Enter the year: '))
    
    # If the year types it is not between 1903 and 2009, prompt user again
    while year < 1903 or year > 2009:
        if nTrial < maxTrial:
            print("Please choose a year between 1903 and 2009")
            year = int(input('Enter the year: '))
            nTrial += 1
        else:
            print('You have tried too many times. Bye')
            year = -1
            break
        

    list = []
    for line in lines:
        line = line.strip()
        list.append(line)
        
    myDictionary =dict(enumerate(list,start = 1903))
    
              
    for key,value in myDictionary.items():            
        if key == year and (year == 1904 or year == 1994):
            print(value)
        elif key == year:
            print("The",value, "won the World Series in", key)
            getNumberofVictories(value,myDictionary)
            getOtherYears(value,myDictionary,key)
            
       
def getOtherYears(team,myDictionary,year):
    '''
    Count the number of years each team has won the World Series
    Return:
       - The number of year(s) won
    '''
    years = []
    count = 0
    for key, value in myDictionary.items():
        if value == team and key != year:
            years.append(key)
            count += 1
    if count == 0:
        print("This is the only time they've won")
    elif count == 1:
        print("They also won in", str(years)[1:-1])
    elif count ==2:
        print("They also won in", str(years)[1:-7] + " and" + str(years)[-6:-1])
    else:
        print("They also won in", str(years)[1:-6] + " and " + str(years)[-5:-1])
    

def getNumberofVictories(team,myDictionary):
    '''
    Create a second dictionary to count the number of times each time won
    Return:
       - The number of time(s) each team won
    '''

    Dictionary2={}
    List1 = list(myDictionary.values())
    
    for key, value in myDictionary.items():
        Dictionary2[value] = 0
    for i in range(1,len(List1)):
        val = List1[i]
        Dictionary2[val] += 1
    print("The", team, "have won the World Series", Dictionary2[team], "times")

 
if __name__ == '__main__':
    main()
