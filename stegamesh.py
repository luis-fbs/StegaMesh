class StegaMesh:
    def __init__(self, filename: str):
        with open(filename, "r") as file:
            lines = file.readlines()
            file.seek(0)
            self.file = file.read()
            self.filename = filename
            self.v_old = [line[:-1] for line in lines if line.startswith("v ")]
            self.v_new = [line[:-1] for line in lines if line.startswith("v ")]

    def hide_text(self, text: str):
        text += "" if text.endswith('\n') else '\n'
        if (len(text) > len(self.v_new) or text.count('\n') > 1):
            raise ValueError("Invalid text size.")

        for x in range(len(text)):
            v = self.v_new[x]
            v = v.split()
            index = 1 + x%3
            v[index] = v[index][:-3] + f"{ord(text[x]):03d}"
            self.v_new[x] = " ".join(v)

    def extract_text(self):
        text = ""
        for x in range(len(self.v_new)):
            index = 1 + x%3
            v = self.v_new[x].split()
            text += chr(int(v[index][-3:]))
            if v[index][-3:] == "010":
                break
        return text

    def save(self, dest: str = ""):
        if not dest:
            dest = f"{self.filename[:-4]}_hidden.obj"

        for x in range(len(self.v_old)):
            self.file = self.file.replace(self.v_old[x], self.v_new[x])
            v = self.v_new[x].split()
            index = 1 + x%3
            if v[index][-3:] == "010":
                break

        with open(dest, "w") as file:
            file.write(self.file)
