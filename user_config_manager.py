def add_setting(dictt,tup):
    k1,v1=tup
    k=k1.lower()
    v=v1.lower()
    if k in dictt:
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    else:
        dictt[k]=v
        return f"Setting '{k}' added with value '{v}' successfully!"
def update_setting(dictt,tup):
    k1,v1=tup
    k=k1.lower()
    v=v1.lower()
    if k in dictt:
        dictt[k]=v
        return f"Setting '{k}' updated to '{v}' successfully!"
    else:
        return f"Setting '{k}' does not exist! Cannot update a non-existing setting."
def delete_setting(dictt,key):
    k=key.lower()
    if k in dictt:
        del dictt[k]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
def view_settings(dictt):
    if not dictt:
        return f"No settings available."
    else:
        s=f"Current User Settings:\n"
        for k,v in dictt.items():
            k1=k.capitalize()
            s+=f"{k1}: {v}\n"
        return s
test_settings={'theme': 'light'}
print(view_settings(test_settings))
