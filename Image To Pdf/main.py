from PIL import Image
import os

class ImageToPDF:
    def __init__(self):
        self.valid_formats = (".jpg", ".jpeg", ".png", ".JPG", ".PNG")
        self.pictures = []
        self.directory = ""
        self.is_merge_pdf = True

    def get_user_dir(self):
        """Allow user to choose image directory."""
        msg = "\n1. Current directory\n2. Custom directory\nEnter a number: "
        user_option = self.get_valid_input(msg, [1, 2])

        self.directory = os.getcwd() if user_option == 1 else input("\nEnter custom directory: ").strip()
        if not os.path.isdir(self.directory):
            print(f"[Error] The directory {self.directory} does not exist.")
            return False
        return True

    def get_valid_input(self, msg, valid_options):
        """Get and validate user input."""
        while True:
            try:
                user_input = int(input(msg))
                if user_input in valid_options:
                    return user_input
                else:
                    print(f"\n*Invalid input*\n{msg}")
            except ValueError:
                print(f"\n*Invalid input*\n{msg}")

    def filter_images(self, item):
        return item.lower().endswith(self.valid_formats)

    def sort_files(self):
        return sorted(os.listdir(self.directory))

    def get_pictures(self):
        pictures = list(filter(self.filter_images, self.sort_files()))
        if not pictures:
            print(f" [Error] There are no pictures in the directory: {self.directory} ")
            return False
        print(f"Found picture(s):")
        return pictures

    def select_pictures(self, pictures):
        """Allow user to manually pick each picture or merge all."""
        listed_pictures = {index + 1: pic for index, pic in enumerate(pictures)}
        for index, pic in listed_pictures.items():
            print(f"{index}: {pic}")

        user_input = input("\nEnter the number(s) - (comma separated/no spaces) or (A or a) to merge All\nChoice: ").strip().lower()

        if user_input == "a":
            return pictures

        selected_pictures = []
        for number in user_input.split(','):
            try:
                pic = listed_pictures.get(int(number))
                if pic:
                    selected_pictures.append(pic)
            except ValueError:
                pass

        self.is_merge_pdf = False
        return selected_pictures

    def convert_pictures(self):
        """Convert pictures according to user selection and save as PDF."""
        pictures = self.get_pictures()
        if not pictures:
            return

        if len(pictures) >= 2:
            pictures = self.select_pictures(pictures)

        if self.is_merge_pdf:
            for picture in pictures:
                self.pictures.append(Image.open(os.path.join(self.directory, picture)).convert("RGB"))
            self.save()
        else:
            for picture in pictures:
                self.save(Image.open(os.path.join(self.directory, picture)).convert("RGB"), picture, False)

        self.is_merge_pdf = True
        self.pictures = []
        print(f"\n{'#'*30}")
        print("            Done! ")
        print(f"{'#'*30}\n")

    def save(self, image=None, title="All-PDFs", is_merge_all=True):
        """Save images to PDF."""
        if is_merge_all:
            if self.pictures:
                self.pictures[0].save(
                    os.path.join(self.directory, f"{title}.pdf"), 
                    save_all=True, 
                    append_images=self.pictures[1:]
                )
        else:
            image.save(os.path.join(self.directory, f"{title}.pdf"))

if __name__ == "__main__":
    process = ImageToPDF()
    if process.get_user_dir():
        process.convert_pictures()

        while True:
            user_choice = input("Press (R or r) to Run again\nPress (C or c) to change directory\nPress (Any Key) To Exit\nChoice: ").lower()
            if user_choice == 'r':
                process.convert_pictures()
            elif user_choice == 'c':
                if process.get_user_dir():
                    process.convert_pictures()
            else:
                break
