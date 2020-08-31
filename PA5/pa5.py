import random, re, csv

CANNED_QUESTION_FILE = 'files/canned_question.txt'
CANNED_RESPONSE_FILE = 'files/canned_response.txt'
CONVERSATION_FILE ='files/conversation.txt'
KEYWORD_FILE = 'files/keyword_response.tsv'

def main():
    print('Irasshaimase!')
    
    # make dictionary & list for response
    canned_q_to_r = load_canned_responses(CANNED_QUESTION_FILE, CANNED_RESPONSE_FILE, CONVERSATION_FILE)
    keyword_to_r = load_keyword_responses(KEYWORD_FILE)
    
    # run chatbot
    while True:
        input_text = input('\n>>> ')
        if 'bye' in input_text:
            print('Arigatou Gozaimashita!')
            break
        else:
            print(select_response(input_text, canned_q_to_r, keyword_to_r))


###### DO NOT EDIT ABOVE THIS LINE ######


# 0. functions for reading files and make dictionary/list  
def load_canned_responses(question_file, response_file, conversation_file):
    """
    TODO
    1. open and read question_file and response_file, make them as response dictionary
    2. read conversation_file and make all pairs of lines in a row as reasponse dictionary
    1 and 2 must be one dictionary
    """
    #IMPLEMENT YOUR CODE
    canned_response_dic = {}
    A = []
    B = []
    C = []
    
    with open(question_file , 'r') as question:
        for line in question:
            A.append(line.strip('\n'))
    with open(response_file , 'r') as response:
        for line in response:
            B.append(line.strip('\n'))    
    for i in range(len(A)):
        canned_response_dic[A[i]] = B[i]        
    with open(conversation_file , 'r') as conver:
        for line in conver:
            C.append(line.strip('\n')) 
    for x in range(len(C) -1): #ตัวสุดท้ายไม่มีคำตอบ
        canned_response_dic[C[x]] = C[x+1]

    return canned_response_dic

def load_keyword_responses(keyword_tsv_file):
    """
    TODO
    read keyword_tsv_file and return list of tuples [(keyword, response),...]
    """
    #IMPLEMENT YOUR CODE
    keyword_response_list = []
    with open(keyword_tsv_file, 'r') as key:
        for i in key:
            x = i.split('\t')
            keyword_response_list.append((x[0], x[1].strip()))
    

    return keyword_response_list


# 1. canned response
def canned_response(input_text, canned_response_dic):
    #IMPLEMENT YOUR CODE
    response = None
    try:
        return canned_response_dic[input_text]
    except:    
        return response

    


# 2. Yes/No response
def yes_no_response(input_text):
    #IMPLEMENT YOUR CODE
    #are กับ were ต้องใช้ am เลยยกเว้น
    input = input_text.strip('?').split(' ')
    verb = ['Be','Can','Could','Do','Have','May','Must','Need','Ought','Shall','Should','Will','Would','Is','Am','Was']
    if input[0] in verb and len(input) == 3 : 
        response = 'Yes, I ' + input[0].lower() + ' ' + ' '.join(input[2:-1]) + input[-1].strip('?') + '. ' + input[0] + ' you?'     
    elif input[0] in verb: 
        response = 'Yes, I ' + input[0].lower() + ' ' + ' '.join(input[2:-1]) + ' ' + input[-1].strip('?') + '. ' + input[0] + ' you?'
    elif input[0] == 'Are' and len(input) == 3 : 
        response = 'Yes, I ' + 'am' + ' ' + ' '.join(input[2:-1]) + input[-1].strip('?') + '. ' + input[0] + ' you?'     
    elif input[0] == 'Are': 
        response = 'Yes, I ' + 'am' + ' ' + ' '.join(input[2:-1]) + ' ' + input[-1].strip('?') + '. ' + input[0] + ' you?'
    elif input[0] == 'Were' and len(input) == 3 : 
        response = 'Yes, I ' + 'was' + ' ' + ' '.join(input[2:-1]) + input[-1].strip('?') + '. ' + input[0] + ' you?'     
    elif input[0] == 'Were': 
        response = 'Yes, I ' + 'was' + ' ' + ' '.join(input[2:-1]) + ' ' + input[-1].strip('?') + '. ' + input[0] + ' you?'
    else:
        response = None
    return response


    response = None

    return response


# 3. Keyword to response
def keyword_response(input_text, keyword_response_list):
    #IMPLEMENT YOUR CODE

    input_list = input_text.lower().strip('.').split()
    for key in keyword_response_list:
        keylist = key[0].split()
        if len(keylist) == 1:
            for i in range(len(input_list)):
                if keylist[0] == input_list[i]:
                    return key[1]
                
        if len(keylist) == 2:
            for i in range(len(input_list) - 1):
                if keylist[0] == input_list[i] and keylist[1] == input_list[i + 1]:
                    return key[1]            



    

    return None


# 4. Reflecting
def reflecting(input_text):
    #IMPLEMENT YOUR CODE
    #ใช้ expression re เอาแค่ you ถึง me
    #don't ด้วย
    a = re.compile(r'''[yY]ou \w+.?t? \w+.?\w+?\s?\w+?\s?me\.''')
    b = a.findall(input_text)
    if b == [] or ' and ' in str(b):
        return None
    else:
        c = b[0].split()
        if c[1] == 'are':
            return 'What makes you think I am ' + ' '.join(c[2:-1]) + ' you?' #are = am
        elif c[1] == 'were':
            return 'What makes you think I was ' + ' '.join(c[2:-1]) + ' you?' #were = was
        else:
            return 'What makes you think I ' + ' '.join(c[1:-1]) + ' you?'

    

# 5. Repeating
def repeating(input_text):
    #IMPLEMENT YOUR CODE
    ans = ''
    text = input_text.strip('.').split()
    noun_dict = {'I':'you','me':'you','my':'your','mine':'yours','am':'are'}
    for i in range(len(text)):
        if i == 0 and text[0] == 'I':
            ans += ' ' + 'You'
        else:
            try:
                ans += ' ' + noun_dict[text[i]]
            except:
                try:
                    ans += ' ' + noun_dict[text[i].lower()].capitalize() #ตัวใหญ่
                except:
                    ans += ' ' + text[i]    
    if ans.strip() + '.' == input_text:
        return None
    else:
        return ans.strip() + '?' 






# 6. Give up
def give_up():
    #IMPLEMENT YOUR CODE
    choices = ['Please go on.', "That's very interesting.", "I see."]

    return choices[random.randint(0,2)]


# function to select response
def select_response(input_text:str, canned_response_dic:dict, keyword_response_list:list):
    """
    :param input_text: string received as user input
    :param canned_question_dic: dictionary where questions are keys and responses are values (for 1.)
    :param keyword_response_list: list of tuples: [(keyword, response),...] (for 3.)
    :return: selected_response
    TODO select response according to the priority of functions
    priority of functions:
        1. canned_response(input_text, canned_response_dic)
        2. yes_no_response(input_text)
        3. keyword_response(input_text, keyword_response_list)
        4. reflecting(input_text)
        5. repeating(input_text)
        6. give up()
    """
    #IMPLEMENT YOUR CODE
    if canned_response(input_text, canned_response_dic) != None:
        return canned_response(input_text, canned_response_dic)
    elif yes_no_response(input_text) != None:
        return yes_no_response(input_text)
    elif keyword_response(input_text, keyword_response_list) != None:
        return keyword_response(input_text, keyword_response_list)
    elif reflecting(input_text) != None:
        return reflecting(input_text)
    elif repeating(input_text) != None:
        return repeating(input_text)
    else:
        return give_up()
    
    


###### DO NOT EDIT BELOW THIS LINE ######

if __name__ == '__main__':
    main()