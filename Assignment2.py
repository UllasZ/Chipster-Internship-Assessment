data = []

doc_string = '''
    'data' is basically a list which acts as a hash table by storing the value and it's hash key as tuple.
    
    Insert function :
    - Takes in the argument, compares it's hash value in the list and inserts.
    - The data is sorted after insertion, in increasing order.
    
    Search and Delete functions:
    - Search for the data by argument's hash value and returns the result if found. 
    - The delete function further removes the data from the list.    
'''

def insert(ele):
    if (hash(ele), ele) in data:
        return "Data already exists.\n"
    else:
        data.append((hash(ele), ele))
        return f"Data inserted successfully!\n{sorted(data)}\n"


def search(ele):
    for i in data:
        if hash(ele) in i:
            return f"\nData successfully found : {(hash(ele), ele)}\n"
        return "Search Failed. Data not found\n"


def delete(ele):
    for i in data:
        if hash(ele) in i:
            data.remove(i)
            return f"Data Deleted : {i}\n"
        return "Data not found.\n"


# Driver Code
if __name__ == "__main__":

    i1 = insert("Ullas")
    print(i1)

    i2 = insert("Seema")
    print(i2)

    i3 = insert("Vikas")
    print(i3)

    i4 = insert("Sandy")
    print(i4)

    i5 = insert("Seema")
    print(i5)

    s1 = search("Ullas")
    print(s1)

    s2 = search("SP")
    print(s2)

    d1 = delete("Ullas")
    print(d1)

    d2 = delete("Vicky")
    print(d2)


'''
Expected Output:

    Data inserted successfully!
    [(4609993326100231197, 'Ullas')]

    Data inserted successfully!
    [(-6858884928966607885, 'Seema'), (4609993326100231197, 'Ullas')]

    Data inserted successfully!
    [(-6858884928966607885, 'Seema'), (4609993326100231197, 'Ullas'), (5664976374671742820, 'Vikas')]

    Data inserted successfully!
    [(-6858884928966607885, 'Seema'), (-5831752694732511001, 'Sandy'), (4609993326100231197, 'Ullas'), (5664976374671742820, 'Vikas')]

    Data already exists.


    Data successfully found : (4609993326100231197, 'Ullas')

    Search Failed. Data not found

    Data Deleted : (4609993326100231197, 'Ullas')

    Data not found.

'''
