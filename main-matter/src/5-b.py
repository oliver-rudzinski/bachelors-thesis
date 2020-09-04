def remove_corrupted(self, files):
    return if files == {}

    corrupted_files = []
    for name, content in files.items():
        try:
            et.fromstring(content)
        except et.ParseError:
            self.logger.error(
                'XML File Corrupted | File Name: "{}"'.format(name)
            )
            self.logger.info('Skipping file "{}"'.format(name))
            corrupted_files.append(name)
            self.error_files += 1
            self._set_file_tags(
                    self.src_bucket,
                    f"{self.src_dir}{name}",
                    "xmlCorr-err",
                )
    for file in corrupted_files:
        files.pop(file)