import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding = 'utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

def find_word(string_list):
    """ Return a list of words that contain three digit numbers in the middle. """

    # initialize an empty list
    lst1 = []
    blank_lst = []
    # define the regular expression
    str1 = "[a-z]+\d{3}+[a-z]+"
    # loop through each line of the string list 
    for line in string_list:
    # find all the words that match the regular expression in each line
        found_words = re.findall(str1, line)
        blank_lst.append(found_words)
    # loop through the found words and add the words to your empty list 
    for word in blank_lst:
    #return the list of all words that start with the letter B, E, or T
        if word[0] == 'B' or word[0] == 'E' or word[0] == 'T':
            lst1.append(word)
    return lst1

def find_days(string_list):
    """ Return a list of days from the list of strings the dates format in the text are MM/DD/YYYY. """  

    # initialize an empty list
    lst2 = []
    blank_lst2 = []
    # define the regular expression
    str2 = "[0-9]{1-2}.[0-9]{1-2}.[0-9]{4}"
    # loop through each line of the string list
    for line in string_list:
    # find all the dates that match the regular expression in each line
        found_dates = re.findall(str2, line)
        blank_lst2.append(found_dates)
    # loop through the found dates and only add the days to your empty list 
    for date in blank_lst2:
        day_str = "[0-9]{1-2}([0-9]{1-2})"
        day = re.findall(day_str, date)
        lst2.append(day)
    #return the list of days
    return lst2

def find_domains(string_list):
    """ Return a list of web address domains from the list of strings the domains of a wbsite are after www. """

    # initialize an empty list
    lst3 = []
    extra_lst = []
    blank_lst3 = []
    # define the regular expression
    str3 = "http.+"
    # loop through each line of the string list
    for line in string_list:
    # find all the domains that match the regular expression in each line
        found_domains = re.findall(str3, line)
        blank_lst3.append(found_domains)
    # loop through the found domains
        for domain in blank_lst3:
            str4 = "https?.{3}+(.+)"
    # get the domain name by splitting the (//) after the https or http to get the website name
            www_name = re.findall(str4, domain)
            extra_lst.append(www_name)
    # then strip the www. to get only the domain name
        for www_name in extra_lst:
            if "www." in www_name:
                domain_name = www_name.strip("www.")
            else:
                domain_name = www_name
    # add the domains to your empty list
            lst3.append(domain_name)
    
    #return the list of domains
    return lst3

class TestAllMethods(unittest.TestCase):


    def test_find_word(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        word_list = find_word(string_list)
        self.assertEqual(len(word_list),4)
    
    def test_find_days(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        days_list = find_days(string_list)
        self.assertEqual(days_list,['23', '12', '31', '4', '1', '4'])
    
    def test_domains(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        domain_list = find_domains(string_list)
        self.assertEqual(domain_list,['pythex.org', 'si.umich.edu', 'sabapivot.com', 'stars.chromeexperiments.com', 'theofficestaremachine.com', 'regex101.com'])


def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()