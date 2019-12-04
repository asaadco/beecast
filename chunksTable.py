import random
import operator
import itertools
def generateChunkTable(totalChunks, allocMatrix, contributions, bandwidth):
    size_video1 = [2354772, 2123065, 2177073, 2160877, 2233056, 1941625, 2157535, 2290172, 2055469, 2169201, 2173522, 2102452, 2209463, 2275376, 2005399, 2152483, 2289689, 2059512, 2220726, 2156729, 2039773, 2176469, 2221506, 2044075, 2186790, 2105231, 2395588, 1972048, 2134614, 2164140, 2113193, 2147852, 2191074, 2286761, 2307787, 2143948, 1919781, 2147467, 2133870, 2146120, 2108491, 2184571, 2121928, 2219102, 2124950, 2246506, 1961140, 2155012, 1433658]
    size_video2 = [1728879, 1431809, 1300868, 1520281, 1472558, 1224260, 1388403, 1638769, 1348011, 1429765, 1354548, 1519951, 1422919, 1578343, 1231445, 1471065, 1491626, 1358801, 1537156, 1336050, 1415116, 1468126, 1505760, 1323990, 1383735, 1480464, 1547572, 1141971, 1498470, 1561263, 1341201, 1497683, 1358081, 1587293, 1492672, 1439896, 1139291, 1499009, 1427478, 1402287, 1339500, 1527299, 1343002, 1587250, 1464921, 1483527, 1231456, 1364537, 889412]
    size_video3 = [1034108, 957685, 877771, 933276, 996749, 801058, 905515, 1060487, 852833, 913888, 939819, 917428, 946851, 1036454, 821631, 923170, 966699, 885714, 987708, 923755, 891604, 955231, 968026, 874175, 897976, 905935, 1076599, 758197, 972798, 975811, 873429, 954453, 885062, 1035329, 1026056, 943942, 728962, 938587, 908665, 930577, 858450, 1025005, 886255, 973972, 958994, 982064, 830730, 846370, 598850]
    size_video4 = [668286, 611087, 571051, 617681, 652874, 520315, 561791, 709534, 584846, 560821, 607410, 594078, 624282, 687371, 526950, 587876, 617242, 581493, 639204, 586839, 601738, 616206, 656471, 536667, 587236, 590335, 696376, 487160, 622896, 641447, 570392, 620283, 584349, 670129, 690253, 598727, 487812, 575591, 605884, 587506, 566904, 641452, 599477, 634861, 630203, 638661, 538612, 550906, 391450]
    size_video5 = [450283, 398865, 350812, 382355, 411561, 318564, 352642, 437162, 374758, 362795, 353220, 405134, 386351, 434409, 337059, 366214, 360831, 372963, 405596, 350713, 386472, 399894, 401853, 343800, 359903, 379700, 425781, 277716, 400396, 400508, 358218, 400322, 369834, 412837, 401088, 365161, 321064, 361565, 378327, 390680, 345516, 384505, 372093, 438281, 398987, 393804, 331053, 314107, 255954]
    size_video6 = [181801, 155580, 139857, 155432, 163442, 126289, 153295, 173849, 150710, 139105, 141840, 156148, 160746, 179801, 140051, 138313, 143509, 150616, 165384, 140881, 157671, 157812, 163927, 137654, 146754, 153938, 181901, 111155, 153605, 149029, 157421, 157488, 143881, 163444, 179328, 159914, 131610, 124011, 144254, 149991, 147968, 161857, 145210, 172312, 167025, 160064, 137507, 118421, 112270]

    priority = []

    groupList = []

    groupSize = len(allocMatrix)
    print("Initial Chunk Tables")
    for m in allocMatrix:
        print(m+":")
        print(allocMatrix[m])
    valid = False
    priority = dict()
    remainingContributions = dict()
    contributed = dict()
    i = 0
    for member in allocMatrix:
        contributed[member] = 0
        remainingContributions[member] = contributions[i] - contributed[member] 
        priority[member] = float(bandwidth[i]) + float(remainingContributions[member])/sum(contributions)
        i = i + 1
    print("Initial Priority")
    print(priority)
    while(not valid):
        valid = True
        for i in range(totalChunks):     

            # priority[i] = connections[i][1] + connectionTypeValue + contributions[i]
            # First, define a list of canditates for the next chunk, initially.. it consists of all members
            # maximumPriority = max(priority.iteritems(), key=operator.itemgetter(1))[0]
            # canditates = [k for k,v in priority.iteritems() if v == maximumPriority]
            mx_tuple = max(priority.items(),key = lambda x:x[1]) #max function will return a (key,value) tuple of the maximum value from the dictionary
            canditates =[k[0] for k in priority.items() if k[1]==mx_tuple[1]] #my_tuple[1] indicates maximum dictionary items value
            for c in canditates:
                    chunkAssignments = allocMatrix[c]
                    #print(remainingContributions)
                    #If the member does not have enough contribution to handle the segment size.. drop him
                    if (remainingContributions[c] < size_video3[i]):
                        canditates.remove(c)
                        break
                    if i > 2:
                #Check for sequences.. SOFT Constraint: DO NOT ASSIGN 3 Chunks at row unless its only one MEMBER THEN IGNORE THIS CONSTRAINT
                        if chunkAssignments[i] == 1 and chunkAssignments[i-1] == 1 and chunkAssignments[i-2] == 1 and len(canditates) > 1:
                                canditates.remove(c)
                                break
                               
            
            #print(remainingContributions) 
            print(canditates)
            # Assign the chunk
            allocMatrix[canditates[0]][i] = 1

            contributed[canditates[0]] = contributed[canditates[0]] + size_video3[i]            
            remainingContributions[canditates[0]] = remainingContributions[canditates[0]] - size_video3[i]
            # priority[canditates[0]] = priority[canditates[0]] - contributed[canditates[0]] * 100

        # Priority update: Decrease by 10% 
            priority[canditates[0]] = priority[canditates[0]] - priority[canditates[0]]*0.1
            


            #print(priority)
            # for p in priority:
            #     if(priority[canditates[0]] != p):
            #         priority[p] = priority[p] + float(priority[canditates[0]])*0.05
            #members[selectedMember][i] = 1
            #priority[selectedMember] = priority[SelectedMember] - 10/contributions[selectedMember]
        #check theres no intersection (redundant assignment) HARD condition
        for c in canditates:
            for c2 in canditates:
                if(c != c2 and valid):
                    valid = intersection(c, c2)
                else: break
    print("Generated Chunk Tables")
    for m in allocMatrix:
        print(m+":")
        print(allocMatrix[m])

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
    
def f(arrA, arrB):
    return not set(map(tuple, arrA)).isdisjoint(map(tuple, arrB))

if __name__ == "__main__":
    totalChunks = 48
    assignments, members = totalChunks, 5;
    allocationMatrix = [[0 for x in range(assignments)] for y in range(members)] 
    memberIPs = ["192.168.1.100", "192.168.199", "192.168.209", "192.168.210", "192.168.221", "192.168.225", "192.168.264", "192.168.254", "192.168.322", "192.168.221"]
    matrix = dict(zip(memberIPs, allocationMatrix))
    #print(matrix)
    contributions = [100000, 1073741824, 1073741824, 1073741824, 1073741824, 1073741824, 1073741824, 1073741824, 1073741824, 1073741824]
    bandwidth = [1.25, 1.25, 1.25, 1.25, 1.25*2, 1.25, 1.25, 1.25, 1.25*2, 1.25]
    generateChunkTable(totalChunks, matrix, contributions, bandwidth)