import text
import view
import model

my_pb = model.Phonebook()
def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                my_pb.open()
                view.print_message(text.load_successful)
            case 2:
                my_pb.save()
                view.print_message(text.save_successful)
            case 3:
                pb = my_pb.load()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = my_pb.search(key_word)
                view.print_contacts(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = my_pb.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        view.print_contacts(result, '')
                        current_id = result[0].get('id')
                    new_contact = view.input_contact(text.change_contact)
                    name = my_pb.change(new_contact, current_id)
                    view.print_message(text.change_successful(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 7:
                key_word = view.input_search(text.input_delete)
                result = my_pb.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    name = my_pb.delete(current_id)
                    my_pb.change_order_index()
                    view.print_message(text.delete_successful(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 8:
                view.print_message(text.close_successful)
                my_pb.close()

                    

                

