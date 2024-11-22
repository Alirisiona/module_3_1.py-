calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    s = str(string)
    string_info = (len(s), s.upper(), s.lower())
    return string_info


def is_contains(string, list_to_search):
    count_calls()
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if string != str(list_to_search[i]).lower():
            otvet = False
            continue
        else:
            otvet = True
            break
    return otvet 


print (string_info("serenity"))
print (string_info("sea of serenity"))
print (is_contains("elements", ["fire", "water", "earth", "air"])) # Нет совпадений
print (is_contains("summer",["seasons", "winter","spring","sumMER","autumn"])) # Urban ~ urBAN

print (calls)