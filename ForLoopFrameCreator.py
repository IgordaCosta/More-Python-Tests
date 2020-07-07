import pandas



def CreateDatframeWithOneRow(columns,row):

    frame = pandas.DataFrame(columns=columns)

    frame.loc[len(frame)] = row

    print(frame)

    return frame



def AddRowToExistingDataframe(frame,row):

    frame.loc[len(frame)] = row

    print(frame)

    return frame


columns=['column1','column2','column3','column4']
row=['a1','a2','a3','a4']



frame=CreateDatframeWithOneRow(columns=columns,row=row)


row=['b1','b2','b3','b4']


frame=AddRowToExistingDataframe(frame,row)

print("end frame bellow")

print(frame)



