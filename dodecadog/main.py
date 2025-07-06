# import dpg_gui
import winup_gui

if __name__ == "__main__":
    winup_gui.run()
    # dpg_gui.run()

    ### this breaks
    # thread_1 = threading.Thread(target=winup_gui.run)
    # thread_1.start()
    # print("started thread 1...")

    # thread_2 = threading.Thread(target=dpg_gui.run)
    # thread_2.start()
    # print("started thread 2...")
