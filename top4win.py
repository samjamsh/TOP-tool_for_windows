import os, sys, platform

# pin: Proccess Identification Number
# pid: Proccess ID or Proccess Identification
# pn: Process Name (proccess name only without the extension)
# pcn: Proccess Complete Name (complete name of the proccess)

# (this function) checks the operating system (checks the running OS)
def os_checking():
    system = 'Windows'
    os = [list(platform.uname())[0],platform.platform()]
    os = os[1][:7],os[0] # operating system name must be Windows
    boolean = os[0] == os[1]
    guess = os[0] == system or os[1] == system
    o_s = os[0] == system and os[1] == system
    if boolean is True and o_s is True:
        pass # operating system checked successfully

    elif guess == True:
        print('operating system not confirmed, the tool may run incorrectlly')

    else:
        sys.exit('operating system must be windows')


def int_convert(value,code):
    try:
        try:
            if code != 3 and code != 4:
                return int(value)
            else:
                return value

        except:
            pass

    except Exception as err:
        pass

def kill_proccess(option,signterm,value,numbers,names):

    try:
        if signterm == 15:
            signterm = " " # this option terminates the program but wihtout forcing it 
        elif signterm == 9:
            signterm = " /f " # this option forces the program to stop 
        else:
        # if signterm code is not valid or unknown, exits the tool
            sys.exit(f"error: wrong signterm code {signterm}")

        if option == 1:
        # option one choiced, PIN option (proccess identification number)
            pid = int_convert(numbers[value],1)
            command = f"taskkill{signterm}/pid {pid}"
            os.system(command)

        elif option == 2:
        # option two choiced, PID option (proccess identification)
            command = f"taskkill{signterm} /pid {value}"
            os.system(command)

        elif option == 3:
        # option three choiced, PN option (program name)
            # if given value is greatter than four characters
            if len(value) > 4:
                exe_check = value[-4] + value[-3] + value[-2] + value[-1]
                if exe_check != '.exe':
                # if the lasts four characters are not '.exe'
                    value = value + ".exe"
                    pid = names[value]
                    command = f"taskkill{signterm} /pid {pid}"
                    os.system(command)

                else:
                # if the lasts four characters are '.exe'
                    pid = numbers[value]
                    command = f"taskkill{signterm} /pid {pid}"
                    os.system(command)

            else:
            # if the given value is not greatter than four, if it's less than four 
                pid = numbers[value]
                command = f"taskkill{signterm} /pid {pid}"
                os.system(command)


        elif option == 4:
        # option four choiced, PCN option (program complete name or complete proccess name)
            pid = names[value]
            command = f"taskkill{signterm} /pid {pid}"
            os.system(command)

        else:

            sys.exit(f"error: wrong option code {option}")

    except Exception as error:
        sys.exit(error)


def proccess():
    try:
        numbers = {} # this dict stores 'pin' as key and 'pid' as value (all pin's and pid's)
        max = 34
        min = 25
        names = {} # this dict stores 'proccess name' as key and 'pid' as value (do it will all proccess names and pid's)
        number = 0
        data = os.popen("tasklist").read()
        line, lines = '',[]
        n = -3 
        for character in data:
            line += character
            if character == '\n':
            # if character is an break line (\n) 
                lines.append(line)
                number += 1 
                n +=1
                proccess_pid = line[min:max]
                name_end = line.find(" ")
                process_name = line[:name_end]

                if number == 3:
                    
                    names = {} # cleans (dict) 'names'
                    numbers = {} # cleans (dict) 'numbers'
                    lines = [] # cleans (list) 'lines'

                names[process_name] = proccess_pid
                numbers[n] = proccess_pid
                line = ""

            else:
            # if character is not equal to break line '\n' just keep adding/appending character to 'line' variable
                pass

        n=0 # pin auxiliary var (variable that represents pin)
        print("PIN ==== ====== PCN ==================  PID =========================================",end="\n\n")
        for each_line in lines:
        # for each line in all lines (proccess info's separeted in lines)
            n+=1
            str_n = str(n)
            buffer_n = (8-len(str_n)) * " "
            buffer_n = str_n + buffer_n 
            print(f"{buffer_n} {each_line}",end="")
        
        return numbers, names, lines

    except Exception as error:
        sys.exit(error)

    except:
        sys.exit()

def user_input():
    print('1.PIN, 2.PID, 3.PN, 4.PCN; and signterm: 9. force kill, 15. terminates/kill')
    try:
        # asks the user option to use
        user_option = input("option: ").strip()

        # asks the user signalterm code to send to the program to terminate(kill)
        signterm = input("signterm: ").strip()

        if user_option == '1':
        # if choiced option is one, asks for an data input that choices(selects to program)
            proccess_number = input("proccess id number: ")
            return 1, signterm, proccess_number # returns option choiced, signalterm code, and choiced program (program to terminate)

        elif user_option == '2':
        # if choiced option is two, asks for program to terminate
            proccess_id = input("proccess id: ")
            return 2, signterm, proccess_id # returns option, signterm code and program

        elif user_option == '3':
        # if it's option three choiced, asks for program and returns usefully infos
            proccess_name = input("proccess name: ")
            return 3, signterm, proccess_name

        elif user_option == '4':
            # if it's option number four, asks for program to terminate(some program identification as well)
            proccess_complete_name = input("proccess complete name: ")
            return 4, signterm , proccess_complete_name # option, signterm, some identification of the program to terminate

        elif signterm != '9' or signterm != '15':
        # if choiced signterm codes aren't 9 or 15, exits the tool
            # wrong signterm code
            sys.exit(f"signterm must be 9 or 15")

        else:
        # elif choiced options are not 1,2,3 or 4
            # exits the tool, bacause of the invalid option choiced
            sys.exit("choice option 1 to 4 only")

    except Exception as error:
        sys.exit(error)

    except:
        sys.exit()


# (this function) checking if operating system is windows
os_checking()
pin_pid, pcn, proccess_lines = proccess()

# user data inputs
option, signterm, value = user_input()
value = int_convert(value,option)
signterm = int_convert(signterm,0)

# (this function) kills the proccess
kill_proccess(option,signterm,value,pin_pid,pcn)
