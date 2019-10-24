def countpossiblecourses(n,courses):

    visited = set()
    nonvisited = set()
    current = []

    courses.sort()

    for i in range(0, len(courses)):
        nonvisited.add(courses[i][0])
        nonvisited.add(courses[i][1])

    current.append(courses[0][0])
    current.append(courses[0][1])

    nonvisited.remove(courses[0][0])
    nonvisited.remove(courses[0][1])

    for i in range(1,len(courses)):
        if (courses[i][0] != current[0]):
            visited.add(current[0])
            current.remove(current[0])
        if(courses[i][1] in visited and (courses[i][0] in current or courses[i][0] in visited) ):
            return False
        else:
            if(courses[i][0] not in current):
                current.append(courses[i][0])
            if(courses[i][0] in nonvisited):
                nonvisited.remove(courses[i][0])
            if ((courses[i][1] not in current) and (courses[i][1] not in visited)):
                current.append(courses[i][1])
            elif((courses[i][1]  in current) and (courses[i][1] not in visited)):
                visited.add(courses[i][1])
                current.remove(courses[i][1])
            if (courses[i][1] in nonvisited):
                nonvisited.remove(courses[i][1])

            current.sort()






    return True


#print(countpossiblecourses(5,[[0,1],[0,5],[1,2],[2,3],[3,4],[4,6]]))
#print(countpossiblecourses(5,[[1,0],[2,1],[2,0],[3,1]]))
#print(countpossiblecourses(5,[[0,1],[1,2],[2,0]]))
#print(countpossiblecourses(1,[[1,0],[0,1]]))
#print(countpossiblecourses(1,[[1,0],[0,2],[2,1]]))
#print(countpossiblecourses(4,[[1,0],[2,1],[3,2],[1,3]]))
print(countpossiblecourses(3,[[0,2],[1,2],[2,0]]))







