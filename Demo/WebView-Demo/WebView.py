import webview

url = input("Inserisci un URL da aprire nella WebView: ")
webview.create_window("WebView Demo", url)
webview.start()
