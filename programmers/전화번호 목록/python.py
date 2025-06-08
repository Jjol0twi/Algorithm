def solution(phone_book):
    answer = True
    '''
    # phone_book_dic = {}
    # for i in range(len(phone_book)):
    #     phone_book_dic[i] = phone_book[i]    

    # phone_book_dic = {i : phone_book[i] for i in range(len(phone_book))}

    '''
    phone_book_dic = {i: len(i) for i in phone_book}

    print(phone_book_dic)
    return answer
