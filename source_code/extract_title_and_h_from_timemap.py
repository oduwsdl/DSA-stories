import os

from bs4 import BeautifulSoup

def extract_text_from_title_and_h(htmlbuffer):

    alltext = ""

    soup = BeautifulSoup(htmlbuffer)

    try:
        alltext += soup.title.string + '\n'
    except TypeError:
        # this happens if the title is empty
        pass
        #print(htmlbuffer) 
    except AttributeError:
        # this happens if the title is empty
        pass

    for counter in range(1, 7):
    
        for header in soup.find_all('h{}'.format(counter)):

            alltext += header.get_text() + '\n'

    return alltext


def extract_title_and_h_from_seed_list(timemap_file, collection_directory):

    text_dir = "{}/text/".format(collection_directory)

    with open(timemap_file) as timemap_reader:

        for line in timemap_reader:

            line = line.strip()

            fields = line.split('\t')

            uri_id = fields[0]
            dt = fields[1]

            htmlfilename = "{}/html/{}/{}.html".format(collection_directory, uri_id, dt)

            if not os.path.exists(htmlfilename):
                continue

            if not os.path.exists(text_dir):
                os.makedirs(text_dir)

            text_file = "{}{}/{}.txt".format(text_dir, uri_id, dt)

            if os.path.exists(text_file):
                continue

            if not os.path.exists("{}{}".format(text_dir, uri_id)):
                os.makedirs("{}{}".format(text_dir, uri_id)) 

            htmlbuffer = ""

            with open(htmlfilename) as htmlfile:
                
                for line in htmlfile:
                    htmlbuffer += line

            text = extract_text_from_title_and_h(htmlbuffer)

            with open(text_file, "w") as writer:

                writer.write(text.encode('utf-8'))

        
