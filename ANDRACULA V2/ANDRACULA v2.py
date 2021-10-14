#Mission: Save time and avoid errors in the links parameterization


#    two options:
#1 - create a txt file with a table for each link
#2 - generate link from a table


#      option one - gererating a new table
#1 - ask for a base link
#2 - check the base link
#3 - create a new table




#      option two - gererating links
#1 - get link and infos from the file 
#2 - insert new infos in the new links
#3 - format and check links
#4 - write the links in a new the txt file





#____________________________________________________________________________________________

#                   IMPORTANT!!!

#       You have to install some libraries to use ANDRACULA.
#       Press Windows + R and paste:

#       pip install Unidecode
#       pip install python-time

#       You have to change the directory path too. 
#                         Just choose a good one for you

#                          Thanks for using. We hope it helps you!




#               IMPLEMENTS
#   make only the description lower. NOT all the link

#   WHY UNIDE CODE INST WORKIN?????????





import time
import unidecode

quit_program = 0
make_a_table = 1
make_links = 2

path = ('C:/Users/andre/Desktop')

def ask_to_user_if_he_wants_to_generate_links_or_generate_a_table():
    print('\n\n                           WELCOME TO ANDRACULA')    
    chosen_option = int((input('\n\n   Escolha uma opcao:\n\n1 - Criar uma nova tabela de links vazia\n2 - Gerar links a partir de uma table pronta \n')))
    if int(chosen_option) == make_a_table:
        return (make_a_table)
    if int(chosen_option) == make_links:
        return(make_links)
    
    if int(chosen_option) != make_a_table and int(chosen_option) != make_links:
        print('\nOps. Opcao invalida')
        time.sleep(5)
        return(quit_program)                

def check_interrogation_numbers(link_to_test_interrogation, type):
    
    link_to_test_interrogation = link_to_test_interrogation.split('utm_source')
    link_to_test_interrogation[1] = 'utm_source' + link_to_test_interrogation[1]

    
    if link_to_test_interrogation[0].count('?') >  2:        
        if type == 'base_link':
            link_to_test_interrogation = ('\n\nessa_url_nao_esta_no_formato_correto._favor_checar_a_quantidade_de_"?"_na_url')
            print(link_to_test_interrogation)
            time.sleep(6)
            return(link_to_test_interrogation) 
            
            
        if type == 'created_link':
            link_to_test_interrogation = ('essa_url_nao_esta_no_formato_correto._favor_checar_a_quantidade_de_"?"_na_url')
            return(link_to_test_interrogation)

    elif link_to_test_interrogation[0].count('?') ==  0:
        link_to_test_interrogation[0] = link_to_test_interrogation[0] + '?'
        link_to_test_interrogation = link_to_test_interrogation[0] + link_to_test_interrogation[1]
        if type == 'base_link':
            link_to_test_interrogation = ('\n\nessa_url_nao_esta_no_formato_correto. nao contem nenhum "?". Favor utilizar o link gerado na SMILES URL BUILDER')
            print(link_to_test_interrogation)
            time.sleep(6)
            return(link_to_test_interrogation) 
            
        if type == 'created_link':
            return(link_to_test_interrogation)  

    elif link_to_test_interrogation[0].count('?') ==  1:
         
        if link_to_test_interrogation[0][-1] != '?' and link_to_test_interrogation[0][-1] != '&':
            link_to_test_interrogation[0] = link_to_test_interrogation[0] + '&'

            if type == 'base_link':                
                print('\n                 ADICIONADO "&" NA URL') #do it after 
                link_to_test_interrogation = link_to_test_interrogation[0] + link_to_test_interrogation[1]
                return(link_to_test_interrogation) 

            if type == 'created_link':
                link_to_test_interrogation = link_to_test_interrogation[0] + link_to_test_interrogation[1]
                return(link_to_test_interrogation)               
                  
    

    elif link_to_test_interrogation[0].count('?') ==  2:
        if link_to_test_interrogation[0][-1] != '?':           
            if type == 'base_link':
                link_to_test_interrogation = ('\n\nessa_url_nao_esta_no_formato_correto._favor_checar_a_quantidade_de_"?"')
                print(link_to_test_interrogation)
                time.sleep(6)
                return(link_to_test_interrogation) 
            
            if type == 'created_link':
                link_to_test_interrogation = ('essa_url_nao_esta_no_formato_correto._favor_checar_a_quantidade_de_"?".')
                return(link_to_test_interrogation)  
        else:
            link_to_test_interrogation[0] = link_to_test_interrogation[0][:-1]
            link_to_test_interrogation[0] = link_to_test_interrogation[0] + '&'
            link_to_test_interrogation = link_to_test_interrogation[0] + link_to_test_interrogation[1]
            if type == 'base_link':
                print('\n                 ADICIONADO "&" NA URL')
                return(link_to_test_interrogation) 

            if type == 'created_link':
                return(link_to_test_interrogation)

    link_to_test_interrogation = link_to_test_interrogation[0] + link_to_test_interrogation[1]            
    return(link_to_test_interrogation)

def generate_an_empty_table():
    number_of_links = int(input('\nDigite a quantidade de links que deseja gerar: '))    
    base_link = str(input('\nCole o link referencia: ')) 
    base_link = format_links(base_link)
    if check_parametrization_parameters_and_date(base_link, 'base_link') == True:
        base_link = check_interrogation_numbers(base_link,'base_link')
        print(base_link)
        if 'essa_url_nao_esta' not in base_link:     
            txt_file_first_lines = ['Renomeie esse arquivo para "TABELA PRONTA" antes de criar os links | reads  {}\n'.format(number_of_links),'link referencia:{}\n\n'.format(base_link),'Parametros para formato:\n'' email_botao , banner , link_bot , hotel_1 , destino_1 , slot_email , slot_tarja , slot_banner , email_kv \n\n']
            empty_table_name = 'Tabela para {} links'.format(number_of_links) 

            file = open(r"{}/{}.txt".format(path,empty_table_name), "w")    
            file.writelines(txt_file_first_lines)
            for i in range(number_of_links):
                txt_file_links_lines = ['LINK {}\n'.format(i+1),'descricao: \n','formato: \n','nova_url,_se_houver: \n\n']
                file.writelines(txt_file_links_lines)
            file.close()
            print('\n\n          Tabela gerada')
            time.sleep(4)

def check_parametrization_parameters_and_date(reference_link, type):        
    parametrization_parameters = ['https://','utm_source=email&utm_medium=responsys&utm_campaign=pd_','-pm_','-ac_','-sg_','-ft_','-dt_']
    missing_parameter = []
    number_of_missing_parameters = 0
    correct_parameters = True

    #check parameters
    for i in range(len(parametrization_parameters)):
        if parametrization_parameters[i] not in reference_link:
            missing_parameter.append(parametrization_parameters[i])
            number_of_missing_parameters = number_of_missing_parameters +1
            correct_parameters = False

    if correct_parameters == False:
        if type == 'base_link':        
            print('\nLink incorreto. \nNao contem o(s) seguinte(s) parametro(s): ')
            for i in range(number_of_missing_parameters):
                print(missing_parameter[i]) 
            time.sleep(6)

        if type == 'created_link':
            reference_link = ('ALERTA:_essa_url_nao_esta_no_formato_correto._PARAMETROS_FALTANTES_NO_LINK : {} '.format(missing_parameter))
            return(reference_link)

    #check date
    if correct_parameters == True:        
        check_date = reference_link.split('-dt_')    
        if len(check_date[1]) != 8:
            correct_parameters = False            
            if type == 'base_link':
                print('\nLink nao pode ser gerado\nA data nao está no formato correto. ')                
                time.sleep(6)
            if type == 'created_link':
                reference_link = ('ALERTA:_essa_url_nao_esta_no_formato_correto._POR_FAVOR_REPORTE!_A_DATA_SE_PERDEU ')
                return(reference_link)


    if correct_parameters == True:
        if type == 'base_link':
            return(correct_parameters)
        if type == 'created_link':
            return(reference_link)         

def read_the_txt_file_and_get_the_lines():
    file = open(r"{}/TABELA PRONTA.txt".format(path),"r")
    file_lines = file.readlines()
    file.close()
    return(file_lines)

def get_the_reference_link_in_the_lines(reference_lines_to_get_the_link):    
    line_of_the_link = reference_lines_to_get_the_link[1]
    link_in_the_txt_file = line_of_the_link[16:]
    #remove spaces
    link_in_the_txt_file = remove_spaces(link_in_the_txt_file)   
    return(link_in_the_txt_file) 

def remove_spaces(string_parameter):
    while ' ' in string_parameter or '\n' in string_parameter:
        string_parameter = string_parameter.replace(' ','')
        string_parameter = string_parameter.replace('\n','')
    return(string_parameter)    

def get_the_description_format_and_url_in_the_lines(reference_lines_to_get_infos):
    loop_times = reference_lines_to_get_infos[0][-3:]
    loop_times = remove_spaces(loop_times) 

    new_links_infos = []
    new_description_index = 7
    new_format_index = 8
    new_url_index = 9

    for i in range(int(loop_times)):
        description_get = reference_lines_to_get_infos[new_description_index]
        format_get = reference_lines_to_get_infos[new_format_index]
        url_get = reference_lines_to_get_infos[new_url_index]

        description_get = remove_spaces(description_get)
        format_get = remove_spaces(format_get)
        url_get = remove_spaces(url_get)

        new_links_infos.append([description_get[10:],format_get[8:],url_get[20:]])

        new_description_index = new_description_index + 5 
        new_format_index = new_format_index +5
        new_url_index = new_url_index + 5
        
    return(new_links_infos)    

def parse_link_and_return_it(reference_link):
    
    splited_link = reference_link.split('utm_source=')
    splited_link[1] = 'utm_source=' + splited_link[1]
 
    splited_link_aux = splited_link[1].split('sg_')
    splited_link[1]= splited_link_aux[0]

    splited_link_aux[1] = '-sg_' + splited_link_aux[1]
    splited_link.append(splited_link_aux[1])

    splited_link_aux = splited_link[2].split('-ft_')
    splited_link_aux[0] = splited_link_aux[0] + ('-ft_')
    splited_link[2] = (splited_link_aux[0])

    splited_link_aux = splited_link_aux[1].split('-dt_')
    splited_link_aux[1] = ('-dt_') + splited_link_aux[1] 
    splited_link.append(splited_link_aux[1])
   

    return(tuple(splited_link))

def insert_format_description_and_url_in_the_link_and_return_it(reference_parsed_link,reference_user_links_parameters,i):
    new_parsed_link = list(reference_parsed_link)
    #insert url in the parsed
    if reference_user_links_parameters[i][2] != '':        
        new_parsed_link[0] = reference_user_links_parameters[i][2]      
    
    #insert description in the parsed link
    new_parsed_link[1] = new_parsed_link[1] + reference_user_links_parameters[i][0] 
    #insert format in the parsed link
    new_parsed_link[2] = new_parsed_link[2] + reference_user_links_parameters[i][1]

    link_created = new_parsed_link[0] + new_parsed_link[1] + new_parsed_link[2] + new_parsed_link[3]
    return(link_created)   
        
def change_the_format_and_return_it(format_new_link, last_part_of_the_link):
    end_of_the_link = []

    split = last_part_of_the_link.split('ft_')
    split[0] = split[0] + 'ft' + format_new_link
    aux_split = split[1].split('-dt_')
    aux_split[1] = '-dt_' + aux_split[1]
    split[1] = aux_split[1]
    end_of_the_link.append(split[0] + split[1]) 
    print(end_of_the_link)

    return(end_of_the_link)
           
def format_links(reference_link_to_formatting):

    #remove accents
    aux_link = unidecode.unidecode(reference_link_to_formatting)
    aux_link = aux_link.lower()

    while '--' in aux_link or ' ' in aux_link:
        aux_link = aux_link.replace(' ','')
        aux_link = aux_link.replace('--','-')

    reference_link_to_formatting = aux_link
 

    return(aux_link)

def check_link_parameters(link_to_be_write):
    parametrization_parameters = ['https://','utm_source=email&utm_medium=responsys&utm_campaign=pd_','-pm_','-ac_','-sg_','-ft_','-dt_']
    missing_parameter = []
    number_of_missing_parameters = 0
    correct_parameters = True
    for i in range(len(parametrization_parameters)):
        if parametrization_parameters[i] not in link_to_be_write:
            missing_parameter.append(parametrization_parameters[i])
            number_of_missing_parameters = number_of_missing_parameters +1
            correct_parameters = False
            link_to_be_write = ('Link_incorreto._Nao_contem_o(s)_seguinte(s)_parametro(s): {}'.format(missing_parameter))

    if correct_parameters == True:
        check_date = link_to_be_write.split('-dt_')         
        if len(check_date[1]) != 8:
            link_to_be_write = ('Link_nao_pode_ser_gerado._A_data_nao_esta_no_formato_correto.')
           
def check_link_and_write_it_in_a_new_file(link_to_be_write,parameters,list_of_new_links,i):    
    if 'essa_url_nao_esta' not in link_to_be_write:
        link_to_be_write = check_parametrization_parameters_and_date(link_to_be_write,'created_link')
        if 'essa_url_nao_esta' not in link_to_be_write:
            link_to_be_write = check_interrogation_numbers(link_to_be_write, 'created_link')
       
    file = open(r"{}/LINKS GERADOS.txt".format(path), "a")
    txt_file_links_lines = ['LINK {}\n'.format(i+1), '{}        {}\n__________________________________________________________\n'.format(parameters[i][0],parameters[i][1]), '{} \n\n\n'.format(link_to_be_write)]
    file.writelines(txt_file_links_lines)
    file.close()  

def main():
    generate_table_or_links = ask_to_user_if_he_wants_to_generate_links_or_generate_a_table()
    if int(generate_table_or_links) == make_a_table:
         generate_an_empty_table()
        
    if int(generate_table_or_links) == make_links: 
        txt_file_lines = read_the_txt_file_and_get_the_lines()        
        link = get_the_reference_link_in_the_lines(txt_file_lines)
        user_links_parameters = get_the_description_format_and_url_in_the_lines(txt_file_lines)
        parsed_link = parse_link_and_return_it(link)  

        #make new function to check description and change segmentation if its necessary

        list_of_new_links = []
        for i in range(len(user_links_parameters)):                     
            list_of_new_links.append(insert_format_description_and_url_in_the_link_and_return_it(parsed_link,user_links_parameters,i))
                  
        file = open(r"{}/LINKS GERADOS.txt".format(path), "w") 
        file.close()
        for i in range(len(list_of_new_links)):
            list_of_new_links[i] = format_links(list_of_new_links[i])             
            check_link_and_write_it_in_a_new_file(list_of_new_links[i],user_links_parameters,list_of_new_links,i)

        print('\n\n          Links gerados\n\n') 
        time.sleep(5)   

main()





