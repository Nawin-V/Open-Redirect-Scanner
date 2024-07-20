from utils import check_internet
import argparse
from utils import banner
import webbrowser
from includes import scan
from includes import read_file
from includes import write_output
import validators

def validate_url(url):
    return validators.url(url)

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-u","--url",nargs='+',type=str,help="enter ther url")
parser.add_argument("-i","--input",help="enter the input filename")
parser.add_argument("-o","--output",help="enter the output filename")
parser.add_argument("-h","--help",action="store_true",help="Help menu")
parser.add_argument("-b","--blog",action="store_true",help="read about the bug")

args = parser.parse_args() 

if args.help:
    banner.helpbanner()
    
if args.url and not args.output:
    banner.banner()
    for url in args.url:
        if validate_url(url.strip()):
            scan.openscan(url.strip())
        else:
            print(f"Invalid URL: {url.strip()}\nEnter a valid URL")

if args.url and  args.output:
    banner.banner()
    for url in args.url:
        if validate_url(url.strip()):
            scan.openscan(url.strip(),args.output)
        else:
            print(f"Invalid URL: {url.strip()}\nEnter a valid URL")

if args.input and args.output:
    banner.banner()
    urls = read_file.read(args.input)  
    if urls:
        for url in urls:
            scan.openscan(url.strip(), args.output)

if args.input and not args.output:
    banner.banner()
    urls = read_file.read(args.input)  
    if urls:
        for url in urls:
            scan.openscan(url.strip(), args.output)    

if args.blog:
    blog_url="https://brightsec.com/blog/open-redirect-vulnerabilities/"
    webbrowser.open(blog_url)  

if __name__=="__main__":
    if check_internet.chk_net():
        pass
    else:
        print("check your network connection")
    