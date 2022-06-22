import checking_string as ch_st

def check_file(guid_contact, text_cont):
    find_list = []
    with open(guid_contact, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if ch_st.find_text(text_cont, line):
                find_list.append(line)
    return find_list        

