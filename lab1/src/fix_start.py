'''
Created on 2014��3��24��

@author: MAYUAN
'''

def fix_start(string):
    # replace all the characters equal to the first
    return string[0] + string[1:].replace(string[0], "*")

if __name__ == '__main__':
    # get the input string
    string = raw_input("Insert a string:\n>")
    
    # print the computed string
    print fix_start(string)