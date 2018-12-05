# webbrowser

- It allows to open a document or website in the default browser on Unix, Windows and Max OS X systems.
- Enables viewing in a new tab, window or in the current one, whenever possible. If this is not possible, normally the document is displayed in a new tab, depending on the browser.
- In most cases it will be enough to use the open () function.
- webbrowser also works as a script.

    ```
    python -m webbrowser -t "https://www.google.es/"
    ```

### functions

##### open(url, new=0, autoraise=True)

- Open the url in the browser by default.
- If new is 0, it opens in the same browser window.
- If it is 1, it opens in a new window.
- If it is 2, it opens in a new tab.
- The autoraise variable indicates whether the window is brought to the front.

```
webbrowser.open("https://www.google.es/")
webbrowser.open("https://www.google.es/", 1, True)
```

##### open_new(url)

- Open url in a new window of the default browser, if possible, otherwise, open url in the only browser window.

```
webbrowser.open_new("https://www.google.es/")
```

##### open_new_tab(url)

- Open url in a new page (“tab”) of the default browser, if possible, otherwise equivalent to open_new().

```
webbrowser.open_new_tab("https://www.google.es/")
```

##### get(using=None)

- Return a controller object for the browser type using. If using is None, return a controller for a default browser appropriate to the caller’s environment.

```
browser = webbrowser.get("chromium")
browser.open("https://www.google.es/")
```

##### oficial documentation:

- https://docs.python.org/3/library/webbrowser.html