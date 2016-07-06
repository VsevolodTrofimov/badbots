from math import *
parrot = 1     # min distance

# Adapts data, so my code works
def find_path (player_cords, aim_cords, walls):
    line_cords_start = []
    line_cords_end = []
    for i in range(0, len(player_cords)):       # Makes from one array two arrays one with first points and anothe with the seconds [x,y,x..]
        line_cords_start.append(walls[i][0][0])
        line_cords_start.append(walls[i][0][1])
        line_cords_end.append(walls[i][1][0])
        line_cords_end.append(walls[i][1][1])
    way_map = []
    way_map = way (player_cords, aim_cords, line_cords_start, line_cords_end, way_map, [0, 0], player_cords) # starts the main code
    way_map = way_map[0]
    path ({})
    for j in range(0, len(way_map)/2-1):      # I`m not sure about this way of filling path
        path.append({
            "x": way_map[j],
            "y": way_map[j+1],
        })
    return path



def angle_calculation (player_cords, aim_cords, alfa):
    # finding sin and cos
    r = sqrt((player_cords[1]-aim_cords[1])**2 + (player_cords[0]-aim_cords[0])**2)
    s = (aim_cords[1]-player_cords[1])/r
    c = (aim_cords[0]-player_cords[0])/r
    # compare to understand which angle to choose
    if(s>=0):
        if(c>=0):
            betta = asin(s)
        else:
            betta = pi-asin(s)
    else:
        if(c>=0):
            betta = asin(s)
        else:
            betta = -pi-asin(s)
    if (alfa>=0):
        alfa = betta - alfa
    else:
        alfa += betta
    return alfa



def intersection_check (player_cords, aim_cords, line_cords_start, line_cords_end):
    # finding equations of lines
    k_1 = (player_cords[1] - aim_cords[1]) / (player_cords[0] - aim_cords[0])
    b_1 = player_cords[1] - (k_1*player_cords[0])
    k_2 = (line_cords_start[1] - line_cords_end[1]) / (line_cords_start[0] - line_cords_end[0])
    b_2 = line_cords_start[1] - (k_2*line_cords_start[0])
    # intersection point v = x, w = y
    v = (k_1 - k_2) / (b_1 - b_2)
    w = v*k_1 + b_1
    # compare to find out whether intersection point appertains to segments
    if player_cords[0] < aim_cords[0]:
        player_cords[0], aim_cords[1] = aim_cords[0], player_cords[0]
    if player_cords[1] < aim_cords[1]:
        player_cords[1], aim_cords[1] = aim_cords[1], player_cords[1]
    if line_cords_start[0] < line_cords_end[0]:
        line_cords_start[0], line_cords_end[0] = line_cords_end[0], line_cords_start[0]
    if line_cords_start[1] < line_cords_end[1]:
        line_cords_start[1], line_cords_end[1] = line_cords_end[1], line_cords_start[1]
    # if point appertains...
    if player_cords[0]>v and aim_cords[0]<v and line_cords_start[0]>v and line_cords_end[0]<v and player_cords[1]>w and aim_cords[1]<w and line_cords_start[1]>w and line_cords_end[1]<w:
        return [True, v, w, line_cords_start, line_cords_end]
    else:
        return [False]



# the main function
def way (player_cords, aim_cords, line_cords_start, line_cords_end, way_map, cords, player):  
    # Definition of several lists which we`ll need later     
    rubbish_rubbish = [0]
    answer = []
    way_map = []
    answer = [True, aim_cords[0], aim_cords[1], 0, 0]                                      
    length = len(line_cords_start)
    # if the field is empty, turn aim cords and length(we don`t actuarelly need this, but in another cases it will be really useful)
    if length == 0:
        way_map.append (aim_cords[0])
        way_map.append (aim_cords[1])
        ANSWER = []
        ANSWER = [way_map, length_calculation(way_map, player)]
        return ANSWER
    # Definition of several more lists which we`ll need later     
    start = []
    end = []
    answer_2 = []
    rubbish = []
    ANSWER_1 = []
    ANSWER_2 = []
    # check all the segments on intersection
    for t in range(0, length/2 - 1):
        start = [line_cords_start[2*t], line_cords_start[2*t+1]]
        end = [line_cords_end[2*t], line_cords_end[2*t+1]]
        answer_2 = intersection_check (player_cords, aim_cords, start, end)
        # find the closest from bot
        if answer_2[0] == True and sqrt((player_cords[0] - answer[1])**2 + (player_cords[1] - answer[2])**2)>sqrt((player_cords[0] - answer_2[1])**2 + (player_cords[1] - answer_2[2])**2):
            answer = answer_2
    # if tere are no walls on our way turn map and the length of the way
    if answer[1]==aim_cords[0] and answer[2]==aim_cords[1]:
        way_map.append (aim_cords[0])
        way_map.append (aim_cords[1])
        ANSWER = []
        ANSWER = [way_map, length_calculation(way_map, player)]
        return ANSWER
    else:
        cur_aim = []
        cur_aim = [answer[1], answer[2]]
        # Look whether there are any intersections with already passed way
        for j in range(0, len(way_map)/2-2):
            start = [way_map[2*j], way_map[2*j+1]]
            end = [way_map[2*j+2], way_map[2*j+3]]
            answer_2 = intersection_check (player_cords, cur_aim, start, end)
            if answer_2[0] == True:
                j = len(way_map)
        # if no, come through free space to the wall, calculate the point we can stand, add it into map
        if answer_2[0] == False:
            intersection_point = []
            intersection_point = [answer[1], answer[2]]
            rubbish = parrot_calculation(way_map, intersection_point, answer[3], answer[4])
            way_map.append (rubbish[0])
            way_map.append (rubbish[1])
            # find the point to stand on if we go one way, add it into map, calculate the final length (to difficult to go into details)
            # this is the most difficult part of my programm, I`hope there are no mistakes, because I don`t want to reread it
            k_1 = (answer[4[1]] - answer[3[1]]) / (answer[4[0]] - answer[3[0]])
            k_2 = k_1
            b_2 = answer[2]-k_1*answer[1]
            for i in range(0, len(line_cords_start)/2-1):
                if (line_cords_start[2*i] == answer[3[0]] and line_cords_start[2*i+1] == answer[3[1]]) or (line_cords_end[2*i] == answer[3[0]] and line_cords_end[2*i+1] == answer[3[1]]):
                    k_1 = (line_cords_start[2*i+1] - line_cords_end[2*i+1]) / (line_cords_start[2*i] - line_cords_start[2*i])
                    b_1 = line_cords_start[2*i+1] - (k_1*line_cords_start[2*i])
                    v = (k_1 - k_2) / (b_1 - b_2)
                    w = v*k_1 + b_1
                    if line_cords_start[2*i] < line_cords_end[2*i]:
                        line_cords_start[2*i], line_cords_end[2*i] = line_cords_end[2*i], line_cords_start[2*i]
                    if line_cords_start[2*i+1] < line_cords_end[2*i+1]:
                        line_cords_start[2*i+1], line_cords_end[2*i+1] = line_cords_end[2*i+1], line_cords_start[2*i+1]
                    if line_cords_start[2*i+1]>w and line_cords_end[2*i+1]<w and line_cords_start[2*i]>v and line_cords_end[2*i]<v:
                        rubbish = parrot_calculation(way_map, [v, w], [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_end[2*i], line_cords_end[2*i+1]])
                        if rubbish_rubbish[0] == 0:
                            rubbish_rubbish = rubbish
                        else:
                            if sqrt((way_map[len(way_map)] - rubbish[1])**2 + (way_map[len(way_map)-1] - rubbish[0])) < sqrt((way_map[len(way_map)] - rubbish_rubbish[1])**2 + (way_map[len(way_map)-1] - rubbish_rubbish[0])):
                                rubbish_rubbish = rubbish
                    else:
                        rubbish_rubbish = parrot_calculation(way_map, [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_end[2*i], line_cords_end[2*i+1]])
            way_map.append (rubbish_rubbish[0])
            way_map.append (rubbish_rubbish[1])
            ANSWER_1 = way ([rubbish_rubbish[0], rubbish_rubbish[1]], aim_cords, line_cords_start, line_cords_end, way_map, [rubbish_rubbish[2], rubbish_rubbish[3]], player)
            # delete the last point, find another if we choose the second way, add it into map, calculate the length of this way
            way_map.pop
            way_map.pop
            k_1 = (answer[4[1]] - answer[3[1]]) / (answer[4[0]] - answer[3[0]])
            k_2 = k_1
            b_2 = answer[2]-k_1*answer[1]
            for i in range(0, len(line_cords_start)/2-1):
                if (line_cords_start[2*i] == answer[4[0]] and line_cords_start[2*i+1] == answer[4[1]]) or (line_cords_end[2*i] == answer[4[0]] and line_cords_end[2*i+1] == answer[4[1]]):
                    k_1 = (line_cords_start[2*i+1] - line_cords_end[2*i+1]) / (line_cords_start[2*i] - line_cords_start[2*i])
                    b_1 = line_cords_start[2*i+1] - (k_1*line_cords_start[2*i])
                    v = (k_1 - k_2) / (b_1 - b_2)
                    w = v*k_1 + b_1
                    if line_cords_start[2*i] < line_cords_end[2*i]:
                        line_cords_start[2*i], line_cords_end[2*i] = line_cords_end[2*i], line_cords_start[2*i]
                    if line_cords_start[2*i+1] < line_cords_end[2*i+1]:
                        line_cords_start[2*i+1], line_cords_end[2*i+1] = line_cords_end[2*i+1], line_cords_start[2*i+1]
                    if line_cords_start[2*i+1]>w and line_cords_end[2*i+1]<w and line_cords_start[2*i]>v and line_cords_end[2*i]<v:
                        rubbish = parrot_calculation(way_map, [v, w], [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_end[2*i], line_cords_end[2*i+1]])
                        if rubbish_rubbish == 0:
                            rubbish_rubbish = rubbish
                        else:
                            if sqrt((way_map[len(way_map)] - rubbish[1])**2 + (way_map[len(way_map)-1] - rubbish[0])) < sqrt((way_map[len(way_map)] - rubbish_rubbish[1])**2 + (way_map[len(way_map)-1] - rubbish_rubbish[0])):
                                rubbish_rubbish = rubbish
                    else:
                        rubbish_rubbish = parrot_calculation(way_map, [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_end[2*i], line_cords_end[2*i+1]])
            way_map.append (rubbish_rubbish[0])
            way_map.append (rubbish_rubbish[1])
            ANSWER_2 = way ([rubbish_rubbish[0], rubbish_rubbish[1]], aim_cords, line_cords_start, line_cords_end, way_map, [rubbish_rubbish[2], rubbish_rubbish[3]], player)
            # choose the shortest way
            if ANSWER_1[1]>ANSWER_2[1]:
                return ANSWER_2
            else:
                return ANSWER_1
        # if there is intersection with already passed way the operations are similar, but twise shorter
        else: 
            k_1 = (cords[1[1]] - cords[0[1]]) / (cords[1[0]] - cords[0[0]])
            k_2 = k_1
            b_2 = way_map[len(way_map)]-k_1*way_map[len(way_map)-1]
            for i in range(0, len(line_cords_start)/2-1):
                if (line_cords_start[2*i] == answer[4[0]] and line_cords_start[2*i+1] == answer[4[1]]) or (line_cords_end[2*i] == answer[4[0]] and line_cords_end[2*i+1] == answer[4[1]]):
                    k_1 = (line_cords_start[2*i+1] - line_cords_end[2*i+1]) / (line_cords_start[2*i] - line_cords_start[2*i])
                    b_1 = line_cords_start[2*i+1] - (k_1*line_cords_start[2*i])
                    v = (k_1 - k_2) / (b_1 - b_2)
                    w = v*k_1 + b_1
                    if line_cords_start[2*i] < line_cords_end[2*i]:
                        line_cords_start[2*i], line_cords_end[2*i] = line_cords_end[2*i], line_cords_start[2*i]
                    if line_cords_start[2*i+1] < line_cords_end[2*i+1]:
                        line_cords_start[2*i+1], line_cords_end[2*i+1] = line_cords_end[2*i+1], line_cords_start[2*i+1]
                    if line_cords_start[2*i+1]>w and line_cords_end[2*i+1]<w and line_cords_start[2*i]>v and line_cords_end[2*i]<v:
                        rubbish = parrot_calculation(way_map, [v, w], [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_end[2*i], line_cords_end[2*i+1]])
                        if rubbish_rubbish == 0:
                            rubbish_rubbish = rubbish
                        else:
                            if sqrt((way_map[len(way_map)] - rubbish[1])**2 + (way_map[len(way_map)-1] - rubbish[0])) < sqrt((way_map[len(way_map)] - rubbish_rubbish[1])**2 + (way_map[len(way_map)-1] - rubbish_rubbish[0])):
                                rubbish_rubbish = rubbish
                    else:
                        rubbish_rubbish = parrot_calculation(way_map, [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_start[2*i], line_cords_start[2*i+1]], [line_cords_end[2*i], line_cords_end[2*i+1]])
            way_map.append (rubbish_rubbish[0])
            way_map.append (rubbish_rubbish[1])
            ANSWER_1 = way ([rubbish_rubbish[0], rubbish_rubbish[1]], aim_cords, line_cords_start, line_cords_end, way_map, [rubbish_rubbish[2], rubbish_rubbish[3]], player)
            return ANSWER_1



# this easy function doesn`t need any comments
def length_calculation(way_map, player_cords):
    length = sqrt((player_cords[0]-way_map[0])**2 + (player_cords[1]-way_map[1])**2)
    for i in range(2, len(way_map)/2-2):
        length += sqrt((way_map[i*2]-way_map[i*2+2])**2 + (way_map[i*2+1]-way_map[i*2+3])**2)
    return length


# this one finds the point, closest to the point on the wall
def parrot_calculation(way_map, intersection_point, line_cords_start, line_cords_end):
    k_1 = (line_cords_end[1] - line_cords_start[1]) / (line_cords_end[0] - line_cords_start[0])
    k_2 = 1/k_1
    b_2 = intersection_point[1] - (k_2*intersection_point[0])
    v_1 = (-(2*k_2*b_2 - 2*intersection_point[0] - 2*intersection_point[1]*k_2) - sqrt((2*k_2*b_2 - 2*intersection_point[0] - 2*intersection_point[1]*k_2)**2 - 4*(-(parrot**2)+intersection_point[0]**2+intersection_point[1]**2+b_2**2-2*intersection_point[1]*b_2)*(k_2**2+1)))/(2*(k**2+1))
    v_2 = (-(2*k_2*b_2 - 2*intersection_point[0] - 2*intersection_point[1]*k_2) + sqrt((2*k_2*b_2 - 2*intersection_point[0] - 2*intersection_point[1]*k_2)**2 - 4*(-(parrot**2)+intersection_point[0]**2+intersection_point[1]**2+b_2**2-2*intersection_point[1]*b_2)*(k_2**2+1)))/(2*(k**2+1))
    w_1 = k_2*v_1+n_2
    w_2 = k_2*v_2+n_2
    l = len(way_map)
    if sqrt((way_map[l]-w_2)**2+(way_map[l+1]-v_2)**2) < sqrt((way_map[l+3]-w_1)**2+(way_map[l+1]-v_1)**2):
        w_1 = w_2
        v_1 = v_2
    answer = [v_1, w_1, line_cords_start, line_cords_end]
    return answer




player_cords = [11, 6]
aim_cords = [10, 9]
walls = [[[8,-8], [8,4]],[[8,4],[2,4]],[[2,4],[2,16]],[[2,16],[6,16]],[[6,16],[6,8]],[[6,8],[12,8]],[[12,8],[12,16]],[[12,16],[15,-8]],[[8,12],[11,12]]]

p = []
p = find_path(player_cords, aim_cords, walls)
print p