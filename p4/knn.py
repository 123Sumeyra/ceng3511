import csv
import math
import operator
import matplotlib.pyplot as plt


# calculate euclidDistance!


def Euclidean_distance(A,B,C):
    dist = 0
    for x in range(C):
        dist += ((A[x] - B[x])**2)
    return math.sqrt(dist)
########################################################################

def Neighbors(trainingSet, test_row, k):
    neighbors = []
    numOfColumns = len(test_row) - 1
    for x in range(len(trainingSet)):
        dist = Euclidean_distance(test_row, trainingSet[x], numOfColumns)
        neighbors.append((trainingSet[x], dist))
#neighbor adding
#neighbor sorting

    neighbors.sort(key=operator.itemgetter(1))
    nr = []
    for i in range(k):
        nr.append(neighbors[i][0][20])
    return kn
#######################################################################################################################
def getAccuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    print("correct: ", correct)
    return (correct / float(len(test_set))) * 100




#######################################################################################################################

def Dataload(Fname):
    with open(Fname, 'r') as csvFile:
        lines = csv.reader(csvFile)
        data_set = list(lines)
        data_set.pop(0)
        for column in range(len(data_set)):
            for row in range(len(data_set[0])):
                data_set[column][row] = float(data_set[column][row]) #from string to float
    return data_set
########################################################################################################################



def Answergeting(n):
    class_votes = {}
    for x in range(len(n)):
        ans = n[x]
        if ans in class_votes:
            class_votes[ans] += 1
        else:
            class_votes[ans] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]


######################################################################################################################

    # data is preparing
train_file = 'train.csv'
test_file = 'test.csv'
#######################################################################################################################

trainingSet = Dataload(train_file)
testSet = Dataload(test_file)
print("\n\ntrainingSet: ", len(trainingSet))
print("testSet: ", len(testSet))
########################################################################################################################
y_coordinate = []
knb= []


k = 10




for x in range(len(testSet)):
    kn = Neighbors(trainingSet, testSet[x], k)
    knb.append(kn)
for j in range(1, k + 1):
    predictions = []
    print("k: ", j)
    for i in range(len(knb)):
        result = Answergeting(knb[i][0:j])
        predictions.append(result)

    accuracy = getAccuracy(testSet, predictions)
    print("Accuracy: " + str(accuracy) + "%\n")
    y_coordinate.append(accuracy)
#fo
f = plt.figure()
plt.plot(range(1, 11), y_coordinate)
# function to show the plot
    # plt.show()
f.savefig("plot.pdf", bbox_inches='tight')


