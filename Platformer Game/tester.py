try:
    import pyi_splash

    pyi_splash.update_text('UI Loaded ...')
    pyi_splash.close()
except:
    pass
print("Hello World!")
wait = input("Press enter to exit...")