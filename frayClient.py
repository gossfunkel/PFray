import socket
import feudNetworking
# for standard net connections, use feudNetworking lib

live = 1

def startup():
    global username
    global host
    host = raw_input("Enter address of Feud Server: ")
    loginOrNew = raw_input("New user?\n")
    if loginOrNew == "yes" or "Yes" or "y" or "Y":
        username = raw_input("Please enter desired username: ")
        password = raw_input("Please enter desired [insecure] password: ")
        new = 1
    else:
        username = raw_input("Please enter username: ")
        password = raw_input("Please enter password: ")
        new = 0
    package = ('LOGI ' + username + password + new)
    feudNetworking.cLient(package)

def logOut(reason):
    package = ('LOGO ' + reason)
    feudNetworking.cLient(package)

def printHelp():
    print "---HELP---"
    print "Available commands: "
    print ' '
    print "logout   -   exit game"

def main():
    while live:
        command = raw_input("FEUD:> ")
        if command == "logout" or "log out" or "LOGOUT" or "LOGO":
            logOut("MENU")
            break
        if command == "help" or "HELP" or "?":
            printHelp()

def shutdown():
    print "logging out"

startup()
main()
shutdown()

