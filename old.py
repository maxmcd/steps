from __future__ import print_function

import sys

from collections import defaultdict
from datetime import datetime


def getSteps(n):

    startTime = datetime.now()

    possibleStepSizes = range(1, n)
    stepPairSums = defaultdict(dict)
    index = 0

    for number in possibleStepSizes:
        toSum = possibleStepSizes[:]
        toSum.pop(index)
        for x in toSum:
            pair = [x, number]
            pair.sort()
            stepPairSums[x + number][pair[0]] = pair[1]
        index += 1

    # now we have a dictionary where the keys are all the sum values of all
    # pairs of steps. ie: for 5 we have:
    # {
    #     3: {1: 2},
    #     4: {1: 3},
    #     5: {1: 4,2: 3},
    #     6: {2: 4},
    #     7: {3: 4}
    # }

    print(stepPairSums)

    nGroup = stepPairSums[n]

    stepValues = []
    stringSolutions = {}

    print(nGroup)

    def appendStepValues(steps):
        steps.sort()
        key = str(steps)
        if not stringSolutions.get(key):
            stringSolutions[key] = True
            stepValues.append(steps)

    def returnSingleCollapse(steps):
        steps = steps[:]
        index = 0
        for step in steps:
            sumPairs = stepPairSums.get(step)
            if sumPairs:
                steps.pop(index)
                return steps, sumPairs
            index += 1
        return None, None

    def generateStepsFromPartials(partialSteps, components):
        out = []
        for x in components:
            forOut = partialSteps[:]
            if x in forOut:
                continue
            if components[x] in forOut:
                continue
            forOut.append(x)
            forOut.append(components[x])
            out.append(forOut)
        return out

    def addSteps(steps):
        sys.stdout.write(str(len(stepValues)))
        sys.stdout.write("\r")
        appendStepValues(steps)
        partialSteps, components = returnSingleCollapse(steps)
        print("collapse:", steps, partialSteps, components)
        if partialSteps and components:
            nextSteps = generateStepsFromPartials(partialSteps, components)
            for steps in nextSteps:
                addSteps(steps)

    for x, y in list(nGroup.iteritems()):
        # print(x, y)
        thisOne = [x, y]
        addSteps(thisOne)

    print(len(stepValues))

    print(datetime.now() - startTime)

getSteps(15)


# getNumber
# getFirstLevelSums

# given 1,6
# get [1] and {1:5, 2:4}
# given [1] and {1:5, 2:4}
# get [1,1,5] and [1,2,4]

# # 7
# 1,6

# 1,1,5

# 1,2,4


# 2,5
# 2,1,4
# 2,2,3

# 3,4
# 1,2,4
# 1,2,1,3
# 3,1,3
