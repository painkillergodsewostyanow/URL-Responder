import setting

try:
    import requests
    from time import sleep
    import os.path
    import sys
except ImportError:
    exit("install requirement (pip install -r requirements.txt)")

file_output = setting.output_file
output_cods = setting.output_cods
timeout = setting.s_timeout
output_conn_err = setting.output_conn_error

banner = """
  _   _   _   _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( U | R | L |   | R | e | s | p | o | n | d | e | r )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

 Author:           Codie Shiv
 Updated by:       https://github.com/painkillergodsewostyanow
 Special Thanks:   Mr. Ichigo kurosaki
 Instagram :       www.instagram.com/codie_shiv
 Github:           www.github.com/codie-shiv
 
 """


def responder(lst):
    lis = open(lst, 'r')
    read_lis = lis.readlines()
    result = []
    for i in read_lis:
        i = i.replace('\n', '')

        try:
            response = requests.get(i)
            status = response.status_code

            if output_cods:
                if status not in output_cods:
                    continue

            result.append(i + " --> " + str(status))
            sleep(timeout)

        except KeyboardInterrupt as e:
            print(str(e))
            exit()
        except Exception as e:
            if output_conn_err:
                result.append(i + f" --> could not connect err: {e}")
            print(i + f" --> could not connect err: {e}")

    with open(file_output, 'w') as file:
        for i in result:
            print(i, file=file)

    print('Done')


def main(__bn__):
    print(__bn__)
    print(" ")
    print(
        "NOTE: \"The target file should be in the same directory as this file is..."
        + "\" \n\"If not, then copy/move it here\"\n"
    )

    while True:
        try:
            a = input("Enter your file name: ")
            if not os.path.isfile(a):
                print("file '%s' not found" % a)
                continue
            else:
                break
        except KeyboardInterrupt as e:
            print(str(e))
            exit()
    responder(a)


if __name__ == "__main__":
    main(banner)
