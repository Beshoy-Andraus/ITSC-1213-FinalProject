
def addtoinventory(dictionary: dict, key, value):
    dictionary[key] = value

tools = {}

addtoinventory(tools, "pickaxe", ["A simple tool, could be used for woodcutting, but maybe combat", 10, 5])
addtoinventory(tools, "sword", ["You had this sword for a while. It aged a bit, but it gets the job done", 30, 15])

print(tools["pickaxe"][0])
def iteminformation(dictionary: dict, key, targetvalue):
    if key not in dictionary:
        return "item not found"
    if targetvalue > len(dictionary) or targetvalue < 0:
        return f"Invalid descriptor for {key}"
    return dictionary[key][targetvalue]
iteminformation(tools, "pickaxe", 0)
