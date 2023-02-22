import re

fields = {
    'Article': ['Title', 'Author', 'Journal', 'Year', 'Pages',
                'Volume', 'Language', 'Address'],
    'Book': ['Title', 'Author', 'Publisher', 'Year', 'Numpages', 'Language', 'Address'],
    'Booklet': ['Title'],
    'PhdThesis': ['Title', 'Author', 'School', 'Year', 'Address', 'Language'],
    'Conference': ['Title', 'Author', 'Booktitle', 'Year', 'Address', 'Pages', 'Language']
}

templates = {
    'Article': '{Author}{Title}{Journal}{Address}{Year}{Volume}{Pages}',
    'Book': '{Author}{Title}{Address}{Publisher}{Year}{Numpages}',
    'Booklet': '{Title}',
    'PhdThesis': '{Author}{Title}{Address}{School}{Year}',
    'Conference': '{Author}{Title}{Booktitle}{Year}{Address}'
}

separators_ru = {
    'Title': '//',
    'Author': ' ',
    'Journal': ' ',
    'Year': '-',
    'Pages': '-С',
    'Volume': '-Вып',
    'Publisher': 'Изд-во',
    'Address': ' ',
    'Booktitle': ' ',
    'Numpages': '-С',
    'School': ' '
}

separators_en = {
    'Title': '//',
    'Author': ' ',
    'Journal': ' ',
    'Year': '-',
    'Pages': '-P',
    'Volume': '-Vol',
    'Publisher': 'Pub',
    'Address': ' ',
    'Booktitle': ' ',
    'Numpages': '-P',
    'School': ' '
}


def load_file(filename):
    """
    Reads a file to a string 'biblio'
    :param filename:
    :return:
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        biblio = file.read()
        file.close()
    return biblio


def process(biblio):
    """
    Extracts all articles, books etc
    :param biblio:
    :return: data about articles in form of a list
    """
    m = re.findall(r'@(?:[^{]*)\{(?:[^,]*),\n(?:[^=]*= *\{(?:[^}]*)},\n)*(?:[^=]*= *\{(?:[^}]*)}\n)}', biblio)
    """
    This regex was created by understanding the following structure of file.
    Each record is in a common format:
    @<TYPE>{<SOME NAME>,
    [SOME NUMBER OF SPACES] <FIELD NAME> [SOME NUMBER OF SPACES] = [SOME NUMBER OF SPACES] {<FIELD VALUE>},
    <SOME NUMBER OF FIELDS>
    [SOME NUMBER OF SPACES] <FIELD NAME> [SOME NUMBER OF SPACES] = [SOME NUMBER OF SPACES] {<FIELD VALUE>}
    }
    
    first_line has this regex @(?:[^{]*)\{(?:[^,]*),\n
    fields has this regex (?:[^=]*= *\{(?:[^}]*)},\n)*(?:[^=]*= *\{(?:[^}]*)}\n)}
    
    During the creation of this regex there was one main issue: value of a field can contain special symbols such as \n and others
    """
    data = []
    for x in m:
        data.append(x)
    return data


def extract_fields(record, fields):
    """
    Extracts value of specified fields from a given article/book/etc
    :param record: an article/book/etc
    :param fields: names of needed fields
    :return: an dictionary {field: value}
    """
    output = {}
    for x in fields:
        temp = re.findall(x + ' *= *{ *[^}]*}', record)
        try:
            field = re.findall(r'\{[^}]*}', temp[0])
            field = re.findall(r'[^\W]{1,10}[^{^}]*', field[0])
            field = field[0].replace('\n', '')
            while '\n' in field:
                field = field.replace('\n', '')
            output[x] = field
        except IndexError:
            output[x] = ''
    return output


def formatted_output(record_type, fields) -> str:
    """
    Formats output according to a record type
    :param record_type: type of record (can be Article, Book, etc)
    :param fields: all extracted fields and their values
    :return: formatted record
    """
    output = ''
    if record_type == 'Article':
        output = templates[record_type].format(Author=fields['Author'], Title=fields['Title'], Journal=fields['Journal'],
                                               Address=fields['Address'], Year=fields['Year'], Volume=fields['Volume'],
                                               Pages=fields['Pages'])
    elif record_type == 'Book':
        output = templates[record_type].format(Author=fields['Author'], Title=fields['Title'], Address=fields['Address'],
                                               Publisher=fields['Publisher'], Year=fields['Year'], Numpages=fields['Numpages'])
    elif record_type == 'Booklet':
        output = templates[record_type].format(Title=fields['Title'])
    elif record_type == 'PhdThesis':
        output = templates[record_type].format(Author=fields['Author'], Title=fields['Title'], Address=fields['Address'],
                                               Year=fields['Year'], School=fields['School'])
    elif record_type == 'Conference':
        output = templates[record_type].format(Author=fields['Author'], Title=fields['Title'], Address=fields['Address'],
                                               Year=fields['Year'], Booktitle=fields['Booktitle'])
    return output


def pretty_print(data, filename):
    """
    Prints all data in a GOST format
    :param data: data to be formatted and printed
    :param filename: a file where to print
    :return: nothing
    """
    print(data)
    with open(filename, 'w', encoding='utf-8') as file:
        for record in data:
            record_type = record[record.find('@') + 1:record.find('{')].strip()
            field_values = extract_fields(record, fields[record_type])
            try:
                is_in_russian = field_values['Language'] == 'russian' or field_values['Language'] == ''
            except KeyError:
                is_in_russian = True
            for field in field_values:
                if field == 'Author':
                    field_values[field].replace('and', ',')
                if field != '' and field != 'Language':
                    if is_in_russian:
                        field_values[field] += separators_ru[field]
                    else:
                        field_values[field] += separators_en[field]
            gost_record = formatted_output(record_type, field_values)
            file.write(gost_record + '\n')
        file.close()
    return


def main():
    biblio = load_file('biblio.bib')
    data = process(biblio)
    pretty_print(data, 'ГОСТ.txt')


if __name__ == '__main__':
    main()
