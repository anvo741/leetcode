# https://www.interviewcake.com/question/python3/find-duplicate-files?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23289:%20Find%20Duplicate%20Files&utm_medium=email&utm_medium=email
'''
Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them, since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return a list of tuples ↴ where:

the first item is the duplicate file
the second item is the original file

For example:

[('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
 ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
You can assume each file was only duplicated once.
'''