import os,sys
args = sys.argv

flatpak_lookup={
        'office':'org.onlyoffice.desktopeditors',
        'code':'com.vscodium.codium',
        'brave':'com.brave.Browser'
}

result = flatpak_lookup.get(args[1])

if result:
    pwd = os.getcwd()

    s = ""
    a = args[2:]
    for i in a:
        s += f"{pwd}/{i} "

    command = f"flatpak run {result} {s}"
    os.system(command)


