import sys

import requests


def get_website_contents(website_address):
    """This function retrieves and returns the contents of the
    website that is passed to it as an argument."""
    website = requests.get(website_address)
    try:
        website.raise_for_status()
    except Exception as exception:
        print("Error encountered: %s" % exception)
        return None
    return website.content


def write_website_to_file(contents, filename):
    """This function writes the website contents to a file
    as bytes."""
    write_contents_bytes = bytearray(contents)
    try:
        with open(filename, "wb") as file:
            file.write(write_contents_bytes)
    except IOError as exception:
        print("Couldn't save the file. Encountered an error: %s" % exception)


def read_arguments(arguments):
    """This reads the arguments passed to the program and returns
    the latter representing the website address. If no address is
    provided, the function returns None."""
    if len(arguments) == 3:
        return arguments[1], arguments[2]
    elif len(arguments) == 2:
        return arguments[1], None
    else:
        return None


def print_help():
    """This funcion prints help text to instruct user how to use
    this scraping program."""
    print("\nThis is a simple program for scraping websites.\n"
          "To scrape a website, pass it as an argument and optionally\n"
          "pass also the name of the file you want the results to be saved\n"
          "as a second argument.\n"
          "Example 1. WebScraper.py address_of_the_website\n"
          "Example 2. WebScraper.py address_of_the_website save_contents_here")


if __name__ == "__main__":
    address, filename = read_arguments(sys.argv)
    if address is None:
        print_help()
    else:
        content = get_website_contents(address)
        if content is None:
            print("Website does not exist")
        else:
            if filename is not None:
                write_website_to_file(content, filename)
            else:
                while True:
                    user_choice = input(
                        "Give a name where the contents of the website will be saved, or (q)uit.").strip()
                    if user_choice == "Q" or user_choice == "q":
                        break
                    elif user_choice == "":
                        print("You have to insert a filename.")
                    else:
                        write_website_to_file(content, user_choice)
                        break
