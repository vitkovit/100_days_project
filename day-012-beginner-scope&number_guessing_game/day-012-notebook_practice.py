

#%% Namespaces: Local vs. Global Scope
########## Scope ##########
enemies = 1 

def increase_enemies1():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies1()
print(f"enemies outside function: {enemies}")

# Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)  # if is inside of function, it is not globaly accessible

drink_potion()
# print(potion_strength) # will not work

#%% Does Python Have Block Scope?
game_level = 3
def create_enemy():
    enemies = ["skeleton", "zombie", "alien"]
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)
#%% How to Modify a Global Variable
# enemies = "skeleton"
enemies = 1
# name global fucntions wiht uppercase with _
GLOBAL_VAR = "some value that will not be changed"
def increase_enemies():
    # global enemies # bad idea, do not modify it 
    # enemies = "zombie"
    # print(f"enemies inside function: {enemies}")
    return enemies+1
# bad idea to name them the same
increase_enemies()
print(f"enemies outside function: {enemies}")
# %%
