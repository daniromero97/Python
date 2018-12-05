import webbrowser

print("####################### 1 #######################")
webbrowser.open("https://www.google.es/")
webbrowser.open("https://www.google.es/", 1, True)


print("####################### 2 #######################")
webbrowser.open_new("https://www.google.es/")


print("####################### 3 #######################")
webbrowser.open_new_tab("https://www.google.es/")


print("####################### 4 #######################")
browser = webbrowser.get("chromium")
browser.open("https://www.google.es/")
