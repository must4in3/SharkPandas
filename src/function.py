def categorize_shark_column(categories, empty_list, *table_columns):
    #the letter 'M', which in the column refers to meters, is erroneously match as a correspondence. 
    #For this reason an exception has been created inside the loop
    for line in table_columns:
        line = str(line).title().split()
        for word in line:
            if word.title()  != 'M':
                if word.title() in categories:
                    empty_list.append((word.title()+ ' shark'))
                    break
        else:
            if word.title() == 'Values':
                empty_list.append('No Values')
            else:
                empty_list.append('Other')

def categorize_activity_column(categories, empty_list, *table_columns):
    # I used the function to clean the data in a column of the dataset
    for line in table_columns:
        line = str(line).title().split()
        for word in line:
            if word.title()[:4] in categories:
                empty_list.append((word.title()[:4]))
                break
        else:
            empty_list.append('Other')

def update_categories_values_table(str_name_column,Dataset,categories):
    # The correspondence of the words was made using only the first 4 letters, 
    # because of too many different variations between the words (infinitive or -ing type).
    # For this it's better to update the previously assigned name
    # Run the function update_categories_values_table to clear the column data 
    for c in categories.split():
        Dataset[f"{str_name_column}"][Dataset[f"{str_name_column}"].str.startswith(f"{c[:4]}")] = f"{c}"

def categorize_injury_column(categories, empty_list, *table_columns):
    import re
    # I used the function to clean the data in a column of the dataset
    for line in table_columns: 
        type_injury = ''
        for c in categories:
            a = re.findall(f'{c}|{c.lower()}|{c.upper()}|{c.title()}', line)
            if len(a)>0:
                type_injury += f' {str(a[0]).title()}'
        if len(type_injury) > 0:
            empty_list.append(type_injury.strip())
        else:
            empty_list.append('Unknown')
