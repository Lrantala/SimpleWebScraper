import requests
import sys


def get_website_contents():
    """This function retrieves and returns the contents of the
    website that is passed to it as an argument."""
    website = requests.get("http://www.darklyrics.com/lyrics/kingdiamond/abigail.html")
    try:
        website.raise_for_status()
    except Exception as exception:
        print("Error encountered: %s" % exception)
    return website.content


def write_website_to_file(contents):
    """This function writes the website contents to a file
    as bytes."""
    write_contents_bytes = bytearray(contents)
    try:
        with open("Abigail.scrape", "wb") as file:
            file.write(write_contents_bytes)
    except IOError as exception:
        print("Couldn't save the file. Encountered an error: %s" % exception)


def read_arguments(arguments):
    """This reads the arguments passed to the program and returns
    the latter representing the website address. If no address is
    provided, the function returns None."""
    if len(arguments) == 2:
        return arguments[1]
    else:
        return None


def print_help():
    """This funcion prints help text to instruct user how to use
    this scraping program."""
    print("\nThis is a simple program for scraping websites.")
    print("To scrape a website, pass it as an argument.")
    print("E.g. WebScraper.py this_is_the_address_of_the_website\n")


if __name__ == "__main__":
    argument = read_arguments(sys.argv)
    if argument is None:
        print_help()