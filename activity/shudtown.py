import signal
import os

def shutdown(all_predict, correct_pred):
    print("Skutecznosc:", correct_pred / all_predict)
    os.kill(os.getpid(), signal.SIGINT)