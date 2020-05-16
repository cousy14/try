documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},                          {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_person_by_doc_no(docs):
  doc_no = input("Введите номер документа для определения его владельца:")
  sign = 0
  for doc in docs:
    if doc["number"] == doc_no:
      print(doc.get("name"))
      sign += 1
  if sign == 0:
    print(f"Номер документа {doc_no} отсутсвует в базе данных, попробуйте еще раз")

# get_person_by_doc_no(documents)



def get_list_docs(docs):
  print("\n".join([" ".join(doc.values()) for doc in docs]))
# get_list_docs(documents)



def add_doc(docs,dirs):
  doc_num = input("Введите номер документа: ")
  doc_type = input("Введите тип документа: ")
  doc_person = input("Введите имя владельца документа: ")
  doc_shelf = input("Введите номер полки: ")
  if doc_shelf not in dirs.keys():
    print("Введен несуществующий номер полки")
  else:
    dirs[doc_shelf].append(doc_num)
    docs.append({"type": doc_type, "number": doc_num, "name": doc_person})
  print(docs,dirs)
  return docs, dirs

# documents, directories = add_doc(documents, directories)



def get_shelf_by_doc_no(dirs):
  doc_no = input("Введите номер документа для определения номера полки с досье:")
  sign = 0
  for doc in dirs:
    if doc_no in dirs[doc]:
      print(f"Полка номер - {doc}")
      sign += 1
  if sign == 0:
    print(f"Номер документа {doc_no} отсутсвует в базе данных, попробуйте еще раз")

# get_shelf_by_doc_no(directories)

def get_check_name(docs):
  for doc in docs:
    try:
      print(doc["name"])
      # print(f"{doc.values[name]}")
    except KeyError:
      print(f"name отсутствует в документе")
   
# get_check_name(documents)

def main():
  while True:
    user_input = input('Введите команду: ')
    if user_input == 'p':
      get_person_by_doc_no(documents)
    elif user_input == 's':
      get_shelf_by_doc_no(directories)
    elif user_input == 'l':
      get_list_docs(documents)
    elif user_input == 'a':
      add_doc(documents, directories)
    elif user_input == 'c':
      get_check_name(documents)
    elif user_input == 'q':
      break


main()