'''

    Advent of Code 2021: https://adventofcode.com/
    Login through GitHub

'''

def day1p1():
    '''
    '''
    depths = open('AdventOfCodeP1.txt','r').readlines()
    curr = int(depths[0])
    result=0
    
    for i in range(len(depths)):
        if int(depths[i]) > curr:
            result += 1
        curr = int(depths[i])

    return result

def day1p2():
    depths = open('AdventOfCodeP1.txt','r').readlines()
    curr = int(depths[0])+int(depths[1])+int(depths[2])
    result=0
    
    for i in range(len(depths)-2):
        if int(depths[i])+int(depths[i+1])+int(depths[i+2]) > curr:
            result += 1
        curr = int(depths[i])+int(depths[i+1])+int(depths[i+2])

    return result

def day2p1():
    steps = open('AdventOfCodeP2.txt').readlines()
    horiz=0
    depth=0
    
    for step in steps:
        split = step.split()
        if split[0] == 'forward': 
            horiz += int(split[1])
        elif split[0] == 'up': 
            depth -= int(split[1])
        elif split[0] == 'down': 
            depth += int(split[1])
        else: 
            return 'big oops'
        
    return horiz*depth

def day2p2():
    steps = open('AdventOfCodeP2.txt').readlines()
    horiz=0
    depth=0
    aim=0
    
    for step in steps:
        split = step.split()
        if split[0] == 'forward': 
            horiz += int(split[1])
            depth += int(split[1])*aim
        elif split[0] == 'up': 
            aim -= int(split[1])
        elif split[0] == 'down': 
            aim += int(split[1])
        else: 
            return 'big oops'
        
    return horiz*depth

def day3p1():
    lines = open('AdventOfCodeP3.txt').read().split()
    gamma = ''
    epsilon = ''
    
    for i in range(len(lines[0])):
        zero = 0
        one = 0
        for line in lines:
            if line[i] == '1':
                one += 1
            elif line[i] == '0':
                zero += 1
        if one > zero:
            gamma += '1'
            epsilon += '0'
        elif zero > one:
            gamma += '0'
            epsilon += '1'
    print(gamma,epsilon)
    return int(gamma, 2)*int(epsilon,2)
            
def day3p2():
    lines = open('AdventOfCodeP3.txt').read().split()
    oxygen = []
    carbon = []
    
    for i in range(len(lines[0])):
        
    
    
    
        