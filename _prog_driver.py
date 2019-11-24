import time
from pynput.keyboard import Key, Controller
import threading

keyboard = Controller()
results = None
import _prg_undr_test as prog
        
def enter(data):
    for d in data:
        keyboard.press(d)
        keyboard.release(d)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

def launch_typer(input_data):
    time.sleep(1)
    for d in input_data:
        enter(d)

def launch_prg(expected_results):
    results = prog.do_work()
    try:
        assert results == expected_results, "\n **ERROR** \texpecting: " + str(expected_results) + "\n\trecieved: " + str(results) +"\n"
    except Exception as e: print(e)
    
def test(input_data, expected_results):
    
    prog_ut = threading.Thread(target=launch_prg, args=(expected_results,),daemon=True)
    typer = threading.Thread(target=launch_typer, args=(input_data,), daemon=True)

    prog_ut.start()
    typer.start()
    prog_ut.join()
