import pprint


def UserImputToTableImput(tableTextLocationsSimplified, UserImput):

    if len(UserImput) == len(tableTextLocationsSimplified):
        UserInputFinal = []
        for i in range(len(tableTextLocationsSimplified)):
            for NumberExpressed in range(tableTextLocationsSimplified[i]):
                UserInputFinal.append(UserImput[i])

        # pprint.pprint('UserInputFinal: '+str(UserInputFinal))

        return UserInputFinal
    else:
        # print('user input size must equal table size')

        return "UserInputSizeError"







# tableTextLocationsSimplified =  [8, 7, 3, 3, 1, 3, 3, 8, 7, 1, 1]

# UserImput = ["AddedInput_:"+str(tableTextLocationsSimplified[i])+"#"+str(i+1)+"__XXXXXX" for i in range(len(tableTextLocationsSimplified))]

# UserImput = [2,3]


# UserInputFinal = UserImputToTableImput(tableTextLocationsSimplified, UserImput)


# pprint.pprint('UserInputFinal: '+str(UserInputFinal))












# tableTextLocations:  [25, 26, 27, 28, 29, 30, 31, 32, 78, 79, 80, 81, 82, 83, 84, 90, 91, 92, 99, 100, 101, 106, 146, 147, 148, 155, 156, 157, 182, 183, 184, 185, 186, 187, 188, 189, 235, 236, 237, 238, 239, 240, 241, 699, 782]
# tableTextLocationsSimplified:  [8, 7, 3, 3, 1, 3, 3, 8, 7, 1, 1]