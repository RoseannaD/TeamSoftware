# import socket
#
# def internet(host="8.8.8.8", port=53, timeout=3):
#   """
#   Host: 8.8.8.8 (google-public-dns-a.google.com)
#   OpenPort: 53/tcp
#   Service: domain (DNS/TCP)
#   """
#   try:
#     socket.setdefaulttimeout(timeout)
#     socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
#     return True
#   except socket.error as ex:
#     print(ex)
#     return False
#
# internet()
#
# import tkinter as tk
# from pandastable import Table
# import pandas as pd
#
# df = pd.DataFrame({
#     'A': [1,2,3,4,5,6,],
#     'B': [1,1,2,2,3,3,],
#     'C': [1,2,3,1,2,3,],
#     'D': [1,1,1,2,2,2,],
# })
#
# root = tk.Tk()
# root.title('PandasTable Example')
#
# frame = tk.Frame(root)
# frame.pack(fill='both', expand=True)
#
# pt = Table(frame, dataframe=df)
# pt.show()
#
# root.mainloop()
import os
import sys

print (os.path.dirname(sys.executable))

