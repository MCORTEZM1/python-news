def format_date(date): 
    return date.strftime('%m/%d/%y')

from datetime import datetime 


def format_url(url): 
    # This code removes all extraneous information from a URL string, leaving only the domain name. 
    # Note that the methods we use, like replace() and split(), behave exactly the same as they do in JavaScript.
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]


def format_plural(amount, word): 
    if amount != 1: 
        return word + 's'
    
    return word 


# can run any python file to test; here like 'python app/utils/filters.py' in the command line 
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))
# print(format_date(datetime.now()))
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))
