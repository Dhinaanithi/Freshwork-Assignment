from crud import CRUD

#print(crud.create('age','20'))

x = CRUD()

print(x.read())

print(x.create("college","St.Joseph's Insitute of Technology"))

print(x.read())

print(x.update("college","St.Joseph's Insitute of Technology"))

print(x.delete("college"))
