import os
import shutil
import subprocess


class FileFolderPackager:

    def __init__(self, movie_root="~/Videos"):  # TODO use some xdg alias or so
        self.movie_root = movie_root
        del movie_root

    def run(self):
        for filename in os.listdir(self.movie_root):
            try:
                source_file_path = self.get_source_file_path(filename)
                with open(source_file_path) as file:
                     pass
                self.handle_file(filename)
            except IOError:
                pass  # ignore dirs

    def get_source_file_path(self, filename):
        source_file_path = self.movie_root + os.sep + filename
        return source_file_path

    def get_target_dir_path(self, filename):
        dirname, extension = os.path.splitext(filename)
        target_dir_path = self.movie_root + os.sep + dirname + os.sep
        return target_dir_path, extension

    def get_source_file_extension(self, filename):
        dirname, source_file_extension = os.path.splitext(filename)
        del dirname
        return source_file_extension

    def get_target_file_path(self, filename):
        target_file_path = self.get_target_dir_path(filename)[0] + filename
        return target_file_path


    def handle_file(self, filename):
        source_file_path = self.get_source_file_path(filename)
        (target_dir_path, extension) = self.get_target_dir_path(filename)
        target_file_path = self.get_target_file_path(filename)

        common_prefix_length = len(os.path.commonprefix(
                [source_file_path, target_dir_path, target_file_path]))

        if source_file_path[common_prefix_length:].lower() in ['.avi', '.flv', '.mkv', '.mpg']:
            self.move(filename, source_file_path, target_dir_path, target_file_path)
            return

        if source_file_path[common_prefix_length:].lower() in ['.zip', '.rar']:
            return

        print("source file path:", source_file_path[common_prefix_length:])
        print("target dir path:", target_dir_path[common_prefix_length:])
        print("target file path:", target_file_path[common_prefix_length:])

        answer = input("Shall we move? [Y/n]: ")

        if answer.lower() in ["y", "yes", ""]:
            self.move(filename, source_file_path, target_dir_path, target_file_path)

    def move (self, filename, source_file_path, target_dir_path, target_file_path):
        print("Moving...")
        # print(shutil.move(source_file_path, target_dir_path)) # does not work somehow
        extension = self.get_source_file_extension(filename)
        if extension:
            mk_command = ("mkdir", target_dir_path)
            print(" ".join(mk_command))
            subprocess.Popen(mk_command)
            mv_command = ("mv", '-f', source_file_path, target_file_path)
            print(" ".join(mv_command))
            subprocess.Popen(mv_command)
        else:
            mk_command = ("mkdir", target_dir_path[:-1] + "_had_no_extension" + os.sep)
            print(" ".join(mk_command))
            subprocess.Popen(mk_command)
            mv_command = ("mv", '-f', source_file_path, target_dir_path[:-1] + "_had_no_extension" + os.sep + filename)
            print(" ".join(mv_command))
            subprocess.Popen(mv_command)
            mv_command = ("mv", target_dir_path[:-1] + "_had_no_extension", target_dir_path)
            print(" ".join(mv_command))
            subprocess.Popen(mv_command)
        print("Done.")


if __name__ == "__main__":
    FFP = FileFolderPackager("/media/realcrypt2/Media/Video/Filme")
    FFP.run()
