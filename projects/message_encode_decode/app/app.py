from tkinter import Button, Entry, StringVar, Tk, Label
import base64
from tkinter.constants import BOTTOM


class Application:
    def main(self):
        root = Tk()

        root.geometry("500x300")
        root.resizable(0, 0)
        root.title("David - Message Encode and Decode")

        Label(root, text="ENCODE DECODE", font="arial 20 bold").pack()
        Label(root, text="David", font="arial 20 bold").pack(side=BOTTOM)

        Text = StringVar()
        private_key = StringVar()
        mode = StringVar()
        Result = StringVar()
        Label(root, font="arial 12 bold", text="MESSAGE").place(x=60, y=60)
        Entry(root, font="arial 10", textvariable=Text, bg="ghost white").place(
            x=290, y=60
        )
        Label(root, font="arial 12 bold", text="KEY").place(x=60, y=90)
        Entry(root, font="arial 10", textvariable=private_key, bg="ghost white").place(
            x=290, y=90
        )

        Label(root, font="arial 12 bold", text="MODE(e-encode, d-decode)").place(
            x=60, y=120
        )
        Entry(root, font="arial 10", textvariable=mode, bg="ghost white").place(
            x=290, y=120
        )
        Entry(root, font="arial 10", textvariable=Result, bg="ghost white").place(
            x=290, y=150
        )

        Button(
            root,
            font="arial 10 bold",
            text="RESULT",
            padx=2,
            bg="LightGray",
            command=lambda: self.parse_mode(mode, Result, private_key.get(), Text),
        ).place(x=60, y=150)
        Button(
            root,
            font="arial 10 bold",
            text="RESET",
            width=6,
            padx=2,
            bg="LimeGreen",
            command=lambda: self.reset(Text, private_key, mode, Result),
        ).place(x=80, y=190)
        Button(
            root,
            font="arial 10 bold",
            text="EXIT",
            width=6,
            padx=2,
            bg="OrangeRed",
            command=exit,
        ).place(x=180, y=190)

        root.mainloop()

    def encode(self, key, message):
        enc = []

        for i in range(len(message)):
            key_c = key[i % len(key)]
            enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def decode(self, key, message):
        dec = []
        message = base64.urlsafe_b64decode(message).decode()
        for i in range(len(message)):
            key_c = key[i % len(key)]
            dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
        return "".join(dec)

    def parse_mode(self, mode, result, private_key, text: StringVar):
        if mode.get() == "e":
            result.set(self.encode(private_key, text.get()))
        elif mode.get() == "d":
            result.set(self.decode(private_key, text.get()))
        else:
            result.set("Invalid Mode")

    def exit(self):
        self.root.destroy()

    def reset(self, text, private_key, mode, result):
        text.set("")
        private_key.set("")
        mode.set("")
        result.set("")


if __name__ == "__main__":
    application = Application()
    application.main()
