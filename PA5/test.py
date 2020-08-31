import os, sys
try:
    del sys.modules['pa5']
except:
    pass
from pa5 import *

canned_response_dic = load_canned_responses('files/canned_question.txt', 'files/canned_response.txt', 'files/conversation.txt')
keyword_response_list = load_keyword_responses('files/keyword_response.tsv')

def main():
    choice = input('1: canned\n2: yes/no\n3: keyword\n4: reflecting\n5: repeating\n6: give up\nselect function to test : ')
    if choice not in ['1','2','3','4','5','6']:
        return
    while True:
        input_text = input('\nINPUT >>> ')
        if 'quit' == input_text: 
            break
        elif choice == '1':
            print(canned_response(input_text, canned_response_dic))
        elif choice == '2':
            print(yes_no_response(input_text))
        elif choice == '3':
            print(keyword_response(input_text, keyword_response_list))
        elif choice == '4':
            print(reflecting(input_text))
        elif choice == '5':
            print(repeating(input_text))
        elif choice == '6':
            print(give_up())

if __name__ == '__main__':
    main()