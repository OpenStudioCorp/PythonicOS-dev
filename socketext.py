import tkinter as tk
import socket
import threading
def send_message():
    message = entry.get()  # Get the text from the entry box
    sock1.sendall(message.encode())  # Send the message over the socket
    entry.delete(0, tk.END)  # Clear the entry box

def receive_message():
    while True:
        data = sock2.recv(1024)  # Receive data from the socket
        print('Received:', data.decode())

# Create the Tkinter application window
window = tk.Tk()
window.title("Socket Client")

# Create the input box
entry = tk.Entry(window)
entry.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Start the Tkinter event loop
window.mainloop()

# Close the sockets
sock1.close()
sock2.close()
