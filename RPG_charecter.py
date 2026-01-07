full_dot = '●'
empty_dot = '○'
def create_character(name,strength,intel,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if not name:
        return "The character should have a name"
    if len(name)>10:
        return "The character name is too long"
    if name.find(" ")!=-1:
        return "The character name should not contain spaces"
    if (not isinstance(strength,int)) or (not isinstance(intel,int)) or (not isinstance(charisma,int)):
        return "All stats should be integers"
    if (strength<1) or (intel<1) or (charisma<1):
        return "All stats should be no less than 1"
    if (strength>4) or (intel>4) or (charisma>4):
        return "All stats should be no more than 4"
    if strength+intel+charisma!=7:
        return "The character should start with 7 points"
    return name+"\n"+"STR "+(full_dot*strength)+(empty_dot*(10-strength))+"\n"+"INT "+(full_dot*intel)+(empty_dot*(10-intel))+"\n"+"CHA "+(full_dot*charisma)+(empty_dot*(10-charisma))
print(create_character('ren', 4, 2, 1))
    
    
