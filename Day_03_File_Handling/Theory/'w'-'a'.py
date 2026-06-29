#"w" - OPEN FOR WRITING, TRUNCATING THE FILE FIRST
f = open("'w'-'a'-demo.txt", "w")
f.write("Hola")
f.close()


#"a" - OPEN FOR WRITING, APPENDING TO THE END OF THE FILE IF IT EXISTS 
f = open("'w'-'a'-demo.txt", "a")
f.write("\nCiao")
f.close()

# "r+" = read + overwrite - pointer posi at start - (NO TRUNCATE)
# "w+" = read + overwrite - pointer posi dont matter becoz --> (TRUNCATE) file first
# "a+" = read + append - pointer posi at end - (NO TRUNCATE)